#include <cstdio>

int n, m;
int a[150][150];

bool f() {
  for (int k = 1; k <= 100; ++k) {
    for (int i = 0; i < n; ++i) {
      bool row = 1;
      for (int j = 0; j < m; ++j) {
        row &= (a[i][j] == k || a[i][j] == -1);
      }
      if (row) for (int j = 0; j < m; ++j) a[i][j] = -1;
    }
    for (int j = 0; j < m; ++j) {
      bool col = 1;
      for (int i = 0; i < n; ++i) {
        col &= (a[i][j] == k || a[i][j] == -1);
      }
      if (col) for (int i = 0; i < n; ++i) a[i][j] = -1;
    }
  }
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      if (a[i][j] != -1) return 0;
    }
  }
  return 1;
}


int main() {
  int cas = 0;
  int T; scanf("%d", &T);
  while (T--) {
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        scanf("%d", &a[i][j]);
      }
    }
    printf("Case #%d: ", ++cas);
    if (f()) puts("YES"); else puts("NO");
  }
}
