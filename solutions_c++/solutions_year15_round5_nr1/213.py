#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cstdint>
#include <memory.h>
using namespace std;

vector<int> seq(int n)
{
  int64_t m, a, c, r;
  cin>>m>>a>>c>>r;
  vector<int> ret(n);
  for (int i=0;i<n;i++) {
    ret[i] = m;
    m = (m * a + c) % r;
  }
  return ret;
}

int rec(int par, int cur, int lo, int d, const vector<int> &s, const vector<vector<int>> &g)
{
  if (!(lo <= s[cur] && s[cur] <= lo + d))
    return 0;

  int ret = 1;
  for (auto &c: g[cur]) {
    if (par == c) continue;
    ret += rec(cur, c, lo, d, s, g);
  }
  return ret;
}

void solve()
{
  int n, d; cin>>n>>d;

  vector<int> s = seq(n);
  vector<int> m = seq(n);

  vector<vector<int>> g(n);
  for (int i=1;i<n;i++) {
    g[m[i]%i].push_back(i);
  }

  int ans = 0;
  for (int lo = 0; lo < 1000; lo++) {
    ans = max(ans, rec(-1, 0, lo, d, s, g));
  }
  cout << ans << endl;
}

int main()
{
  int cases; cin >> cases;
  for (int cn = 1; cn <= cases; cn++) {
    cout << "Case #" << cn << ": ";
    solve();
  }
  return 0;
}
