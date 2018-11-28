#include <cstdio>

using namespace std;

#define EPS 1e-9

int main()
{
  int T, t = 1;
  double cps, c, f, x, t1, t2, tt;

  for (scanf("%d", &T); T; --T) {
    scanf("%lf%lf%lf", &c, &f, &x);
    cps = 2.0;
    tt = 0.0;
    while (1) {
      t1 = x / cps;
      t2 = c / cps + x / (cps + f);
      if (t2 < t1) {
        tt += c / cps;
        cps += f;
      }
      else {
        tt += t1;
        break;
      }
    }
    printf("Case #%d: %0.7lf\n", t++, tt);
  }

  return 0;
}
