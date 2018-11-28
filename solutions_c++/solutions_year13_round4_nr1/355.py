#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <cmath>
#include <ctime>

using namespace std;

const long long mod = 1000002013;

int n, m;
vector< long long > p;
vector< long long > l, r;

map< int, pair<long long, long long> > inout;
map< int, long long > kol;

long long sum(long long q) {
  if (q <= 0)
    return 0;
  return (q * (q + 1) / 2);
}

long long calc(long long q, long long w) {
  return ((n * (w - q)) % mod - sum(w - q - 1)) % mod;
}

void solve() {
  long long ans = 0;
  long long ans2 = 0;
  cin >> n >> m;
  p.resize(m);
  l.resize(m);
  r.resize(m);
  inout.clear();
  for (int i = 0; i < m; i++)
  {
    cin >> l[i] >> r[i] >> p[i];
    l[i]--; r[i]--;
    inout[l[i]].first += p[i];
    inout[r[i]].second += p[i];
    ans2 = (ans2 +  (p[i] * calc(l[i], r[i])) % mod) % mod;
  }
  
  kol.clear();
  map< int, pair< long long, long long> >::iterator it = inout.begin();
  for (; it != inout.end(); it++) {
    kol[it->first] += it->second.first;
    long long out = it->second.second;
    if (out > 0)
    {
      map<int, long long>::reverse_iterator q = kol.rbegin();
      for (;q != kol.rend() && out > 0; q++) {
	int type = q->first;
	long long goout = min(out, q->second);
	ans = (ans + (goout * calc(type, it->first)) % mod) % mod;
	out -= goout;
	q->second -= goout;
      }
    }
  }
  
  cout << ((ans2 - ans) % mod + mod) % mod << endl;
}

int main() {
#ifdef OFFLINE
  freopen("A_input.txt","r", stdin);
  freopen("A_output.txt","w", stdout);
#endif
  int t;
  scanf("%d\n", &t);
  for (int testnum = 0; testnum < t; testnum++) {
    printf("Case #%d: ", testnum + 1);
    solve();
  }
}
