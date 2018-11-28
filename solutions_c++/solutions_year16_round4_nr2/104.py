#include <bits/stdc++.h>
using namespace std;

double f[222][222], fl[222][222], fr[222][222];

double calc(vector <double> p)
{
  int n = p.size();
  memset(f, 0, sizeof f);
  f[0][0] = 1;
  for (int i = 0; i < n; i++)
    for (int j = 0; j <= n / 2; j++)
    {
      f[i + 1][j + 1] += f[i][j] * p[i];
      f[i + 1][j] += f[i][j] * (1 - p[i]);
    }
  return f[n][n / 2];
}

int main()
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  int test;
  cin >> test;
  for (int iTest = 1; iTest <= test; iTest++)
  {
    cerr << "Running test " << iTest << "..." << endl;
    int n, k;
    double p[222];

    cin >> n >> k;
    for (int i = 0; i < n; i++)
      cin >> p[i];
    sort(p, p + n);

    double ans = 0;
    for (int i = 0; i + k <= n; i++)
    {
      vector <double> cur;
      for (int j = 0; j < k; j++)
        cur.push_back(p[i + j]);
      ans = max(ans, calc(cur));
    }

    for (int i = 1; i < k; i++)
    {
      vector <double> cur;
      for (int j = 0; j < i; j++)
        cur.push_back(p[j]);
      for (int j = 0; j < k - i; j++)
        cur.push_back(p[n - 1 - j]);
      ans = max(ans, calc(cur));
    }

    cout << fixed << setprecision(9) << "Case #" << iTest << ": " << ans << endl;
  }
}