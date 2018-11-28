#include <bits/stdc++.h>

using namespace std;

int tsts;

void solve(double &c, double f, double &x, double &best, double acum = 0.0, double cps = 2.0)
{
  if (acum + x / cps > best) return;
  best = min(best, acum + x / cps);
  solve(c, f, x, best, acum + c / cps, cps + f);
}

int main()
{
//freopen("B-large.in", "r", stdin);
  freopen("B-large.in", "r", stdin);
  freopen("myfile.out", "w", stdout);
  cin >> tsts;
  for (int tno = 1; tno <= tsts; tno++)
  {
    double c, f, x;
    cin >> c >> f >> x;
    double ret = 1e9;
    double acum = 0.0;
    double cps = 2.0;
    for (int i = 0; i < 1000000; i++)
    {
      if (acum + x / cps > ret) break;
      ret = min(ret, acum + x / cps);
      acum += c / cps;
      cps += f;
    }


    cout << "Case #" << tno << ": ";
    cout << fixed << setprecision(10) << ret << endl;
  }
  return 0;
}
