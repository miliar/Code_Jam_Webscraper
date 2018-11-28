#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <string.h>
#include <algorithm>
#include <set>
#include <cstdio>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;

int main() {
  int TC; cin >> TC;
  for (int t = 1; t <= TC; t++) { 
    printf("Case #%d: ", t);
    
    vs board(4);
    for(int i = 0; i < 4; ++i) {
      cin >> board[i];
    }

    bool X = false, O = false, dot = false;
    int Xdiag1 = 0, Odiag1 = 0, Xdiag2 = 0, Odiag2 = 0;
    for(int i = 0; i < 4; ++i) {
      // Diagonals
      if (board[i][i] == 'X') Xdiag1++;
      if (board[i][i] == 'O') Odiag1++;
      if (board[i][i] == 'T') {
        Xdiag1++;
        Odiag1++;
      }
      if (board[i][3-i] == 'X') Xdiag2++;
      if (board[i][3-i] == 'O') Odiag2++;
      if (board[i][3-i] == 'T') {
        Xdiag2++;
        Odiag2++;
      }
      int Xcount = 0, Ocount = 0;
      int Xcol = 0, Ocol = 0;
      for(int j = 0; j < 4; ++j) {
        // Rows
        if (board[i][j] == 'X') Xcount++;
        if (board[i][j] == 'O') Ocount++;
        if (board[i][j] == 'T') {
          Xcount++;
          Ocount++;
        }
        if (board[i][j] == '.') dot = true;
        // Columns
        if (board[j][i] == 'X') Xcol++;
        if (board[j][i] == 'O') Ocol++;
        if (board[j][i] == 'T') {
          Xcol++;
          Ocol++;
        }
      }
      if (Xcount == 4 || Xcol == 4) X = true;
      if (Ocount == 4 || Ocol == 4) O = true;
    }

    if (Xdiag1 == 4 || Xdiag2 == 4) X = true;
    if (Odiag1 == 4 || Odiag2 == 4) O = true;

    if (X || O) {
      cout << (X ? "X won" : "O won") << endl;
    } else if (dot) {
      cout << "Game has not completed" << endl;
    } else {
      cout << "Draw" << endl;
    }
  }
  return 0;
}
