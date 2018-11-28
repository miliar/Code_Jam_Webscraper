#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <math.h>
#include <queue>

using namespace std;

int n, m;
int a[105][105];
bool vis[105][105];

bool checkCol(int c) {
    bool ok = 1;
    for (int i = 0; i < n; ++i) {
        ok &= a[i][c] == 1;
    }
    return ok;
}

bool checkRow(int r) {
    bool ok = 1;
    for (int i = 0; i < m; ++i) {
        ok &= a[r][i] == 1;
    }
    return ok;
}

int main() {
    freopen("B-small-attempt0.IN", "r", stdin);
    freopen("sol.txt", "w", stdout);

    int T;
    scanf("%d", &T);

    for (int t = 1; t <= T; ++t) {
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j)
                scanf("%d", &a[i][j]);
        }

        bool ok = 1;
        memset(vis, 0, sizeof(vis));

        for (int i = 0; i < m; ++i) {
            if (a[0][i] == 1) {
               bool can = checkCol(i);
               if (can) {
                  for (int j = 0; j < n; ++j)
                      vis[j][i] = 1;
               }
            }
        }

        for (int i = 0; i < n; ++i) {
            if (a[i][0] == 1) {
                bool can = checkRow(i);
                if (can) {
                    for (int j = 0; j < m; ++j)
                        vis[i][j] = 1;
                }
            }
        }

        for (int i = 0; i < n; ++i)
          for (int j = 0; j < m; ++j) {
              if (a[i][j] == 1 && vis[i][j] == 0)
                  ok = 0;
          }

        printf("Case #%d: %s\n", t, ok ? "YES" : "NO");
    }

    return 0;
}
