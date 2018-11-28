#include <cstdio>
#include <algorithm>

const int N = 100 + 10;
const int dx[] = {-1, 0, 1, 0}, dy[] = {0, 1, 0, -1};

int n, m, cnt, tot, x[N], y[N], z[N];

char cur[N][N];
int pal[2 * N];

void get(int &x, int &y, int z) {
  while (0 <= x && x < n && 0 <= y && y < m) {
    if (cur[x][y] == '/') {
      if (z == 0)
        z = 1;
      else if (z == 1)
        z = 0;
      else if (z == 2)
        z = 3;
      else
        z = 2;
    } else {
      if (z == 0)
        z = 3;
      else if (z == 1)
        z = 2;
      else if (z == 2)
        z = 1;
      else
        z = 0;
    }
    x += dx[z], y += dy[z];
  }
}

bool check() {
  for (int i = 1; i <= tot; i += 2) {
    int a = x[pal[i]], b = y[pal[i]];
    get(a, b, z[pal[i]]);
    int u = x[pal[i + 1]], v = y[pal[i + 1]], w = z[pal[i + 1]];
    if (!(a == u - dx[w] && b == v - dy[w])) return false;
  }
  return true;
}

int main() {
  int tcase;
  scanf("%d", &tcase);
  for (int tid = 1; tid <= tcase; ++tid) {
    scanf("%d%d", &n, &m);
    tot = 0;
    for (int i = 0; i < m; ++i) x[++tot] = 0, y[tot] = i, z[tot] = 2;
    for (int i = 0; i < n; ++i) x[++tot] = i, y[tot] = m - 1, z[tot] = 3;
    for (int i = m - 1; i >= 0; --i) x[++tot] = n - 1, y[tot] = i, z[tot] = 0;
    for (int i = n - 1; i >= 0; --i) x[++tot] = i, y[tot] = 0, z[tot] = 1;
    for (int i = 1; i <= tot; ++i) scanf("%d", &pal[i]);
    cnt = n * m;
    printf("Case #%d:\n", tid);
    for (int s = 0; s < (1 << cnt); ++s) {
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
          if (s >> (i * m + j) & 1) cur[i][j] = '/'; else cur[i][j] = '\\';
        }
        cur[i][m] = '\0';
      }
      if (check()) {
        for (int i = 0; i < n; ++i) puts(cur[i]);
        goto success;
      }
    }
    puts("IMPOSSIBLE");
 success:
    continue;
  }
  return 0;
}
