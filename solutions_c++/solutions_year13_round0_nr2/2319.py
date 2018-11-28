#include <iostream>

using namespace std;

int height[500][500];

int main() {
  int t; cin >> t;
  for (int test = 1; test <= t; ++test) {
    cout << "Case #" << test << ": ";
    int n, m; cin >> n >> m;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        cin >> height[i][j];
      }
    }

    bool done = false;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        bool found = false;

        bool okay = true;
        for (int ii = 0; ii < n; ++ii) {
          if (height[ii][j] > height[i][j]) {
            okay = false; break;
          }
        }
        if (okay) found = true;

        okay = true;
        for (int jj = 0; jj < m; ++jj) {
          if (height[i][jj] > height[i][j]) {
            okay = false; break;
          }
        }
        if (okay) found = true;

        if (!found) {
          cout << "NO" << endl;
          done = true;
          break;
        }
      }
      if (done) break;
    }
    if (done) continue;
    cout << "YES" << endl;
  }
  return 0;
}