#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, -1, 0, 1};
string dir = ">^<v";

bool search(const vector<string>& g, int x, int y, int d) {
  for (;;) {
    x += dx[d]; y += dy[d];
    if (x >= g[0].size() || x < 0) return false;
    if (y >= g.size() || y < 0) return false;
    if (g[y][x] != '.') return true;
  }
}

main() {
  int T, prob=1;
  for (cin >> T; T--;) {
    int X, Y;
    cin >> Y >> X;
    vector<string> g(Y);
    for (int y = 0; y < Y; y++) cin >> g[y];
    int ret = 0;
    for (int y = 0; y < Y; y++)
    for (int x = 0; x < X; x++) {
      int d = dir.find(g[y][x]);
      if (d == -1) continue;
      if (search(g, x, y, d)) continue;
      for (d = 0; d < 4; d++) {
        if (search(g, x, y, d)) break;
      }
      if (d == 4) goto imp;
      ret++;
    }
    cout << "Case #" << prob++ << ": " << ret << endl;
    continue;
imp:
    cout << "Case #" << prob++ << ": IMPOSSIBLE" << endl;
  }
}
