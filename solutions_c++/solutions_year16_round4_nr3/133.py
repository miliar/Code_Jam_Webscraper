#include <bits/stdc++.h>
using namespace std;
int n, m;
int a[50];
vector<int> edges[1000];
int id(int x, int y, int z) {
  return x * 400 + y * 20 + z + 100;
}
int dfs(int x, int p) {
  for (int y : edges[x]) {
    if (y == p) continue;
    return dfs(y, x);
  }
  return x;
}
void solve() {
  scanf("%d %d", &n, &m);
  for (int i = 0; i < n + m; i++) {
    int x, y;
    scanf("%d %d", &x, &y);
    a[x] = y;
    a[y] = x;
  }
  int k = (1 << (n * m));
  for (int i = 0; i < k; i++) {
    //printf("%d\n", i);
    for (int j = 0; j < 1000; j++) {
      edges[j].clear();
    }
    int z = 1;
    for (int j = 1; j <= m; j++, z++) {
      edges[z].push_back(id(0, 0, j - 1));
      edges[id(0, 0, j - 1)].push_back(z);
    }
    for (int j = 1; j <= n; j++, z++) {
      edges[z].push_back(id(1, j - 1, m));
      edges[id(1, j - 1, m)].push_back(z);
    }
    for (int j = m; j >= 1; j--, z++) {
      edges[z].push_back(id(0, n, j - 1));
      edges[id(0, n, j - 1)].push_back(z);
    }
    for (int j = n; j >= 1; j--, z++) {
      edges[z].push_back(id(1, j - 1, 0));
      edges[id(1, j - 1, 0)].push_back(z);
    }
    for (int j = 0; j < n; j++) {
      for (int l = 0; l < m; l++) {
        int p, q, r, s;
        p = id(0, j, l);
        q = id(1, j, l + 1);
        r = id(0, j + 1, l);
        s = id(1, j, l);
        if ((i & (1 << (j * m + l))) == 0) {
          edges[p].push_back(s);
          edges[s].push_back(p);
          edges[q].push_back(r);
          edges[r].push_back(q);
        } else {
          edges[p].push_back(q);
          edges[q].push_back(p);
          edges[s].push_back(r);
          edges[r].push_back(s);
        }
      }
    }
    bool ok = true;
    for (int j = 1; ok && j <= (n + m) * 2; j++) {
      int ret = dfs(j, 0);
      //printf("dfs %d is %d\n", j, ret);
      ok &= ret == a[j];
    }
    if (ok) {
      for (int j = 0; j < n; j++) {
        for (int l = 0; l < m; l++) {
          printf((i & (1 << (j * m + l))) == 0 ? "/" : "\\");
        }
        printf("\n");
      }
      return ;
    }
  }
  printf("IMPOSSIBLE\n");
}
int main() {
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    printf("Case #%d:\n", t);
    solve();
  }
  return 0;
}

