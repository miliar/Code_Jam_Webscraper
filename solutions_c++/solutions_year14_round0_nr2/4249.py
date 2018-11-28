#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
  int T;
  scanf("%d", &T);
  for (int tt = 1; tt <= T; ++tt) {
    double c, f, x;
    scanf("%lf%lf%lf", &c, &f, &x);
    double min_time = 1e9;

    double cookies_per_sec = 2;
    double start_time = 0;
    for (int b = 0; b < 1000000; ++b) {
      min_time = min(min_time, start_time + x / cookies_per_sec);
      start_time += c / cookies_per_sec;
      cookies_per_sec += f;
    }
    printf("Case #%d: %.8lf\n", tt, min_time);
  }
  return 0;
}
