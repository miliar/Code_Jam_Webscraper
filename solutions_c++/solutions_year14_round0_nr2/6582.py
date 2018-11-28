#include <bits/stdc++.h>
using namespace std;
void solve() {
  double c, f, x;
  scanf("%lf%lf%lf", &c, &f, &x);
  double f_t = 0;
  double last = 1e100;
  for (int i = 0; i < 1<<20; i++) {
    double cur = x / (2 + i * f);
    cur += f_t;
    if (cur > last) {
      printf("%.8f\n", last);
      return;
    }
    f_t += c/(2 + i*f);
    last = cur;
  }
}
int main() {
  int t;
  scanf("%d", &t);
  for (int i = 1; i <= t; i++) {
    printf("Case #%d: ", i);
    solve();
  }
  return 0;
}
