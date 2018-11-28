#include <cstdio>
#include <algorithm>

using namespace std;

using real = long double;

int main() {
  int re;

  scanf("%d", &re);
  for (int ri = 1; ri <= re; ++ri) {
    int n;
    real v, x;
    vector<pair<real, real>> a;

    scanf("%d%Lf%Lf", &n, &v, &x);
    a.resize(n);
    for (int i = 0; i < n; ++i) {
      scanf("%Lf%Lf", &a[i].first, &a[i].second);
    }
/*
    if (ri == 49) {
      fprintf(stderr, "%d %Lf %Lf\n", n, v, x);
      for (int i = 0; i < n; ++i) {
        fprintf(stderr, "%Lf %Lf\n", a[i].first, a[i].second);
      }
    } else {
      continue;
    }
*/
    printf("Case #%d: ", ri);
    if (n == 1) {
      if (a[0].second == x) {
        printf("%.10Lf\n", v / a[0].first);
      } else {
        puts("IMPOSSIBLE");
      }
    } else {
      if (a[0].second == x && a[1].second == x) {
        printf("%.10Lf\n", v / (a[0].first + a[1].first));
      } else if (a[0].second == x) {
        printf("%.10Lf\n", v / a[0].first);
      } else if (a[1].second == x) {
        printf("%.10Lf\n", v / a[1].first);
      } else if ((a[0].second < x && a[1].second < x)
              || (a[0].second > x && a[1].second > x)) {
        puts("IMPOSSIBLE");
      } else {
        real d0 = fabsl(a[0].second - x);
        real d1 = fabsl(a[1].second - x);
        real p0 = d1 / (d0 + d1);
        real p1 = d0 / (d0 + d1);
        real r = min(a[0].first / p0, a[1].first / p1);
        printf("%.10Lf\n", v / r);
      }
    }
  }

  return 0;
}
