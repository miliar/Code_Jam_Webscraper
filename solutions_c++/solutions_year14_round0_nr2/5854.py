#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
  int T;
  cin >> T;
  for (int counter = 1; counter <= T; counter++) {
    long double C, F, X;
    // C: cookie farm cost
    // F: cookie farm production 
    // X: target
    cin >> C >> F >> X;

    long double T_last = 0; // time last factory bought
    int factories = 0; // number of factories
    long double ans = X / (long double) (2 + factories * F) + T_last;
    while (true) {
      T_last += C / (long double) (2 + factories * F);
      factories++;
      long double next = X / (long double) (2 + factories * F) + T_last;
      if (next >= ans) {
        break;
      }
      ans = next;
    }
    cout.precision(10);
    cout.setf(ios::fixed, ios::floatfield);
    cout << "Case #" << counter << ": " << ans << "\n";
  }
  return 0;
}

