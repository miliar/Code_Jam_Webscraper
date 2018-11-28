#include <iostream>
#include <algorithm>
#include <iomanip>

using namespace std;

double timeToObj(double t, int nFarm, double F, double X)
{
  return t + X / (2 + nFarm * F);
}

double minTime(double C, double F, double X)
{
  double t = 0;
  int nFarm = 0;
  while ( true ) {
    /* Go to time = we have C */
    t = timeToObj(t, nFarm, F, C);
    if ( timeToObj(t, nFarm, F, X - C) < timeToObj(t, nFarm + 1, F, X) )
      return timeToObj(t, nFarm, F, X - C);
    else
      ++nFarm;
  }
}

int main()
{
  int Ca = 1;
  int N;
  cin >> N;
  cerr << N;
  cout << fixed << setprecision(7);
  while ( Ca <= N ) {
    double C,F,X;
    cin >> C >> F >> X;
    cout << "Case #" << Ca << ": " << minTime(C, F, X) << endl;
    ++Ca;
  }
}
