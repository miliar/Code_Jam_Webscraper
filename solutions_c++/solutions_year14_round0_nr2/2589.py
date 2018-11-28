#include <vector>
#include <algorithm>
#include <utility>
#include <string>
#include <iostream>
#include <iterator>
#include <cmath>

using namespace std;

double solve(const double C, const double F, const double X, const int fnum)
{
  double t1 = 0;

  // fnum個のfarmを買うまでの時間
  for (int i = 0; i < fnum; ++i) {
    t1 += C / (F * i + 2.0);
  }

  // X個のクッキーをfnum個のfarmで作るまでの時間
  double t2 = X / (fnum * F + 2.0);

  return t1 + t2;
}

int main()
{
  int T;
  cin >> T;


  for (int cs = 1; cs <= T; ++cs) {
    double C, F, X;
    cin >> C >> F >> X;
    
    double ans = X;
    for (int i = 0; i < X; ++i) {
      double tmp = solve(C, F, X, i);
      //cerr << "\t" << i << ": " << tmp << endl;

      if (tmp < ans) ans = tmp;
      else           break;
    }

    cout.precision(7 + log10(ans)+1);

    cout << "Case #" << cs << ": " << ans << endl;
  }

  return 0;
}
