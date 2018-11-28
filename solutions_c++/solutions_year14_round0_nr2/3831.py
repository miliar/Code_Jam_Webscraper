#include <iostream>
#include <iomanip>
using namespace std;

int main() {
  int cases=0;
  cin >> cases;
  int casenum=0;
  while (casenum < cases) {
    casenum++;
    long double time=0.0;
    long double rate=2.0;
    long double farmCost=0.0;
    cin >> farmCost;
    long double rateInc=0.0;
    cin >> rateInc;
    long double goal=0.0;
    cin >> goal;
    long double ttWin=goal/rate;
    long double ttWinPlus=(farmCost/rate) + goal/(rate+rateInc);
    while (ttWin > ttWinPlus) {
      time+=farmCost/rate;
      rate+=rateInc;
      ttWin=goal/rate;
      ttWinPlus=(farmCost/rate) + goal/(rate+rateInc);
    }
    time+=ttWin;
    cout << "Case #" << casenum << ": " << fixed << setprecision(7) << time << endl;
  }
  return 0;
}

