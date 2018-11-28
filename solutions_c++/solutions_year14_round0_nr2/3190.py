#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

double C, F, X;
const double DEFAULT_RATE = 2;
const int FARMS_MAX = 100000;
double farming_costs[FARMS_MAX];

double cookie_rate(int num_farms) {
  return num_farms * F + DEFAULT_RATE;
}

void init() {
  cin >> C >> F >> X;

  farming_costs[0] = 0.0;
  for (int i = 1; i < FARMS_MAX; i++) {
    double rate = cookie_rate(i - 1);
    farming_costs[i] = farming_costs[i - 1] + C / rate;
  }
}

void solve_case(int t) {
  init();

  int opt_farms = (int) floor((F * X - DEFAULT_RATE * C) / (C * F));
  opt_farms = max(opt_farms, 0);

  double answer = farming_costs[opt_farms] + X / cookie_rate(opt_farms);
  cout << "Case #" << t << ": " << setprecision(10) << answer << "\n";
}

int main() {
  int T;
  cin >> T;

  for (int i = 0; i < T; i++) {
    solve_case(i + 1);
  }

  return 0;
}
