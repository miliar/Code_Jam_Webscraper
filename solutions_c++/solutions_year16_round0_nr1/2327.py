#include <bits/stdc++.h>
using namespace std;

int ans[1000100];

int main()
{
  ios::sync_with_stdio(0);
  cin.tie(0);

  for (int i = 1; i <= 1000000; i++)
  {
    int d[10] = {0}, cnt = 0, j = 1;
    while (1)
    {
      long long v = 1LL * i * j;
      while (v)
      {
        if (!d[v % 10])
          cnt += ++d[v % 10];
        v /= 10;
      }
      if (cnt == 10) break;
      j++;
    }
    ans[i] = j;
  }

  int test, n;
  cin >> test;
  for (int iTest = 1; iTest <= test; iTest++)
  {
    cerr << "Running test " << iTest << "..." << endl;
    cin >> n;
    cout << "Case #" << iTest << ": ";
    if (!n) cout << "INSOMNIA" << endl;
    else cout << ans[n] * n << endl;
  }
}