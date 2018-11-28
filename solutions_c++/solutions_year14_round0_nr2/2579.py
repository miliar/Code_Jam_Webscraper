#include <cstdio>
#include <algorithm>
#include <cassert>

#define DEBUG 0

using namespace std;


static double C, F, X;
static int i;
static double total_time;

void solve(double c_per_sec, double currentTime) {
  double fac_time = C / c_per_sec;
  double time = X / c_per_sec;

  if (currentTime + time < total_time) {
    total_time = currentTime + time;
  }
  if (time <= fac_time) {
    return;
  }
  if (currentTime + time < X && currentTime + fac_time < total_time) {
    solve(c_per_sec + F, currentTime + fac_time);
  }
}

int main()
{
  int count;
  scanf("%d", &count);

  for (i = 1; i <= count; i++) {
    double time = 0;
    double c_per_sec = 2.0;
    int cookies = 0;

    scanf("%lf %lf %lf", &C, &F, &X);
    total_time = X / c_per_sec;
#if DEBUG
    printf("  Case #%d %lf %lf %lf\n", i, C, F, X);
#endif
    solve(c_per_sec, 0);
    printf("Case #%d: %.7lf\n", i, total_time);
  }
}
