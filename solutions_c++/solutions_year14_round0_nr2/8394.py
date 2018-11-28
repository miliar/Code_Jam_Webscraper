#include <iostream>
using namespace std;

const double initialRate = 2; // initial production rate in cookies per second

double secondsBestStrategy(double C, double F, double X) {
  double currentRate = initialRate;
  double retVal = 0;
  double waitIncrement = X/currentRate;
  double buyIncrement = C/currentRate + X/(currentRate+F);
  while (buyIncrement < waitIncrement) {
    retVal += C/currentRate;
    currentRate += F;
    waitIncrement = X/currentRate;
    buyIncrement = C/currentRate + X/(currentRate+F);
  }
  retVal += X/currentRate;
  return retVal;
}

int main() {
  int nTestCases;
  cout.setf(ios::fixed);
  cout.precision(7);
  cin >> nTestCases;
  for (int c = 1; c <= nTestCases; ++c) {
    double C,F,X,seconds;
    cin >> C >> F >> X;
    seconds = secondsBestStrategy(C,F,X);
    cout << "Case #" << c << ": " << seconds << endl;
  }
}
