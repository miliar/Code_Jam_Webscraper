#include <bits/stdc++.h>
using namespace std;

const double inf = 1e10;
const double eps = 1e-8;

bool equals(double a, double b) {
  return abs(a-b) < eps;
}

int main() {
  int Tc;
  cin >> Tc;
  for(int tc = 0; tc < Tc; ++tc) {
    double C, F, X;
    cin >> C >> F >> X;
    double now = 0.0;
    double ans = inf;
    double cookie_par_second = 2.0;
    while(!equals(X/cookie_par_second, 0.0) && ans > now) {
      ans = min(ans, now + X/cookie_par_second);
      now += C/cookie_par_second;
      cookie_par_second += F;
    }
    printf("Case #%d: %.7f\n", tc+1, ans);
  }
  return 0;
}
