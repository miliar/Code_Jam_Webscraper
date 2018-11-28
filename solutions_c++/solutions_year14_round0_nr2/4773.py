#include <iostream>
#include <cstdio>
#include <cfloat>
#include <algorithm>
#include <cmath>

using namespace std;

double cost_per_farm, rate_gain_per_farm, target_cookies;
const double epsilon = 1e-7;

double solve(int nfarms) {
  double time = 0;
  double current_rate = 2.0;
  for(int i = 0; i < nfarms; ++i) {
    time += (cost_per_farm / current_rate);
    current_rate += rate_gain_per_farm;
  }
  time += (target_cookies / current_rate);
  return time;
}

bool equalDouble(double a, double b) {
    return fabs(a - b) < epsilon;
}

double binary_search() {
   int lo = 0;
   int hi = (int) ceil(target_cookies);
   while(lo < hi) {
      int mid = lo + (hi - lo)/2;
      double x1 = solve(mid);
      double x2 = solve(hi);
      if (x1 < x2)
         hi = mid;
      else
         lo = mid + 1;
   }
   return solve(lo);
}

int main() {
  int TC;
  cin >> TC;
  for(int tc = 1; tc <= TC; ++tc) {
    cin >> cost_per_farm >> rate_gain_per_farm >> target_cookies;
    //double ans = binary_search();
    double ans = DBL_MAX;
    for(int i = 0; i <= ceil(target_cookies); ++i)
      ans = min(ans, solve(i));
    printf("Case #%d: %lf\n", tc, ans);
  }
  return 0;
}
