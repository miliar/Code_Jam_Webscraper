#include <bits/stdc++.h>
using namespace std;

int n;
double v,x;

double vv[10];
double xx[10];

double EPS = 1e-7;

bool eq(double a, double b) {
  return fabs(a-b) < EPS;
}

int main() {
  int t,cs = 0;
  scanf("%d", &t);
  while (t--) {
    ++cs;
    scanf("%d %lf %lf", &n, &v, &x);
    for (int i = 0; i < n; i++) {
      scanf("%lf %lf", &vv[i], &xx[i]);
    }
    printf("Case #%d: ", cs);
    if (n == 1) {
      if (!eq(xx[0], x)) {
        printf("IMPOSSIBLE\n");
      } else {
        printf("%.10lf\n", v/vv[0]);
      }
    } else {
      if (eq(xx[0], x) || eq(xx[1], x)) {
        double res = 1000000000;
        if (eq(xx[0], x)) {
          res = min(res, v/vv[0]);
        }
        if (eq(xx[1], x)) {
          res = min(res, v/vv[1]);
        }
        if (eq(xx[0], x) && eq(xx[1],x)) {
          res = min(res, v/(vv[0] + vv[1]));
        }
        printf("%.10lf\n", res);
      } else if (eq(xx[0], xx[1])) {
        printf("IMPOSSIBLE\n");
      } else {
        double t1 = (v*(x-xx[0]))/(vv[1]*(xx[1]-xx[0]));
        double t2 = (v*(x-xx[1]))/(vv[0]*(xx[0]-xx[1]));
        if (t1 > 0 && t2 > 0) {
          printf("%.10lf\n", max(t1,t2));
        } else {
          printf("IMPOSSIBLE\n");
        }
      }
    }
  }
}
