#include <iostream>
#include <algorithm>

using namespace std;

double R[109];
double C[109];

void solve()
{
  double V, X;
  int N;
  cin >> N >> V >> X;
  for (int i = 0; i < N; ++i)
    cin >> R[i] >> C[i];
  if (*min_element(C, C+N) > X || *max_element(C, C+N) < X)
  {
    cout << "IMPOSSIBLE";
    return;
  }
  if (N == 1)
  {
    cout << V/R[0];
  }
  else if (N == 2)
  {
    if (C[0] == X && C[1] == X)
    {
      cout << V/(R[0]+R[1]);
    }
    else if (C[0] == X)
    {
      cout << V/R[0];
    }
    else if (C[1] == X)
    {
      cout << V/R[1];
    }
    else
    {
      double F = V/(1.+(C[0]-X)/(X-C[1]));
      double S = V-F;
      cout.precision(9);
      cout << fixed << max(F/R[0], S/R[1]);
    }
  }
}

int main()
{
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i)
  {
    cout << "Case #" << i << ": ";
    solve();
    cout << endl;
  }
  return 0;
}
