#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

char double_cmp(double a, double b) {
  if (fabs(a - b) < 1e-10) return 0;
  if (a - b < 1e-10) return -1;
  return 1;
}

int main() {
  int T;
  scanf("%d", &T);

  for (int test = 1; test <= T; test++) {
    double C, F, X;
    scanf("%lf%lf%lf", &C, &F, &X);
    double speed = 2.0;
    double res = X/speed;
    double additional_time = 0;

    while (true) {
      double new_speed = speed + F;
      double curr = additional_time + C/speed + X/new_speed;
      if (double_cmp(curr, res) < 0) {
        res = curr;
        additional_time += C/speed;
        speed = new_speed;
      } else {
        break;
      }
    }

    printf("Case #%d: %.7lf\n", test, res);
  }
}
