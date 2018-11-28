#include <cstdio>
#include <algorithm>

using namespace std;

typedef long double t_d;

const t_d INF = 500 * 1000;
t_d C, F, X;

t_d go(t_d r, t_d m) {
  //  printf("%lf %lf\n", r, m);
  t_d nextFarm = C / r;
  m = min(m, X/r);
  if (nextFarm > m)
    return m;
  return min(m, nextFarm + go(r + F, m - nextFarm));
}

int main() {

  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    scanf("%Lf%Lf%Lf", &C, &F, &X);
    t_d r = 2.0;
    t_d cur = 0;
    t_d m = X / r;
    do {
      t_d nextFarm = C / r;
      m = min(m, X/r);
      if (nextFarm > m)
        break;
      cur += nextFarm;
      r += F;
      m -= nextFarm;
    } while(true);
    printf("Case #%d: %.9Lf\n", t, cur+m);
  }

  return 0;
}
