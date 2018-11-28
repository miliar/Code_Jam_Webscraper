#include <stdio.h>

int main() {
  int n_inupt;
  scanf("%d", &n_inupt);

  double C, F, X;
  for (int n = 1; n <= n_inupt; ++n) {
    scanf("%lf %lf %lf", &C, &F, &X);
    double min_cost = 1e38, cost = 1e38;
    int n_farm = 0;
    double farm_time = 0;
    do {
      min_cost = cost;
      cost = X / (2 + n_farm * F) + farm_time;
      farm_time += C / (2 + n_farm * F);
      n_farm++;
    } while (cost < min_cost);

    printf("Case #%d: %.7f\n", n, min_cost);
  }
}