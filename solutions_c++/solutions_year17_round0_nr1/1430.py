#include <bits/stdc++.h>
using namespace std;

int main()
{
  int test;
  cin >> test;
  for (int iTest = 1; iTest <= test; iTest++)
  {
    cerr << "Running test " << iTest << endl;
    string s;
    int k, ans = 0;
    cin >> s >> k;
    for (int i = 0; i < s.size(); i++)
      if (s[i] == '-')
      {
        if (i + k > s.size())
        {
          ans = -1;
          break;
        }
        ans++;
        for (int j = i; j < i + k; j++)
          if (s[j] == '-') s[j] = '+';
          else s[j] = '-';
      }

    cout << "Case #" << iTest << ": ";
    if (ans < 0) cout << "IMPOSSIBLE" << endl;
    else cout << ans << endl;
  }
}