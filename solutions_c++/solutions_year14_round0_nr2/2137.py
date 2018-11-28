#include <cassert>
#include <cstdio>
#include <algorithm>

int main() {
  using std::min;
  int tn;
  assert(scanf("%d", &tn) == 1);
  for (int t = 1; t <= tn; t++) {
    double c, f, x;
    assert(scanf("%lf%lf%lf", &c, &f, &x) == 3);
    double time = 0.0, ans = x / 2.0, rate = 2.0;
    for (int cf = 0; cf <= 100000; cf++) {
      time += c / rate;
      rate += f;
      ans = min(ans, time + x / rate);
    }
    printf("Case #%d: %.20lf\n", t, ans);
  }
  return 0;
}

