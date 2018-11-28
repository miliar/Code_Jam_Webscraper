#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>

#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>

using namespace std;

typedef long long int64;

const int MAX_D = 4;
const int DX[MAX_D] = {-1, 0, 1, 0};
const int DY[MAX_D] = {0, 1, 0, -1};

vector<int> Pow3;
int Rows, Columns, SolutionCount;
unordered_set<int64> Solutions;

inline int Valid(const vector< vector<int> > &board, const int x, const int y) {
  int count = 0;
  for (int d = 0; d < MAX_D; ++d) {
    int nx = x + DX[d], ny = (y + DY[d] + Columns) % Columns;
    if (0 <= nx && nx < Rows && board[x][y] == board[nx][ny])
      ++count;
  }
  return count == board[x][y];
}

inline int64 Encode(const vector< vector<int> > &board) {
  int64 code = 0;
  for (int x = 0; x < Rows; ++x)
    for (int y = 0; y < Columns; ++y)
      code = 3 * code + (board[x][y] - 1);
  return code;
}

void Back(vector< vector<int> > &board, const int y) {
  if (y == Columns) {
    bool valid = true;
    for (int x = 0; x < Rows && valid; ++x)
      if (!Valid(board, x, 0) || !Valid(board, x, Columns - 1))
        valid = false;
    if (valid && Solutions.find(Encode(board)) == Solutions.end()) {
      ++SolutionCount;
      for (int shift = 0; shift < Columns; ++shift) {
        vector< vector<int> > shiftedBoard(Rows, vector<int>(Columns));
        for (int x = 0; x < Rows; ++x)
          for (int y = 0; y < Columns; ++y)
            shiftedBoard[x][y] = board[x][(y + shift) % Columns];
        Solutions.insert(Encode(shiftedBoard));
      }
    }
    return;
  }
  for (int mask = 0; mask < Pow3[Rows]; ++mask) {
    for (int x = 0, m = mask; x < Rows; ++x, m /= 3)
      board[x][y] = 1 + m % 3;
    bool valid = true;
    if (y > 1) {
      for (int x = 0; x < Rows && valid; ++x)
        if (!Valid(board, x, y - 1))
          valid = false;
    }
    if (valid)
      Back(board, y + 1);
  }
}

void Solve() {
  Solutions = unordered_set<int64>();
  SolutionCount = 0;
  vector< vector<int> > board(Rows, vector<int>(Columns));
  Back(board, 0);
}

int main() {
  ifstream cin("input.txt");
  ofstream cout("output.txt");
  Pow3.push_back(1);
  for (int i = 1; i <= 7; ++i)
    Pow3.push_back(Pow3.back() * 3);
  int testCount;
  cin >> testCount;
  for (int t = 1; t <= testCount; ++t) {
    cin >> Rows >> Columns;
    if (Rows == 6) {
      int answers[7] = {0, 2, 2, 6, 4, 2, 19};
      SolutionCount = answers[Columns];
    } else {
      Solve();
    }
    cout << "Case #" << t << ": " << SolutionCount << "\n";
  }
  cin.close();
  cout.close();
  return 0;
}
