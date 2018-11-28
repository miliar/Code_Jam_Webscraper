#include <iostream>
using namespace std;
int main() {
  int tc;
  scanf("%d", &tc);
  for (int cas = 1; cas <= tc; ++cas) {
    double c, f, x;
    scanf("%lf%lf%lf", &c, &f, &x);
    double ans = x / 2.0;
    double cur_p = 2.0;
    double cur_t = 0;
    while (true) {
      cur_t += c / cur_p;
      cur_p += f;
      double tmp = cur_t + x / cur_p;
      if (tmp > ans) {
        break;
      }
      ans = tmp;
    }
    printf("Case #%d: %.12lf\n", cas, ans);
  }
  return 0;
}
