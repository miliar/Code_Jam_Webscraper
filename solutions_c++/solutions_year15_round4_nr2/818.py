#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;

int main()
{
  ifstream cin("p2s.in");
  ofstream cout("p2s.out");
  int t, T;
  cin >> T;
  for (t = 1; t <= T; t ++)
  {
    cout << setiosflags(ios::fixed);
    cout << setprecision(7);

    cout << "Case #" << t << ": ";
    double n, v, x;
    double r[2], c[2];
    cin >> n >> v >> x;
    for (int i = 0; i < n ; i++)
      cin >> r[i] >> c[i];
    if (n == 1)
    {
      if (c[0] != x)
        cout << "IMPOSSIBLE" << endl;
      else
        cout << v / r[0] << endl;
      continue;
    }
    if (x > max(c[0], c[1]) || x < min(c[0], c[1]))
      cout << "IMPOSSIBLE" << endl;
    else
    {
      if (c[0] == c[1])
        cout << v / (r[0] + r[1]) << endl;
      else
      {
        double p = (x - c[1]) / (c[0] - c[1]);
        double vol[2];
        vol[0] = p * v;
        vol[1] = (1 - p) * v;
        double t[2];
        t[0] = vol[0] / r[0];
        t[1] = vol[1] / r[1];
        cout << max(t[0], t[1]) << endl;
      }
    }
  }
  return 0;
}


