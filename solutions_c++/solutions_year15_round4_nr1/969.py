#include <iostream>
#include <iomanip>
#include <cassert>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int t;
  cin >> t;
  for (int tt = 1; tt <= t; ++tt) {
    int r, c;
    cin >> r >> c;
    vector<string> board(r);
    for (int i = 0; i < r; ++i) {
      cin >> board[i];
    }

    vector<int> rowSum(r, 0);
    vector<int> colSum(c, 0);
    for (int i = 0; i < r; ++i) {
      for (int j = 0; j < c; ++j) {
        if (board[i][j] != '.') {
          ++rowSum[i];
          ++colSum[j];
        }
      }
    }
    bool solvable = true;
    for (int i = 0; i < r; ++i) {
      for (int j = 0; j < c; ++j) {
        if (board[i][j] != '.'
            && rowSum[i] == 1
            && colSum[j] == 1) {
          solvable = false;
        }
      }
    }
    if (!solvable) {
      cout << "Case #" << tt << ": IMPOSSIBLE" << endl;
      continue;
    }

    int res = 0;
    for (int i = 0; i < r; ++i) {
      for (int j = 0; j < c; ++j) {
        if (board[i][j] != '.') {
          if (board[i][j] == '<') ++res;
          break;
        }
      }
      for (int j = c - 1; j >= 0; --j) {
        if (board[i][j] != '.') {
          if (board[i][j] == '>') ++res;
          break;
        }
      }
    }
    for (int j = 0; j < c; ++j) {
      for (int i = 0; i < r; ++i) {
        if (board[i][j] != '.') {
          if (board[i][j] == '^') ++res;
          break;
        }
      }
      for (int i = r - 1; i >= 0; --i) {
        if (board[i][j] != '.') {
          if (board[i][j] == 'v') ++res;
          break;
        }
      }
    }

    cout << "Case #" << tt << ": " << res << endl;
  }
  return 0;
}
