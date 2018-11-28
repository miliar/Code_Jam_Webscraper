#include <iostream>
#include <iomanip>
#include <set>
#include <string>

int main()
{
  int T;
  std::cout << std::setprecision(7) << std::fixed;

  double C, F, X;

  double bestTime, currTotalTime, currFarmBuildTime, currCookieProduceTime;

  int noFarms;

  std::cin >> T;

  // for each case
  for (int i = 1; i <= T; ++i) {

    std::cin >> C;
    std::cin >> F;
    std::cin >> X;

    currFarmBuildTime = 0.0;     // this number needs to be incremented for each noFarms
    noFarms = 0;

    currTotalTime = X/2.0; // worst case, with 0 farms

    do {
      // increment number of Farms built and figure out if the time improves
      ++noFarms;

      bestTime = currTotalTime;

      currFarmBuildTime += C / (2.0 + (noFarms-1) * F);

      currCookieProduceTime = X / (2.0 + noFarms * F);

      currTotalTime = currFarmBuildTime + currCookieProduceTime;

    }
    while (currTotalTime < bestTime);

    std::cout << "Case #" << i << ": " << bestTime << std::endl;
  }

  return 0;
}
