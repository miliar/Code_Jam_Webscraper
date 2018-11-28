#include <cstdio>
#include <iostream>
#include <cstring>
#include <set>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

#define EPS 1e-9

long double abs(long double a) {
  if (a < 0) return -a;
  return a;
}

long double best(long double a, long double b) {
  if (a < -1) return b;
  if (b < -1) return a;
  return min(a, b);
}

int main() {
  int t;
  cin >> t;
  for (int tt = 1; tt <= t; ++tt) {
    int n;
    long double v, x;
    cin >> n >> v >> x;
    long double vv[111], xx[111];
    for (int i = 0; i < n; ++i) cin >> vv[i] >> xx[i];

    long double res = -2;

    if (n == 1) {
      if (abs(xx[0] - x) < EPS) res = v/vv[0];
    }

    if (n == 2) {
      if (abs(xx[1] - x) < EPS && abs(xx[0] - x) < EPS) {
        long double r = vv[0] + vv[1];
        res = best(res, v/r);
      }
      else if (abs(xx[0] - x) < EPS) res = best(res, v/vv[0]);
      else if (abs(xx[1] - x) < EPS) res = best(res, v/vv[1]);
      else if ((xx[0]-EPS < x && xx[1]+EPS > x) || (xx[0]+EPS > x && xx[1]-EPS < x)) {
        long double v1 = (x*v - v*xx[1])/(xx[0] - xx[1]);
        long double v2 = v - v1;
        long double t1 = v1/vv[0];
        long double t2 = v2/vv[1];
        res = best(res, max(t1, t2));
      }
    }

    if (res < -1) printf("Case #%d: IMPOSSIBLE\n", tt);
    else printf("Case #%d: %.9Lf\n", tt, res);
  }
}
