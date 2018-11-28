#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

const double EPS = 1e-7;

int main()
{
  int T;
  cin >> T;
  for (int testcase = 1; testcase <= T; ++testcase) {
    const long double CR = 2.0;
    long double C, F, X;
    cin >> C >> F >> X;

    vector<long double> dp(10001, 0.0);
    for (int i = 1; i < 10001; ++i)
      dp[i] = dp[i-1] + (C / (CR + (F * (i - 1))));

    long double ans = 1e20;
    for (int i = 0; i < 10001; ++i) {
      long double sec = dp[i] + (X / (CR + (F * i)));
      if (sec + EPS < ans) {
        ans = sec;
      }
    }

    cout << "Case #" << testcase << ": " << setprecision(30) << ans << endl;
  }
  return 0;
}
