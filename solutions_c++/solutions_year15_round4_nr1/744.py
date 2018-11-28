#include <iostream>
#include <string>

using namespace std;

int r, c;
int grid[200][200];

bool points_to_something(int i, int j, int setting) {
  if (setting == 1) {
    for (int ii = i-1; ii >= 0; --ii) {
      if (grid[ii][j] != 0) return true;
    }
  } else if (setting == 2) {
    for (int jj = j-1; jj >= 0; --jj) {
      if (grid[i][jj] != 0) return true;
    }
  } else if (setting == 3) {
    for (int ii = i+1; ii < r; ++ii) {
      if (grid[ii][j] != 0) return true;
    }
  } else {
    for (int jj = j+1; jj < c; ++jj) {
      if (grid[i][jj] != 0) return true;
    }
  }
  return false;
}

int main() {
  int t; cin >> t;
  for (int test = 1; test <= t; ++test) {
    cin >> r >> c;
    string dummy; getline(cin, dummy);
    for (int i = 0; i < r; ++i) {
      string row; getline(cin, row);
      for (int j = 0; j < c; ++j) {
        switch (row[j]) {
          case '.':
            grid[i][j] = 0; break;
          case '^':
            grid[i][j] = 1; break;
          case '<':
            grid[i][j] = 2; break;
          case 'v':
            grid[i][j] = 3; break;
          case '>':
            grid[i][j] = 4; break;
        }
      }
    }
    int necessary_fixes = 0;
    for (int i = 0; i < r && necessary_fixes >= 0; ++i) {
      for (int j = 0; j < c && necessary_fixes >= 0; ++j) {
        if (grid[i][j] == 0) continue;
        if (points_to_something(i, j, grid[i][j])) continue;
        bool found_safety = false;
        for (int k = 1; k <= 4; ++k) {
          if (points_to_something(i, j, k)) {
            found_safety = true;
            break;
          }
        }
        if (found_safety) {
          necessary_fixes++;
        } else {
          necessary_fixes = -1;
        }
      }
    }
    cout << "Case #" << test << ": ";
    if (necessary_fixes >= 0) {
      cout << necessary_fixes;
    } else {
      cout << "IMPOSSIBLE";
    }
    cout << endl;
  }
  return 0;
}