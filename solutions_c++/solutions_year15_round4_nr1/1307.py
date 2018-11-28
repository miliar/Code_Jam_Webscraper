#include <iostream>
#include <cstdlib>
using namespace std;

int R, C;
string grid[110];
int next[10100];
string dirs = "^>v<";

int getNext(int x, int y) {
  int dx = 0, dy = 0;
  if (grid[x][y] == '^') dx = -1;
  else if (grid[x][y] == '>') dy = 1;
  else if (grid[x][y] == 'v') dx = 1;
  else if (grid[x][y] == '<') dy = -1;

  x += dx; y += dy;
  while (x >= 0 && x < R && y >= 0 && y < C && grid[x][y] == '.') {
    x += dx;
    y += dy;
  }
  if (x < 0 || x >= R || y < 0 || y >= C) return -1;
  return x * R + y;
}

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    cin >> R >> C;
    for (int i = 0; i < R; i++) cin >> grid[i];
    for (int i = 0; i < R; i++)
      for (int j = 0; j < C; j++)
        if (grid[i][j] != '.') {
          next[i * C + j] = getNext(i, j);
          // cout << i << " " << j << " " << next[i * C + j] << endl;
        }

    int res = 0;
    bool imp = false;
    for (int i = 0; i < R; i++)
      for (int j = 0; j < C; j++)
        if (grid[i][j] != '.' && next[i * C + j] == -1) {
          for (int d = 0; d < dirs.size(); d++) {
            grid[i][j] = dirs[d];
            int n = getNext(i, j);
            if (n != -1) next[i * C + j] = n;
          }
          if (next[i * C + j] == -1) imp = true;
          else res++;
        }

    cout << "Case #" << c << ": ";
    if (imp) cout << "IMPOSSIBLE";
    else cout << res;
    cout << endl;
  }
  return 0;
}
