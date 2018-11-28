#include <numeric>
#include <set>
#include <iostream>

using std::begin;
using std::end;

constexpr double INITIAL_CPS = 2.0;

constexpr double cps(int nFarms, double nFarmProduction) { return nFarms * nFarmProduction + INITIAL_CPS; }

double calculate_best_time(double nFarmCost, double nFarmProduction, double nTargetCookies) {
  std::multiset<double> times;
  int nFarms = 0;

  while (true) {
    auto timeToFarm = nFarmCost / cps(nFarms, nFarmProduction);
    auto timeToTargetWithFarm = timeToFarm + nTargetCookies / cps(nFarms+1, nFarmProduction);
    auto timeToTarget = nTargetCookies / cps(nFarms, nFarmProduction);
    if (timeToTargetWithFarm < timeToTarget) {
      times.insert(timeToFarm);
      ++nFarms;
    } else {
      times.insert(timeToTarget);
      return std::accumulate(begin(times), end(times), 0.0);
    }
  }
}

int main(int argc, char** argv) {
  size_t nCases;
  std::cin >> nCases;
  std::cout.precision(12);
  for (auto i=0u; i<nCases; ++i) {
    double nFarmCost, nFarmProduction, nTargetCookies;
    std::cin >> nFarmCost >> nFarmProduction >> nTargetCookies;
    std::cout << "Case #" << (i+1) << ": ";
    std::cout << calculate_best_time(nFarmCost, nFarmProduction, nTargetCookies) << std::endl;
  }
}
