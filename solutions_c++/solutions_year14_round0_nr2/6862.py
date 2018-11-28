#include <iostream>
#include <cstdio>
#include <cmath> //ceil
#include <algorithm> //max

using namespace std;

int main() 
{
  int T;
  double C, F, X;
  // Initial rate
  double f0 = 2.0;
  // Get the number of testcases
  cin >> T;
  for (int t=1; t<=T; t++) 
    {
      cin >> C >> F >> X;
      // Number of farms to buy
      int n = ceil((F*(X-C)/C - f0)/F);
      // Make sure n is not negative
      n = max(n, 0);
      
      double time = 0;
      // Time to buy my farms
      for (int i=0; i<n; i++) 
        {
          time += C/(i*F + f0);
        }
      // Have farms, add time to get X
      time += X/(n*F + f0);

      printf("Case #%d: %.7f\n", t, time);
    }
  return 0;
}
