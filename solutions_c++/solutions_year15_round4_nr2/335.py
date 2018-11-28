#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <numeric>
#include <utility>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

void solve() {
  int n;
  double v, x;
  double r[100], c[100];
  scanf("%d", &n);
  scanf("%lf%lf", &v, &x);
  for (int i = 0; i < n; ++i) {
    scanf("%lf%lf", r + i, c + i);
  }
  if (n > 2) {
    printf("-\n");
    return;
  }
  if (n == 1) {
    if (c[0] == x) {
      printf("%.10lf\n", v / r[0]);
    } else {
      printf("IMPOSSIBLE\n");
    }
    return;
  }
  if ((c[0] > x && c[1] > x) || (c[0] < x && c[1] < x)) {
      printf("IMPOSSIBLE\n");
      return;
  }
  if (c[0] == x && c[1] == x) {
    printf("%.10lf\n", v / (r[0] + r[1]));
    return;
  }
  double t = (x - c[1]) / (c[0] - c[1]);
  double ret = max(v*t / r[0], v*(1-t) / r[1]);
  printf("%.10lf\n", ret);
}

int main() {
  int t;
  scanf("%d", &t);
  for (int tc = 1; tc <= t; ++tc) {
    printf("Case #%d: ", tc);
    solve();
  }
  return 0;
}
