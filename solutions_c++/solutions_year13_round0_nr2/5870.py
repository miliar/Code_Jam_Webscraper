#include <cstdio>
using namespace std;

const int maxn = 100 + 10;

int n, m, tcase, a[maxn][maxn];

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  scanf("%d", &tcase);
  for (int t = 1; t <= tcase; ++t) {
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < m; ++j)
        scanf("%d", &a[i][j]);
    bool no_sol = false;
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < m; ++j) {
        if (no_sol) break;
        bool larger = false;
        for (int k = 0; k < n; ++k)
          if (a[k][j] > a[i][j]) {
            larger = true;
            break;
          }
        if (!larger) continue;
        for (int k = 0; k < m; ++k)
          if (a[i][k] > a[i][j]) {
            no_sol = true;
            break;
          }
      }
    if (no_sol) printf("Case #%d: NO\n", t);
    else printf("Case #%d: YES\n", t);
  }
  return 0;
}
