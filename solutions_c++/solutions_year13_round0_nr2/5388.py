#include <iostream>
#include <cstdio>
#include <set>
#include <vector>

using namespace std;

const int MAXN = 105;
int a[MAXN][MAXN];
int b[MAXN][MAXN];

int main() {
  freopen("B-small-attempt0.in", "r", stdin);
  freopen("B-small-attempt0.out", "w", stdout);
  int t, cas = 1;
  int n, m;

  scanf("%d", &t);
  while (t--) {
    printf("Case #%d: ", cas++);

    scanf("%d%d", &n, &m);
    int mi = 105;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        scanf("%d", &a[i][j]);
        b[i][j] = 0;
        mi = min(mi, a[i][j]);
      }
    }
    if (n == 1 || m == 1) {
      puts("YES");
      continue;
    }
    int tot = 0;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        tot += mi == a[i][j];
        if (a[i][j] == mi) {
          bool flag = true;
          for (int k = 0; k < n && flag; ++k) {
            flag = mi == a[k][j];
          }
          if (flag) {
            for (int k = 0; k < n && flag; ++k) {
              b[k][j] = true;
            }
          }

          flag = true;
          for (int k = 0; k < m && flag; ++k) {
            flag = mi == a[i][k];
          }
          if (flag) {
            for (int k = 0; k < m && flag; ++k) {
              b[i][k] = true;
            }
          }
        }
      }
    }
    int cnt = 0;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        cnt += b[i][j];
      }
    }
    puts(tot == cnt ? "YES" : "NO");

  }
  return 0;
}
