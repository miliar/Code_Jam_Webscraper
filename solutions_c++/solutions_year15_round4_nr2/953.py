#include "cstdio"
#include "iostream"
#include "cmath"
#include "algorithm"

#define eps 1e-9

using namespace std;

int main() {
  int ntc;

  cin >> ntc;
  for (int tc = 1; tc <= ntc; tc++) {
    int n;
    long double V, X;
    cin >> n >> V >> X;

    long double r1, c1;
    long double r2, c2;

    if ( n == 1 ) {
      cin >> r1 >> c1;
      
      if ( fabs( X - c1 ) < eps ) {
        printf("Case #%d: %.12Lf\n", tc, V / r1);
      } else {
        printf("Case #%d: IMPOSSIBLE\n", tc);
      }
    } else {
      cin >> r1 >> c1;
      cin >> r2 >> c2;

      if ( fabs(c1 - c2) < eps ) {
        if ( fabs( X - c1 ) < eps ) {
          printf("Case #%d: %.12Lf\n", tc, V / (r1 +r2));
        } else {
          printf("Case #%d: IMPOSSIBLE\n", tc);
        }
      } else {
        long double v0 = (V*X - V*c2) / (c1 - c2);

        if ( v0 < 0.0 || v0 > V + eps ) {
          printf("Case #%d: IMPOSSIBLE\n", tc);
        } else {
          long double v1 = V - v0;
          long double t0 = v0/r1;
          long double t1 = v1/r2;

          printf("Case #%d: %.12Lf\n", tc, max(t0, t1));
        }
      }
    }
  }

  return 0;
}
