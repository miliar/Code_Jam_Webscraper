#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

#include <iomanip>

using namespace std;

int main(int argc, char* argv[])
{
  int T;
  cin >> T;
  double C, X, F;
  double total_time = 1.0;

  for (int ii = 1; ii <= T; ++ii)
  {
    cin >> C >> F >> X;

       
    double prev_cost = X / 2;
    double prev_overhead = 0;
    for (int jj = 0; ; ++jj)
    {
      double overhead = prev_overhead + (C / (2 + jj * F));
      double cost = overhead + (X / (2 + (jj + 1) * F));
      if (cost <= prev_cost)
      {
	prev_cost = cost;
	prev_overhead = overhead;
      }
      else
      {
	break;
      }
    }
    
    cout << std::fixed;
    cout << "Case #" << ii << ": " << setprecision(7) << prev_cost << endl;
  }
  return 0;
}
