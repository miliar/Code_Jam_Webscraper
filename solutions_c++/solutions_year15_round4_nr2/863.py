#include <math.h>
#include <stdio.h>

#include <algorithm>


struct Source {
  double temp;
  double rate;
};

int N;
double velo, temp;

Source src[100];

int main() {
  int t, T;
  for (scanf("%d", &T), t = 1; t <= T; ++t) {
    printf("Case #%d: ", t);

    scanf("%d %lf %lf", &N, &velo, &temp);
    for (int n = 0; n < N; ++n) {
      scanf("%lf %lf", &(src[n].rate), &(src[n].temp));
    }

    if (N == 1) {
      if (fabs(src[0].temp - temp) < 1e-9) {
        printf("%.9f\n", velo / src[0].rate);
      } else {
        printf("IMPOSSIBLE\n");
      }
    } else {
      if (src[0].temp > temp + 1e-9 && src[1].temp > temp + 1e-9 ||
          src[0].temp < temp - 1e-9 && src[1].temp < temp - 1e-9) {
        printf("IMPOSSIBLE\n");
      } else {
        if (fabs(src[0].temp - src[1].temp) < 1e-9) {
          printf("%.9f\n", velo / (src[0].rate + src[1].rate));
        } else {
          double ra = fabs(temp - src[0].temp);
          double rb = fabs(temp - src[1].temp);
          double ta = velo * rb / (ra + rb) / src[0].rate;
          double tb = velo * ra / (ra + rb) / src[1].rate;
          printf("%.9f\n", std::max(ta, tb));
        }
      }
    }
  }
  return 0;
}
