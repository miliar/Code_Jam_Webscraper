#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cstdint>
#include <memory.h>
using namespace std;

int gcd(int a, int b)
{
  if (b == 0) return a;
  return gcd(b, a % b);
}

void solve()
{
  int p; cin >> p;

  vector<int> a(p);
  vector<int> b(p);
  for (auto &i: a) cin>>i;
  for (auto &i: b) cin>>i;

  int g = b[0];
  for (auto &i: b) g=gcd(g, i);
  for (auto &i: b) i/=g;

  vector<int> ans;
  for (int i=0;(1<<i) < g; i++)
    ans.push_back(0);

  int pn = 0;
  for (auto &i: b) pn+=i;

  int n = 0;
  for (; (1 << n) < pn; n++);

  multiset<int> ss;
  for (int i=0;i<p;i++){
    for (int j=0;j<b[i];j++)
      ss.insert(a[i]);
  }

  while(n--) {
    int c = *next(ss.begin());
    ans.push_back(c);

    multiset<int> tt;
    while (ss.size()) {
      int l = *ss.rbegin();
      ss.erase(ss.find(l));
      ss.erase(ss.find(l-c));
      tt.insert(l-c);
    }

    ss = tt;
  }

  for (int i=0;i<ans.size();i++) {
    if (i>0) cout << " ";
    cout << ans[i];
  }
  cout << endl;
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
