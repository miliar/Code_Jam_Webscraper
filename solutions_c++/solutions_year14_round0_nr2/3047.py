#include <stdio.h>

using namespace std;

int main()
{
  int T;

  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);

  scanf("%d", &T);

  for (int cn = 1; cn <= T; cn++) {
    double C, F, X;

    scanf("%lf%lf%lf", &C, &F, &X);

    printf("Case #%d: ", cn);

    double ans = 0;
    double f = 0;
    while (true) {
      if (C / (f + 2) + X / (f + F + 2) < X / (f + 2)) {
        ans += C / (f + 2);
      } else {
        ans += X / (f + 2);
        break;
      }
      f += F;
    }
    printf("%.10f\n", ans);

  }

  return 0;
}