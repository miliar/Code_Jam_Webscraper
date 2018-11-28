#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>

double solve(double C, double F, double X) {
  double proportion = 2.f;
  double time = 0.f;
  double result = X / proportion;

  while (time < result) {
    time += C / proportion;
    proportion += F;

    double tmp = time + X / proportion;
    if (result > tmp) {
      result = tmp;
    }
  }
  return result;
}

int main(void) {
  int64_t T;
  std::cin >> T;
  for (int64_t t = 0; t < T; ++t) {
    double C, F, X;
    std::cin >> C >> F >> X;
#if DEBUG
    std::cout << "C: " << C << ", F: " << F << ", X: " << X << std::endl;
#endif
    std::cout << "Case #" << std::fixed << t + 1 << ": ";
    std::cout << std::setprecision(7) << solve(C, F, X) << std::endl;
  }
  return EXIT_SUCCESS;
}

