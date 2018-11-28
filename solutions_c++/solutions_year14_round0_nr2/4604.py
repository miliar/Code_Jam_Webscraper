#include <cstdio>
#include <cmath>
#include <algorithm>

int main() {
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    double C, F, X;
    scanf("%lf %lf %lf", &C, &F, &X);
    double rate = 2.0;
    double ti = 0.0;
    double min = 100000000.0;
    for (int i = 0; i <= 50005; ++i) {
      min = std::min(min, ti + (X / rate));
      ti += C / rate;
      rate += F;
    }
    printf("Case #%d: %.7lf\n", t, min);
  }
}
