#include "Lawnmower.h"
#include <assert.h>


namespace codejam {

bool Lawnmower::tryCutCol(int col, int target) {
  printf("tryCutCol col: %d, target: %d\n", col, target);
  for (int i = 0; i < n_; ++i) {
    if (board_[i][col] > target) {
      return false;
    }
  }
  return true;
}

bool Lawnmower::brute() {
  for (int i = 0; i < n_; ++i) {
    bool canCutRow = true;
    int min = board_[i][0];
    bool allSame = true;
    for (int j = 0; j < m_; ++j) {
      if (board_[i][j] < min) {
        min = board_[i][j];
        allSame = false;
      } else if (board_[i][j] > min){
        allSame = false;
      } else {
      }
    }
    if (!allSame) {
      for (int j = 0; j < m_; ++j) {
        int cur = board_[i][j];
        if (cur == min) {
          if (!tryCutCol(j, cur)) {
            return false;
          }
        }
      }
    }
  }
  return true;
}

void Lawnmower::solve(std::ostream& output, std::istream& input) {
  int t, _t = 1;
  input >> t;
  while (_t <= t) {
    int n, m;
    input >> n >> m;
    int **board = new int*[n];
    for (int i = 0; i < n; ++i) {
      board[i] = new int[m];
      for (int j = 0; j < m; ++j) {
        input >> board[i][j];
      }
    }
    Lawnmower k(board, n, m);
    const char* result = k.brute() ? "YES" : "NO";
    output << "Case #" << _t << ": " << result << std::endl;
    _t++;
  }
}

}