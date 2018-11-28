#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

double optimalTime(double c, double f, double x) {
  double cRate = 2.0;
  double waitTime = x/cRate;
  if(x <= c)
    return waitTime;
  double curTime = c/cRate; 
  while(true) {
    //Quicker to wait or build
    double waitTime = (x-c)/cRate;
    cRate += f;
    double buildWaitTime = x/cRate;
    if(waitTime <= buildWaitTime)
      return curTime+waitTime;
    curTime += c/cRate;
  }
}

int main() {
  int numCases;
  std::cin >> numCases;
  for(int cas=1; cas<=numCases; cas++) {
    double c, f, x;
    std::cin >> c >> f >> x;
    double time = optimalTime(c,f,x);
    std::cout << "Case #" << cas << ": " << std::setprecision(30) << time << "\n";
  }
  return 0;
}
