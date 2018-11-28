#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <ctime>
#include <cstring>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <algorithm>

#define sz(c) ((int)(c).size())
#define all(c) (c).begin(), (c).end()
#define mp make_pair

using namespace std;
typedef long long ll;

typedef map<int, ll, std::greater<int> > t_map;

inline ll Cost( int n, ll L )
{
  return L * n - L * (L - 1) / 2;
}

void testCase()
{
  int n, m;
  scanf("%d%d", &n, &m);
  map<int, ll> in, out;
  ll fairCost = 0;
  vector<int> ti;
  for (int i = 0; i < m; i++)
  {
    int a, b, p;
    scanf("%d%d%d", &a, &b, &p);
    a--, b--;
    assert(0 <= a && a < b && b < n);
    fairCost += p * Cost(n, b - a);
    in[a] += p;
    out[b] += p;
    ti.push_back(a);
    ti.push_back(b);
  }

  sort(all(ti));
  ti.resize(unique(all(ti)) - ti.begin());

  map<int, ll>::iterator inIt = in.begin(), outIt = out.begin();
  vector<int>::iterator t = ti.begin();
  
  t_map tickets;
  ll total = 0;
  for (; t != ti.end(); ++t)
  {
    for (; inIt != in.end() && inIt->first == *t; ++inIt)
      tickets[*t] += inIt->second;
    for (; outIt != out.end() && outIt->first == *t; ++outIt)
    {
      ll cnt = outIt->second;
      while (!tickets.empty() && cnt > 0)
      {
        t_map::iterator ticketIt = tickets.begin();
        ll val = min(ticketIt->second, cnt);
        assert(ticketIt->first <= *t);
        total += val * Cost(n, *t - ticketIt->first);
        cnt -= val;
        ticketIt->second -= val;
        if (ticketIt->second == 0)
          tickets.erase(ticketIt);
      }
    }
  }
  assert(total <= fairCost);
  cout << fairCost - total << endl;
}

int main() {
//  freopen("sample.in", "rt", stdin);
//  freopen("output.txt", "wt", stdout);
  int n;
  scanf("%d", &n);
  for (int ti = 0; ti < n; ++ti) {
    printf("Case #%i: ", ti + 1);
    testCase();
  }
  return 0;
}
