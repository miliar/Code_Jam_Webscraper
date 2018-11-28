#include <cstdio>
using namespace std;

double f, x, c;
int main() {
  int Case;
  scanf("%d", &Case);
  for (int ca = 1; ca <= Case; ++ ca) {
    scanf("%lf%lf%lf", &c, &f, &x);
    double t = 0;
    double v = 2;
    double ans = x / v;
    do {
      t += c / v;
      v += f;
      if (t + x / v < ans) {
        ans = t + x / v;
      } else {
        break;
      }
      //printf("%lf %.5lf %.5lf\n", v, c, t);
    } while (true);
    printf("Case #%d: %.7lf\n", ca, ans);

  }
  return 0;
}

