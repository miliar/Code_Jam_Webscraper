#include <cstdio>
#include <memory.h>

int main() {
  int nCase;
  scanf("%d", &nCase);
  
  for (int iCase = 0; iCase < nCase; ++iCase) {
    double C, F, X;
    scanf("%lf %lf %lf", &C, &F, &X);

    double sol = -1.0;
    int maxF = static_cast<int>(X / C) + 1;
    double t = 0.0;
    for (int i = 0; i <= maxF; ++i) {
      double cost = t + (X / (2.0 + i * F));
      if (sol < 0.0 || cost < sol) sol = cost;
      t += C / (2.0 + i * F);
    }
    printf("Case #%d: %lf\n", iCase + 1, sol);
  }

  return 0;
}
