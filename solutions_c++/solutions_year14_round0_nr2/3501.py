#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <iomanip>
using namespace std;
int T;
int main() {
  ios::sync_with_stdio(0);
  freopen("inB.txt", "r", stdin);
  freopen("outB.txt", "w", stdout);
  cin >> T;
  double C, prevF, F, X;
  double time = 0.0, tot_time=0.0;
  for (int cases = 1; cases <= T; ++cases) {
    cin >> C >> F >> X;
    tot_time = 0.0;
    cout << "Case #" << cases << ": ";
    prevF = 2.0;
    if (C > X) {
      cout.precision(7);
      cout << fixed << setprecision(7) << X/2.0 << "\n";
      continue;
    }    
    time = C/2.0;
    while (1) {
      double waiting_time = C/prevF;
      //cout << "1: " << waiting_time + X/(F+prevF) << " 2: " << X/prevF <<" ";
      if ((waiting_time + X/(F+prevF)) > X/prevF) {
        tot_time += X/prevF;
        break;
      } else {
        prevF += F;
      }
      //cout << waiting_time << "\n";
      tot_time += waiting_time;
    }
    //printf("%.7lf\n", tot_time);
    cout << fixed << setprecision(7) << tot_time << "\n";
  }
  return 0;
}