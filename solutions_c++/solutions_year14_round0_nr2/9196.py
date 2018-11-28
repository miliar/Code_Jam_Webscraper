#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

double calc(double C, double F, double X)
{
  double tap = 0;
  double tpp = 0;
  double tac = X/2;
  double tpc = 0;
  int i = 0;
  do
  {
    ++i;
    tap = tac;
    tpp = tpc;
    
    tac = X/(2 + i * F);
    tpc += C/(2 + (i - 1) * F);
   
  }while ((tac + tpc) < (tap + tpp));
  
    return tap + tpp;
}

int main(int argc, char* args[])
{
  int T;
  cin >> T;
  cout.precision(10);
  for (int i = 0; i != T; ++i)
  {
    double C, F, X;
    cin >> C >> F >> X;
    cout << "Case #" << i+1 << ": " << calc(C, F, X);
    if (i < T-1)
      cout << endl;
  }
  return 0;
}
