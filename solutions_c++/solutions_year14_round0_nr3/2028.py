#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <ctime>

using namespace std;

int r;
int c;
int m;
int st;
int a[5][5];
int b[5][5];
int was[5][5];

void add(int x, int y, int v) {
  for (int dx = -1; dx <= 1; ++dx)
    for (int dy = -1; dy <= 1; ++dy) if (abs(dx) + abs(dy) != 0) {
      int nx = x + dx;
      int ny = y + dy;
      if (nx >= 0 and nx < r and ny >= 0 and ny < c) a[nx][ny] += v;
    }
}

int get(int x, int y) {
  was[x][y] = st;
  if (a[x][y] != 0) return 1;
  int res = 1;
  for (int dx = -1; dx <= 1; ++dx)
    for (int dy = -1; dy <= 1; ++dy) if (abs(dx) + abs(dy) != 0) {
      int nx = x + dx;
      int ny = y + dy;
      if (nx >= 0 and nx < r and ny >= 0 and ny < c)
        if (was[nx][ny] != st and b[nx][ny] == 0) res += get(nx, ny);
    }
  return res;
}

bool go(int x, int y, int z) {
  if (y > m) return false;
  if (m - y > r * c - x) return false;
  if (x == r * c) {
    if (z == -1 or y != m) return false; ++st;
    if (get(z / c, z % c) == r * c - m) {
      for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
          if (i == z / c and j == z % c) putchar('c'); else
          if (b[i][j] == 1) putchar('*');
          else putchar('.');
        }
        putchar('\n');
      }
      return true;
    }
    return false;
  }
  int i = x / c;
  int j = x % c;
  if (go(x + 1, y, z)) return true;
  if (z == -1)
    if (go(x + 1, y, x)) return true;
  b[i][j] = 1;
  add(i, j, 1);
  if (go(x + 1, y + 1, z)) return true;
  b[i][j] = 0;
  add(i, j, -1);
}

int main() {
  freopen("in", "r", stdin); freopen("out", "w", stdout);
  int tt; scanf("%d", &tt);
  for (int cc = 1; cc <= tt; ++cc) {
    scanf("%d %d %d", &r, &c, &m);
    st = 1;
    for (int i = 0; i < r; ++i)
      for (int j = 0; j < c; ++j) a[i][j] = b[i][j] = was[i][j] = 0;
    printf("Case #%d:\n", cc);
    if (!go(0, 0, -1)) puts("Impossible");
  }
  return 0;
}