/*
 * Cookies solver for google code jam
 * Author: Dov Kruger
 */
#include <iostream>
//#include <iomanip>
#include <stdio.h>
using namespace std;

void doCase() {
  double C, F, X;
  cin >> C >> F >> X;
  cerr << C << ' ' << F << ' ' << X << "\n";
  double rate = 2; // initial cookie production
  double totalTime = 0;
  double timeToWin, timeToFarm, rateWithFarm, timeIncludingFarm;
  for (;;) {
    timeToWin = X / rate;
    timeToFarm = C / rate;
    rateWithFarm = rate + F;
    timeIncludingFarm = timeToFarm + X / rateWithFarm;
//cerr << "Time=" << totalTime << "\n";
//    cerr << "TimeToWin=" << timeToWin << "\n";
//    cerr << "TimeToFarm=" << timeToFarm << "\n";
//    cerr << "rateWithFarm=" << rateWithFarm << "\n";
//    cerr << "TimeIncludingFarm=" << timeIncludingFarm << "\n";
    if (timeIncludingFarm < timeToWin) {
      totalTime += timeToFarm;
      rate = rateWithFarm;
    } else {
      totalTime += timeToWin;
      break;
    }
  }
  printf("%-12.7lf\n", totalTime);
}


int main() {
  int numcases;
  cin >> numcases;
  cerr << "CASES=" << numcases << "\n";
  for (int cases = 1; cases <= numcases; cases++) {
    printf("Case #%d: ", cases);
    doCase();
  }
}
