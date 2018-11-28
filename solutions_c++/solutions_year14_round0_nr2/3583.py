#include <iostream>
#include <iomanip>

using namespace std;

double C;
double F;
double X;

double totalTime(double curRate, double curTotal)
{
  double farmTime;
  double overallTime;

  farmTime =  C/curRate;
  overallTime = X/curRate;

  //  cout << "OverallTime " << overallTime << endl;
  //  cout << "FarmTime " << farmTime << endl;

  if (overallTime <= (farmTime + X/(curRate+F))) {
    return (overallTime + curTotal);
  } else {
    return totalTime(curRate + F, farmTime+curTotal);
  }
}

int main()
{
  int totalTests = 0;
  int curTest = 0;

  double output;

  cin >> totalTests;

  while(curTest != totalTests) {
    curTest++;

    cin >> C >> F >> X;

    //    cout << C << " " << " " << F << " " << X;
    output = totalTime(2,0);
    
    cout << "Case #" << curTest << ": " << setprecision(10) << output << endl;

  }

  return 0;
}


