#include <cstdio>

using namespace std;

int main()
{
  int T, counter = 0;
  double C, F, X;

  scanf("%d", &T);
  while (T--) {
    double P = 2.0, time = 0.0;
    scanf("%lf%lf%lf", &C, &F, &X);
    while ((X - C) / P > X / (P + F)) {
      time += C / P;
      P += F;
    }
    time += X / P;
    printf("Case #%d: %.7f\n", ++counter, time);
  }

  return 0;
}
