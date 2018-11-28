#include <iostream>
#include <vector>

using namespace std;

const int MAX_H = 100;

int main() {
  int t;
  cin >> t;
  for (int ca = 1; t--; ++ca) {
    int n, m;
    cin >> n >> m;
    vector<vector<int> > a(n, vector<int>(m));
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        cin >> a[i][j];
      }
    }
    for (int h = 1; h < MAX_H; ++h) {
      vector<vector<int> > na = a;
      for (int r = 0; r < n; ++r) {
        bool eq = (a[r][0] == h);
        for (int i = 1; i < m && eq; ++i) {
          if (a[r][i] != a[r][0]) eq = false;
        }
        if (eq) {
          for (int i = 0; i < m; ++i) {
            na[r][i] = h+1;
          }
        }
      }
      for (int c = 0; c < m; ++c) {
        bool eq = (a[0][c] == h);
        for (int i = 1; i < n && eq; ++i) {
          if (a[i][c] != a[0][c]) eq = false;
        }
        if (eq) {
          for (int i = 0; i < n; ++i) {
            na[i][c] = h+1;
          }
        }
      }
      swap(a, na);
    }
    bool ok = true;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        if (a[i][j] != MAX_H) ok = false;
      }
    }
    cout << "Case #" << ca << ": ";
    if (ok) cout << "YES" << endl;
    else cout << "NO" << endl;
  }
}
