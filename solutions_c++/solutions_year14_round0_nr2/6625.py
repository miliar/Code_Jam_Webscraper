#include <stdio.h>
#include <iostream>
using namespace std;

int n;
double c, f, x;
int main () {
  cin >> n;
  for (int t = 1; t <= n; t++) {
    cin >> c >> f >> x;

    double ts = 0;
    double speed = 2;
    double best_ts = 1e123;
    while (ts < best_ts) {
      double proj_ts = x/speed + ts;
      best_ts = min(best_ts, proj_ts);
      // time to get to c
      ts += c/speed;
      // update speed
      speed += f;
    }
    printf("Case #%d: %.7lf\n", t, best_ts);
  }
  return 0;
}
