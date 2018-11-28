#include <cstdio>
#pragma warning(disable : 4996)

using namespace std;

int main(void) {
  int T;
  scanf("%d", &T);
  for (int case_n = 1; case_n <= T; case_n++) {
    double C, F, X;
    scanf("%lf%lf%lf", &C, &F, &X);
    double productivity = 2.0;
    double best_time = X / productivity;
    double current_time = 0;
    for (;;) {
      current_time += C / productivity;
      productivity += F;
      double try_time = current_time + X / productivity;
      if (try_time < best_time) {
        best_time = try_time;
      }
      else {
        break;
      }
    }
    printf("Case #%d: %.7f\n", case_n, best_time);
  }
}