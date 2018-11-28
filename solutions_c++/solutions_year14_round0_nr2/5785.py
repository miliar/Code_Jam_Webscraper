#include <cstdio>

const int MAXF = 100100;
const double inf = 1E100;

int T;
double C, F, X;


int main() {
  scanf("%d", &T);
  for(int t = 1; t <= T; ++t) {
    printf("Case #%d: ", t);
    scanf("%lf %lf %lf", &C, &F, &X);
    double curtime = 0;
    double curcook = 0;
    double ans = inf;
    double currate = 2;
    for(int f = 0; f <= MAXF; ++f) {
      double rem = X - curcook;
      double cand = curtime + rem / currate;
      if (cand < ans) {
        ans = cand;
        //printf("f = %d, ans = %lf\n", f, ans);
      }
      if (curcook < C) {
        double need = C - curcook;
        curtime += need / currate;
        curcook += need;
      }
      curcook -= C;
      currate += F;
    }

    printf("%.10lf\n", ans);
  }
  return 0;
}

