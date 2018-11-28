#include <stdio.h>

int main() {
  int T = 0;
  scanf("%d", &T);

  for (int t = 1; t <= T; ++t) {
    double C = 0.0;
    double F = 0.0;
    double X = 0.0;
    scanf("%lf %lf %lf", &C, &F, &X);

    double answer = X / 2.0;
    double current_building_time_sum = 0.0;
    for (int num_of_farms_built = 1; ; ++num_of_farms_built) {
      current_building_time_sum += (C / (2.0 + F * (num_of_farms_built - 1)));
      const double current_answer = current_building_time_sum +
          X / (2.0 + F * num_of_farms_built);
      if (current_building_time_sum > answer) {
        break;
      }
      if (current_answer < answer) {
        answer = current_answer;
      }
    }

    printf("Case #%d: %.7lf\n", t, answer);
  }
  return 0;
}
