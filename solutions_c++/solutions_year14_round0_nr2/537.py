#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;


int main() {
  int t;
  cin >> t;
  
  for(int zz = 1; zz <= t; zz++) {
    long double result = 100000000;
    long double income = 2.0;
    long double factoryCost, factoryProfit, goal, elapsedTime;
    
    cin >> factoryCost >> factoryProfit >> goal;
    elapsedTime = 0.0;
    
    for(int i = 0; i < 1000000; i++) {
      result = min(result, elapsedTime + goal/income); // don't build anymore factories
      elapsedTime += factoryCost/income;
      income += factoryProfit;
    }

    printf("Case #%d: %.10Lf\n", zz, result);
  }

  return 0;
}
