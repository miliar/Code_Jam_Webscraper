#include <cstdio>
#include <algorithm>

using namespace std;

double C, F, X;

double recursion (double cps) {
  double seconds_to_farm = C / cps;
  double seconds_to_win = X / cps;

  double seconds_to_win_after_farm = seconds_to_farm + X / (cps + F);

  if (seconds_to_win < seconds_to_win_after_farm) return seconds_to_win;

  return min(seconds_to_farm + recursion(cps + F), seconds_to_win);
}

int main(int argc, char *argv[]) {
  int T;

  scanf("%d", &T);

  for (int idx = 1; idx <= T; idx++) {
    scanf("%lf %lf %lf", &C, &F, &X);
    
    printf("Case #%d: %.7f\n", idx, recursion(2));
  }

  return 0;
}
