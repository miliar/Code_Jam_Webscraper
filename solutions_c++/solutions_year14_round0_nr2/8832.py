#include <cstdio>
#include <limits>

using namespace std;

double solve(double c, double f, double x) {
  double best = numeric_limits<double>::max();
  double used = 0;
  double rate = 2;
  while (used < best) {
    double act = used + x/rate;
    if (best > act) best = act;

    used += c/rate;
    rate += f;
  }
  return best;
}

int main() {
  int tt;
  double c,f,x;
  scanf("%d", &tt);
  for (int t = 1; t <= tt; t++) {
    scanf("%lf %lf %lf", &c, &f, &x);
    printf("Case #%d: %0.7lf\n", t, solve(c, f, x));
  }
  return 0;
}
