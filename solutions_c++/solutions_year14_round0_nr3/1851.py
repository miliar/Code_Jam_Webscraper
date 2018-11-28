#include <iostream>
#include <vector>

using namespace std;

struct Mine {
  Mine(int row_, int col_, int mines_) 
      : row(row_), col(col_), mines(mines_), size(row * col),
        minefield(row, vector<bool>(col, false)),
        neigh(row, vector<int>(col, 0)), 
        seedi(0), seedj(0) {
  }

  bool search() {
    return find(0, mines);
  }

  bool find(int start, int left) {
    if (left == 0) {
      return check();
    }
    if (start >= size or start + left > size) {
      return false;
    }
    for (int n = start; n < size; n++) {
      int j = n % col, i = n / col;
      minefield[i][j] = true;
      add_neigh(i, j, 1);
      if (find(n + 1, left - 1)) {
        return true;
      }
      minefield[i][j] = false;
      add_neigh(i, j, -1);
    }
    return false;
  }

  bool check() {
    //debug();
    if (size - mines == 1) {
      one_empty_cell();
      return true;
    }
    // Find a zero.
    bool one_zero = false;
    visit_cell([&](int i, int j) {
      if (not minefield[i][j] and neigh[i][j] == 0) {
        one_zero = true;
        seedi = i;
        seedj = j;
        return true;
      }
      return false;
    });
    if (not one_zero) return false;
    // Grow from the seed.
    grow(seedi, seedj);
    // If all zeros are visited, continue.
    bool zeroes = false;
    visit_cell([&](int i, int j) {
      if (not minefield[i][j] and neigh[i][j] == 0) {
        zeroes = true;
        return true;
      }
      return false;
    });
    // If all limits are reachable, you found a solution.
    if (not zeroes) {      
      bool found = true;
      visit_cell([&](int i, int j) {
        if (minefield[i][j] or neigh[i][j] == -2) {
          return false;
        }
        bool zero_neigh = false;
        visit_neigh(i, j, false, [&](int i, int j, int ii, int jj) {
          if (neigh[ii][jj] == -2) {
            zero_neigh = true;
          }
        });
        if (not zero_neigh) {
          found = false;
          return true;
        }
        return false;
      });
      if (found) return true;
    }
    // Clear visited cells.
    visit_cell([&](int i, int j) {
      if (neigh[i][j] == -2) {
        neigh[i][j] = 0;
      }
      return false;
    });
    return false;
  }

  void grow(int i, int j) {
    neigh[i][j] = -2;
    visit_neigh(i, j, false, [&](int i, int j, int ii, int jj) {
      if (neigh[ii][jj] == 0) {
        grow(ii, jj);
      }
    });
  }

  void one_empty_cell() {
    visit_cell([&](int i, int j) {
      if (!minefield[i][j]) {
        seedi = i;
        seedj = j;
        return true;
      }
      return false;
    });
  }

  template<class T>
  void visit_neigh(int i, int j, bool include_seed, T func) {
    for (int ii = -1; ii <= 1; ii++) {
      for (int jj = -1; jj <= 1; jj++) {
        if (not include_seed and ii == 0 && jj == 0) continue;
        if (i + ii < 0 or j + jj < 0) continue;
        if (i + ii >= row or j + jj >= col) continue;
        func(i, j, i + ii, j + jj);
      }
    }
  }

  template<class T>
  void visit_cell(T func) {
    for (int i = 0; i < row; i++) {
      for (int j = 0; j < col; j++) {
        if (func(i,j)) {
          break;
        }
      }
    }
  }

  void add_neigh(int i, int j, int value) {
    visit_neigh(i, j, true, [&](int i, int j, int ii, int jj) {
      neigh[ii][jj] += value;
    });
  }

  void debug() {
    cout << "--\n";
    for (int i = 0; i < row; i++) {
      for (int j = 0; j < col; j++) {
        if (minefield[i][j]) cout << "*";
        else cout << neigh[i][j];
      }
      cout << "\n";
    }
  }

  void print() {
    for (int i = 0; i < row; i++) {
      for (int j = 0; j < col; j++) {
        if (i == seedi and j == seedj) cout << "c"; 
        else cout << (minefield[i][j] ? "*" : ".");
      }
      cout << "\n";
    }
  }

  int row, col, mines, size;
  vector<vector<bool>> minefield;
  vector<vector<int>> neigh;
  int seedi, seedj;
};

int main() {
  int tot;
  cin >> tot;
  for (int t = 1; t <= tot; t++) {
    int row, col, mines;
    cin >> row >> col >> mines;
    Mine mine(row, col, mines);
    cout << "Case #" << t << ":\n";
    bool sol = mine.search();
    if (sol) {
      mine.print();
    } else {
      cout << "Impossible\n";
    }
  }
  return 0;
}
