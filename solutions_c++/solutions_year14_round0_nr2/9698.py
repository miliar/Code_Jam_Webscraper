//James Stojic

#include <iostream>
#include <iomanip>
using namespace std;
double findTime(double farmCost, double rateInc, double toWin, double rate);

int main ()
{
  int trials;
  double farmCost, rateInc, toWin, time, rate = 2;
  cout << setiosflags(ios::fixed)<<setprecision(7);
  cin >> trials;
  for(int i = 1; i <= trials; i++)
  {
    cin >> farmCost >> rateInc >> toWin;
    time = findTime(farmCost, rateInc, toWin, rate);
    cout << "Case #" << i << ": " << time << endl;
  }
  return 0;
}

double findTime(double farmCost, double rateInc, double toWin, double rate)
{
  double winNextTime = toWin / (rate + rateInc), buyFarmNow = farmCost / rate, winNow = toWin / rate;

  if(winNextTime + buyFarmNow >= winNow)
    return winNow;
  
  else
    return buyFarmNow + findTime(farmCost, rateInc, toWin, rate + rateInc);
}











