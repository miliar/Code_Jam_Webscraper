#include <iostream>
#include <vector>

int main() {
  int T;
  std::cin >> T;
  for (int casenum = 1; casenum <= T; ++casenum) {
    int rows, columns;
    std::cin >> rows >> columns;

    std::vector<std::vector<int> > pattern;
    for (int i = 0; i < rows; ++i) {
      std::vector<int> row;
      for (int j = 0; j < columns; ++j) {
        int height;
        std::cin >> height;
        row.push_back(height);
      }
      pattern.push_back(row);
    }

    bool good = true;

    while (rows > 0 && columns > 0) {
      int m = 101;
      int mi = -1, mj = -1;
      for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < columns; ++j) {
          if (pattern[i][j] < m) {
            m = pattern[i][j];
            mi = i;
            mj = j;
          }
        }
      }

      bool row_removable = true;
      for (int j = 0; j < columns; ++j) {
        if (pattern[mi][j] != m) {
          row_removable = false;
          break;
        }
      }

      if (row_removable) {
        pattern.erase(pattern.begin() + mi);
        rows -= 1;
      } else {
        bool col_removable = true;
        for (int i = 0; i < rows; ++i) {
          if (pattern[i][mj] != m) {
            col_removable = false;
            break;
          }
        }

        if (col_removable) {
          for (int i = 0; i < rows; ++i) {
            pattern[i].erase(pattern[i].begin() + mj);
          }
          columns -= 1;
        } else {
          good = false;
          goto done;
        }
      }
    }

  done:

    std::cout << "Case #" << casenum << ": " << (good ? "YES" : "NO") << std::endl;

  }
}
