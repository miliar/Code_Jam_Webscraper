#include <iostream>
#include <string>
#include <cstdio>
#include <cmath>

using namespace std;

double solve(double cost, double rate, double target) {
  // ceil((x/c) - (2.0/f) - 1)
  //cout << "cost: " << cost << " rate: " << rate << " target " << target << endl;
  int n = ceil((target/cost) - (2.0/rate) - 1.0);
  //cout << "n = " << n << endl;
  if (n < 0) n = 0;
  double total = target / (2.0+((double)n*rate));
  //cout << "total = " << total << endl;
  for (int i = n-1; i >= 0; --i) {
    double cur_rate = 2.0 + (double)n*rate;
    total += cost / (2.0+((double)i*rate));
  }
  return total;
}

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    double cost, rate, target;
    cin >> cost >> rate >> target;
    double result = solve(cost, rate, target);
    printf("Case #%d: %.7f\n", i+1, result);
  }
  return 1;
}
