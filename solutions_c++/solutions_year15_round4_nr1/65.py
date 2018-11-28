#include <bits/stdc++.h>

using namespace std;

void solve() {
  int r, c;
  cin >> r >> c;
  string s[r];
  for (int i = 0; i < r; ++i) cin >> s[i];
  int res = 0;
  for (int i = 0; i < r; ++i) {
    for (int j = 0; j < c; ++j) {
      if (s[i][j] == '.') continue;
      int cnt = 0;
      for (int k = 0; k < r; ++k) {
        if (s[k][j] != '.') ++cnt;
      }
      for (int k = 0; k < c; ++k) {
        if (s[i][k] != '.') ++cnt;
      }
      if (cnt == 2) {
        cout << "IMPOSSIBLE";
        return;
      }
      if (s[i][j] == '^') {
        bool found = false;
        for (int k = 0; k < i; ++k) {
          if (s[k][j] != '.') found = true;
        }
        if (!found) ++res;
      }
      if (s[i][j] == 'v') {
        bool found = false;
        for (int k = i + 1; k < r; ++k) {
          if (s[k][j] != '.') found = true;
        }
        if (!found) ++res;
      }
      if (s[i][j] == '<') {
        bool found = false;
        for (int k = 0; k < j; ++k) {
          if (s[i][k] != '.') found = true;
        }
        if (!found) ++res;
      }
      if (s[i][j] == '>') {
        bool found = false;
        for (int k = j + 1; k < c; ++k) {
          if (s[i][k] != '.') found = true;
        }
        if (!found) ++res;
      }
    }
  }
  cout << res;
}

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    cout << "Case #" << i + 1 << ": ";
    solve();
    cout << endl;
  }
}
