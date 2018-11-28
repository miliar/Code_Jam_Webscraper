#include <bits/stdc++.h>
using namespace std;

int n, r[22], p[22], s[22];
string sr[22], sp[22], ss[22];

int count(string s, char c)
{
  int res = 0;
  for (auto u : s)
    res += u == c;
  return res;
}

int main()
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  int test;
  cin >> test;
  for (int iTest = 1; iTest <= test; iTest++)
  { 
    string ans = "IMPOSSIBLE";
    cin >> n >> r[0] >> p[0] >> s[0];
    for (int i = 0; i < n; i++)
    {
      int sum = r[i] + s[i] + p[i];
      int rp = sum / 2 - s[i];
      int ps = sum / 2 - r[i];
      int sr = sum / 2 - p[i];
      if (rp < 0 || ps < 0 || sr < 0)
        break;
      p[i + 1] = rp;
      s[i + 1] = ps;
      r[i + 1] = sr;
      if (i == n - 1)
        ans = "";
    }

    sp[1] = "PR";
    sr[1] = "RS";
    ss[1] = "PS";
    for (int i = 2; i <= n; i++)
    {
      sp[i] = min(sp[i - 1] + sr[i - 1], sr[i - 1] + sp[i - 1]);
      sr[i] = min(ss[i - 1] + sr[i - 1], sr[i - 1] + ss[i - 1]);
      ss[i] = min(sp[i - 1] + ss[i - 1], ss[i - 1] + sp[i - 1]);
    }
    if (ans == "")
    {
      if (p[n]) ans = sp[n];
      else if (r[n]) ans = sr[n];
      else ans = ss[n];
      assert(count(ans, 'R') == r[0]);
      assert(count(ans, 'S') == s[0]);
      assert(count(ans, 'P') == p[0]);
    }

    cout << "Case #" << iTest << ": " << ans << endl;
  }
}