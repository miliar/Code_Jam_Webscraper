#include <cstdio>

int main()
{
  int T;
  scanf("%d", &T);

  for (int Ti = 1; Ti <= T; Ti++) {

    double C, F, X;
    scanf("%lf %lf %lf", &C, &F, &X);

    double R = 2;
    double t = 0;
    while (1) {
      double t1 = X / R;
      double t2 = C / R + X/ (R + F);

      if (t1 <= t2) {
        t += t1; break;
      } else {
        t += C / R;
        R += F;
      }
    }

    printf("Case #%d: %.7lf\n", Ti, t);
  }

  return 0;
}
