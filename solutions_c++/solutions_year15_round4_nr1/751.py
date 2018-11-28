#include <cstdio>
#include <iostream>
#include <cstring>
#include <set>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

int dy[] = { 0, 1, 0, -1};
int dx[] = {-1, 0, 1,  0};
char m[111][111];
map<char, int> d;
int r, c;

int good(int i, int j, int dir) {
  while (true) {
    i += dx[dir];
    j += dy[dir];
    if (i >= r || i < 0 || j >= c || j < 0) return false;
    if (m[i][j] != '.') return true;
  }
}

int main() {
  d['^'] = 0;
  d['>'] = 1;
  d['v'] = 2;
  d['<'] = 3;

  int t;
  cin >> t;
  for (int tt = 1; tt <= t; ++tt) {
    cin >> r >> c;
    for (int i = 0; i < r; ++i) scanf("%s", m[i]);

    int res = 0;

    for (int i = 0; i < r; ++i)
      for (int j = 0; j < c; ++j) {
        if (m[i][j] == '.') continue;
        if (good(i, j, d[m[i][j]])) continue;
        if (good(i, j, 0) || good(i, j, 1) || good(i, j, 2) || good(i, j, 3)) {
          ++res;
        } else {
          cout << "Case #" << tt << ": IMPOSSIBLE" << endl;
          goto next;
        }
      }

    cout << "Case #" << tt << ": " << res << endl;
    next: ;
  }
}
