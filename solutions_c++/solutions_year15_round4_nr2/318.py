#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

const double eps = 1e-10;

void solve()
{
  int n;
  double v, x;
  cin>>n>>v>>x;
  cout << setiosflags(ios::fixed) << setprecision(12);

  vector<pair<double,double>> w(n);
  for (auto &i: w) cin>>i.first>>i.second;

  if (n == 1) {
    if (abs(w[0].second - x) < eps) {
      cout << v / w[0].first << endl;
      return;
    }
    cout << "IMPOSSIBLE" << endl;
    return;
  }

  if (n == 2) {
    double mi = min(w[0].second, w[1].second);
    double ma = max(w[0].second, w[1].second);
    if (!(mi <= x && x <= ma)){
      cout << "IMPOSSIBLE" << endl;
      return;
    }

    if (ma - mi < eps) {
      cout << v / (w[0].first + w[1].first) << endl;
      return;
    }

    double t = (v*x-v*w[1].second)/(w[0].second-w[1].second);
    double u = v - t;
    double ans = max(t/w[0].first, u/w[1].first);
    cout << ans << endl;
    return;
  }

  cout << "IMPOSSIBLE" << endl;
}

int main()
{
  int cases; cin>>cases;
  for (int cn=1;cn<=cases;cn++){
    cout << "Case #" << cn << ": ";
    solve();
  }
  return 0;
}
