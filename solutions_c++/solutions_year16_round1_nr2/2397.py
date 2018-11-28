#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Solver {
  Solver(int n_, vector<vector<int>>& input_) 
      : n(n_), input(input_), mat(n, vector<int>(n)), 
        row(n, false), col(n, false), out(n) {
    sort(input.begin(), input.end());
  }
  bool solve() {
    for (int i = 0; i < n; i++) {
      mat[0][i] = input[0][i];
    }
    row[0] = true;
    for (int i = 1; i < n; i++) {
      hidden = i;
      row[i] = true;
      nextrow = row[1] == true ? 2 : 1;
      nextcol = 0;
      nextiter = 1;
      if (iter()) return true;
      row[i]=false;
    }
    for (int i = 0; i < n; i++) {
      hidden = -i-1;
      col[i] = true;
      nextrow = 1;
      nextcol = col[0] == true? 1 : 0;
      nextiter = 1;
      if (iter()) return true;
      col[i]=false;
    }
    return false;
  }

  bool iter() {
    /*cout << nextrow << " " << nextcol << "\n";
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
          cout << mat[i][j] << " ";
      }
      cout << "\n";
    }
    cout << "\n";*/
    if (nextrow >= n && nextcol >= n) {
      if (hidden > 0) {
        for (int i = 0; i < n; i++) {
          out[i] = mat[hidden][i];
        }
      } else {
        for (int i = 0; i < n; i++) {
          out[i] = mat[i][-hidden-1];
        }
      }
      return true;
    }
    if (nextrow < n && validrow()) {
      int saverow = nextrow;
      row[nextrow] = true;
      vector<int> save(n);
      for (int i = 0; i< n; i++) {
        save[i] = mat[nextrow][i];
        mat[nextrow][i] = input[nextiter][i];
      }
      nextiter++;
      nextrow++;
      if (nextrow < n && row[nextrow]) nextrow++;
      if (iter()) {
        return true;
      }
      nextrow = saverow;
      for (int i = 0; i< n; i++) {
        mat[nextrow][i] = save[i];
      }
      row[nextrow] = false;
      nextiter--;
    }
    if (nextcol < n && validcol()) {
      int savecol = nextcol;
      col[nextcol] = true;
      vector<int> save(n);
      for (int i = 0; i< n; i++) {
        save[i] = mat[i][nextcol];
        mat[i][nextcol] = input[nextiter][i];
      }
      nextiter++;
      nextcol++;
      if (nextcol < n && col[nextcol]) nextcol++;
      if (iter()) {
        return true;
      }
      nextcol = savecol;
      for (int i = 0; i< n; i++) {
        mat[i][nextcol] = save[i];
      }
      col[nextcol] = false;
      nextiter--;
    }
    return false;
  }

  bool validcol() {
    for (int i = 0; i < n; i++) {
      if (mat[i][nextcol] > 0 && input[nextiter][i] != mat[i][nextcol]) {
        return false;
      }
    }
    return true;
  }

  bool validrow() {
    for (int i = 0; i < n; i++) {
      if (mat[nextrow][i] > 0 && input[nextiter][i] != mat[nextrow][i]) {
        return false;
      }
    }
    return true;
  }

  int n;
  int nextrow, nextcol, nextiter;
  vector<bool> row,col;
  vector<vector<int>>& input;
  vector<vector<int>> mat;
  vector<int> out;
  int hidden;
};

int main() {
  int tot;
  cin >> tot;
  for (int t = 0; t < tot; t++) {
    int n;
    cin >> n;
    vector<vector<int>> input(2*n-1, vector<int>(n));
    for (int i = 0; i < 2*n-1; i++) {
      for (int j = 0; j < n; j++) {
        cin >> input[i][j];
      }
    }
    Solver s(n, input);
    s.solve();
    /*cout << s.hidden << "\n";*/
    cout << "Case #" << (t+1) << ": ";
      for (int j = 0; j < n; j++) {
        cout << s.out[j] << " ";
      }
      cout << "\n";
  }
  return 0;
}
