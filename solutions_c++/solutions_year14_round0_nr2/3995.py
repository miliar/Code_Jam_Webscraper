#include <iostream>
#include <iomanip>
#include <cmath>

double solve(const double C, const double F, const double X) {
  double t = 0;
  double s = 2;
  
  while ( (s+F)*X > (s+F)*C + s*X ) {
    t += C/s;
    s += F;
  }
  
  return t + X/s;
}

int main() {
  
  int num_tests;
  std::cin >> num_tests;

  std::cout.precision(7);
  std::cout << std::fixed;
  for ( int t = 1; t <= num_tests; ++t ) {
    double C, F, X;
    std::cin >> C >> F >> X;

    std::cout << "Case #" << t << ": " << solve(C, F, X) << "\n";
  }

  return 0;
}
