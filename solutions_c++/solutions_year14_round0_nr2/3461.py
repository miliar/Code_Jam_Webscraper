#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

int main ()
{
  int T;
  cin >> T;
  for(int t = 0; t < T; t++) {
    double C, F, X;
    cin >> C >> F >> X;
    double prev = 0.0;
    double f = 2.0;
    double bestCost = 200000000.0;
    while (true) {
      // calculate how much time it takes to get all cookies
      double cost = X/f;
      if (prev + cost > bestCost) {
        printf("Case #%d: %.7f\n", t+1, bestCost);
        break;
      }
      bestCost = cost + prev;
      prev += C/f;
      f += F;
    }
  }
}
