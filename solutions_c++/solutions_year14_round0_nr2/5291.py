#include <cstdio>
#include <cmath>
#include <vector>
using namespace std;

double C, F, X;

int main() {
  int T;
  scanf("%d", &T);
  for (int tc = 1; tc <= T; tc++) {
    scanf("%lf%lf%lf", &C, &F, &X);
    double best = X/2;

    double speed = 2;
    double now = 0;
    for (int buy = 1; buy <= X; buy++) {
      now += C/speed;
      speed += F;
      best = min(best, now + X/speed);
    }

    printf("Case #%d: %.9lf\n", tc, best);
  }
}
