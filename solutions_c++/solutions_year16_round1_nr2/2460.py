#include <bits/stdc++.h>

using namespace std;

int n;

struct List {
  int a[55];
  void read() {
    for (int i = 0; i < n; i ++) {
      scanf("%d", a + i);
    }
  }
} b[110];

int r[55], c[55], ans[55], A[55][55];
bool vis[110];

bool xiao(int x, int y) {
  for (int i = 0; i < n; i ++) {
    if (b[x].a[i] >= b[y].a[i]) return 0;
  }
  return 1;
}

void init() {
  for (int i = 0; i < n; i ++) {
    for (int j = 0; j < n; j ++) {
      A[i][j] = b[r[i]].a[j];
    }
  }
}

bool can() {
  for (int i = 0; i < n; i ++) {
    for (int j = 1; j < n; j ++) {
      if (A[i][j] <= A[i][j - 1]) return 0;
      if (A[j][i] <= A[j - 1][i]) return 0;
    }
  }
  return 1;
}

void dfs(int p) {
  if (p == n) {
    int flag = 0;
    init();
    if (!can) return;
    memset(c, 0xff, sizeof c);
    for (int i = 0; i < 2 * n - 1; i ++) {
      if (vis[i]) continue;
      int fd = 0;
      for (int j = 0; j < n; j ++) {
        if (~ c[j]) continue;
        int ok = 1;
        for (int k = 0; k < n; k ++) {
          if (A[k][j] != b[i].a[k]) {
            ok = 0; break;
          }
        }
        if (ok) {
          c[j] = i;
          fd = 1;
          break;
        }
      }
      if (!fd) return;
    }
    int p;
    for (int i = 0; i < n; i ++) {
      if (c[i] == -1) p = i;
    }
    for (int i = 0; i < n; i ++) {
      ans[i] = b[r[i]].a[p];
    }
    return;
  }
  for (int i = 0; i < 2 * n - 1; i ++) {
    if (vis[i]) continue;
    if (p && !xiao(r[p - 1], i)) continue;
    vis[i] = 1;
    r[p] = i;
    dfs(p + 1);
    vis[i] = 0;
  }
}

int main() {
  freopen("B-small-attempt2.in", "r", stdin);
  freopen("B-small-attempt2.out", "w", stdout);
  int T, cas = 0;
  scanf("%d", &T);
  while (T --) {
    scanf("%d", &n);
    for (int i = 0; i < 2 * n - 1; i ++) {
      b[i].read();
    }
    memset(vis, 0, sizeof vis);
    dfs(0);
    printf("Case #%d:", ++ cas);
    for (int i = 0; i < n; i ++) {
      printf(" %d", ans[i]);
    }
    puts("");
  }
  return 0;
}