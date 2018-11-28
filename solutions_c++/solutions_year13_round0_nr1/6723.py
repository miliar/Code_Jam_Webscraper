#include<iostream>
#include<cctype>
#include<string>
#include<cmath>
#include<algorithm>
#include<functional>
#include<vector>
#include<cstring>
#include<queue>
#include <numeric>
#include<map>
#include<set>
#include<stack>
#include<fstream>
#include<sstream>
using namespace std;

char grid[4][4];
char go() {
  //rows
  int x, o, t, dot;
  x = o = t = dot = 0;

  for (int c = 0; c < 4; ++c) {
    x = o = t = 0;
    for (int r = 0; r < 4; ++r) {
      if (grid[c][r] == 'X') ++x;
      if (grid[c][r] == 'O') ++o;
      if (grid[c][r] == 'T') ++t;
      if (grid[c][r] == '.') ++dot;
    }
    if (x == 4 | (x == 3 && t == 1)) return 'X';
    if (o == 4 | (o == 3 && t == 1)) return 'O';
  }


  //cols
  for (int r = 0; r < 4; ++r) {
    x = o = t = 0;
    for (int c = 0; c < 4; ++c) {
      if (grid[c][r] == 'X') ++x;
      if (grid[c][r] == 'O') ++o;
      if (grid[c][r] == 'T') ++t;
      if (grid[c][r] == '.') ++dot;
    }
    if (x == 4 | (x == 3 && t == 1)) return 'X';
    if (o == 4 | (o == 3 && t == 1)) return 'O';
  }

  //diagonals fwd;
  x = o = t = 0;
  for (int r = 0; r < 4; ++r) {
    if (grid[r][r] == 'X') ++x;
    if (grid[r][r] == 'O') ++o;
    if (grid[r][r] == 'T') ++t;
    if (grid[r][r] == '.') ++dot;
  }
  if (x == 4 | (x == 3 && t == 1)) return 'X';
  if (o == 4 | (o == 3 && t == 1)) return 'O';
  //diagonals bwd
  x = o = t = 0;
  int c = 0;
  for (int r = 3; r >= 0; --r) {
    if (grid[r][c] == 'X') ++x;
    if (grid[r][c] == 'O') ++o;
    if (grid[r][c] == 'T') ++t;
    if (grid[r][c] == '.') ++dot;
    ++c;
  }
  if (x == 4 | (x == 3 && t == 1)) return 'X';
  if (o == 4 | (o == 3 && t == 1)) return 'O';


  if (dot) return 'I';

  return 'D';
}
int main() {
  ifstream cin("input.in");
  ofstream cout("out.txt");
  int N, ca = 0;

  cin >> N;

  while (N--) {
    cout << "Case #" << ++ca << ": " ;
    for (int c = 0; c < 4; ++c)
      for (int r = 0; r < 4; ++r)
        cin >> grid[c][r];
    char c = go();
    if (c == 'X') cout << "X won";
    else if (c == 'O') cout << "O won";
    else if (c == 'D') cout << "Draw";
    else cout << "Game has not completed";
    cout << endl;

  }

  return 0;
}

