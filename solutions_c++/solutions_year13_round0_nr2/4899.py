#include <cstdio>

int a[150][150];
bool work() {
  int n, m;
  scanf("%d%d", &n, &m);

  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      scanf("%d", &a[i][j]);
    }
  }
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      bool ok = true;
      for (int k = 0; k < m && ok; ++k) {
        if (a[i][k] > a[i][j]) ok = false;
      }
      if (ok) continue;
      ok = true;
      for (int k = 0; k < n && ok; ++k) {
        if (a[k][j] > a[i][j]) ok = false;
      }
      if (!ok) return false;
    }
  }
  return true;
}

int main() {
  int t;
  scanf("%d", &t);
  for (int i = 1; i <= t; ++i) {
    printf("Case #%d: %s\n", i, work() ? "YES" : "NO");
  }
}
