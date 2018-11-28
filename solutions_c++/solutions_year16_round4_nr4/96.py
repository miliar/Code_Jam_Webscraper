#include <bits/stdc++.h>
using namespace std;

int n, bad;
string a[33];

int att(int i, int p[], int flag[], int mask)
{
  if (i == n)
    return 1;
  int x = p[i], good = 0;
  for (int j = 0; j < n; j++)
    if (!flag[j] && (a[x][j] == '1' || mask >> (x * n + j) & 1))
    {
      flag[j] = 1;
      if (!att(i + 1, p, flag, mask))
        return 0;
      good = 1;
      flag[j] = 0;
    }
  return good;
}

int canOperate(int mask)
{
  int p[33], flag[33] = {0};
  for (int i = 0; i < n; i++)
    p[i] = i;
  do
  {
    if (!att(0, p, flag, mask))
      return 0;
  } while (next_permutation(p, p + n));
  return 1;
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
    cin >> n;
    for (int i = 0; i < n; i++)
      cin >> a[i];

    int ans = n * n;
    for (int mask = 0; mask < 1 << n * n; mask++)
      if (canOperate(mask))
        ans = min(ans, __builtin_popcount(mask));

    cout << "Case #" << iTest << ": " << ans << endl;
  }
}