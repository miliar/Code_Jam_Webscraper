#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <cstdio>

using namespace std;

double calcGoalTime(double cps, double goalCookies, double currentCookies = 0.0) {
  return (goalCookies - currentCookies) / cps;
}

double calcGetFarmTime(double cps, double farmCost) {
  return farmCost / cps;
}

int main() {
  int totalTc; cin >> totalTc;
  for (int tc = 1; tc <= totalTc; ++tc) {
    double c, f, x;
    cin >> c >> f >> x;
    double currentTime = 0.0;
    double cps = 2.0;
    double ans = 0.0;
    while (true) {
      double goalTime = calcGoalTime(cps, x);
      double getFarmTime = calcGetFarmTime(cps, c);
      double goalTimeAfterGetFarm = getFarmTime + calcGoalTime(cps + f, x);
      if (goalTime < goalTimeAfterGetFarm) {
	ans = goalTime + currentTime; break;
      }
      cps += f;
      currentTime += getFarmTime;
    }
    printf("Case #%d: %.9lf\n", tc, ans);
  }
  return 0;
}
