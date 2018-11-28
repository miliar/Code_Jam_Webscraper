#include <iostream>
#include <cmath>
#include <algorithm>
#include <iomanip>

using namespace std;

void solve()
{
  double C, F, X;
  cin >> C >> F >> X;

  double a = 2, b = 0;       // a*x+b
  double best = X/2.0;       // if we don't buy any farm

  while (1) {
    // when can we buy the next farm?
    double next = (C - b) / a;
    if (best <= next) break;

    a += F;
    b = -a * next;

    best = min(best, (X - b) / a);
  }

  cout << fixed << setprecision(10) << best << endl;

}

int main()
{
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": ";
    solve();
  }
  return 0;
}
