#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <cmath>
#include <sstream>
#include <stack>
#include <cassert>

#define pb push_back
#define mp make_pair
#define PI 3.14159265358979
#define sqr(x) (x)*(x)
#define forn(i, n) for(int i = 0; i < n; ++i)
#define ALL(x) x.begin(), x.end()
#define sz(x) int((x).size())
#define X first
#define Y second
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
using namespace std;
typedef pair<int,int> pii;
const int INF = 2147483647;
const ll LLINF = 9223372036854775807LL;

const int mod = 1000002013;

int cnt(int c) {
  if (c == 0) return 0;
  --c;
  return (c*(ll)(c+1)/2)%mod;
}

void solve() {
  int n, m; scanf("%d%d", &n, &m);
  int norm = 0;
  vector<pii> v;
  forn (i, m) {
    int fr, to, c; scanf("%d%d%d", &fr, &to, &c);
    v.pb(mp(fr, -c));
    v.pb(mp(to, c));
    (norm += cnt(to-fr)*(ll)c%mod)%=mod;
  }
  sort(ALL(v));
  stack<pii> st;
  int ans = 0;
  forn(i, sz(v)) {
    int curpos = v[i].X;
    if (v[i].Y < 0) {
      v[i].Y = -v[i].Y;
      st.push(mp(curpos, v[i].Y));
    } else {
      int rem = v[i].Y;
      while (rem) {
        int curc = min(st.top().Y, rem);
        int pos = st.top().X;
        rem -= curc;
        st.top().Y -= curc;
        if (st.top().Y == 0) st.pop();
        (ans += (ll)curc*cnt(curpos-pos)%mod)%=mod;
      }
    }
  }
  assert(st.empty());
  int result = ((ans-norm)%mod+mod)%mod;
  printf("%d\n", result);
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
  int T; scanf("%d", &T); forn(test, T) {
    printf("Case #%d: ", test+1);
    solve();
  }
	return 0;
}