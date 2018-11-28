#include <cstdio>

using namespace std;

void solve_case(int case_idx) {
  double C, F, X;
  scanf("%lf %lf %lf", &C, &F, &X);

  double V = 2.0;
  double T = 0.0;
  bool keep_producing = true;
  while (keep_producing) {
    double simple_time = X / V;
    double before_next_farm_time = C / V;
    double next_V = V + F;
    double farm_time = before_next_farm_time + (X / next_V);

    if (farm_time < simple_time) {
      T += before_next_farm_time;
      V = next_V;
    } else {
      T += simple_time;
      keep_producing = false;
    }
  }

  printf("Case #%d: %0.7lf\n", case_idx, T);
}

int main() {
  int tests;
  scanf("%d", &tests);
  for (int t = 1; t <= tests; ++t) {
    solve_case(t);
  }
  
  return 0;
}
