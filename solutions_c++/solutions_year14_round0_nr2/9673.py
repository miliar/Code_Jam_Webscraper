#include <iostream>
#include <fstream>
#include <iomanip>


int main(int /* argc */, const char** argv) {
  std::ifstream ifs{argv[1]};

  unsigned int numberOfTestCases;
  ifs >> numberOfTestCases;

  //std::clog << "numberOfTestCases " << numberOfTestCases << '\n';

  const double cookiesPerSecond{2.0};
  for(unsigned int testCase{0}; testCase < numberOfTestCases; ++testCase) {
    double C, F, X;
    ifs >> C >> F >> X;
    //std::clog << "C " << C << " F " << F << " X " << X << '\n';

    double upperBoundOnResult{X / cookiesPerSecond}, result{upperBoundOnResult};

    //std::clog << "upperBoundOnResult " << upperBoundOnResult << '\n';

    unsigned int n{1};
    do {
      upperBoundOnResult = result;

      double fixedFarmPurchaseCost{0};
      for(unsigned int i{1}; i <= n; ++i) fixedFarmPurchaseCost += C / ((i - 1) * F + cookiesPerSecond);
      const double crossingCost{X / (n * F + cookiesPerSecond)};

      result = fixedFarmPurchaseCost + crossingCost;

      //std::clog << "n " << n
      //          << " fixedFarmPurchaseCost " << fixedFarmPurchaseCost << " crossingCost " << crossingCost
      //          << std::fixed << std::setprecision(7) << " result " << result << " upperBoundOnResult " << upperBoundOnResult << '\n';

      ++n;
    } while(result < upperBoundOnResult);

    //std::cout << "Case #" << testCase + 1 << ": " << std::fixed << std::setprecision(7) << result << '\n';
    std::cout << "Case #" << testCase + 1 << ": " << std::fixed << std::setprecision(7) << upperBoundOnResult << '\n';
  }
}
