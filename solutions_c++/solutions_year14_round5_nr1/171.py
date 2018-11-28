#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <vector>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <deque>
#include <cassert>

using namespace std;

#ifdef WIN32
	#define I64 "%I64d"
#else
	#define I64 "%lld"
#endif

typedef long long ll;

#define F first
#define S second
#define mp make_pair
#define pb push_back
#define all(s) s.begin(), s.end()
#define sz(s) (int(s.size()))
#define fname "a"
#define ms(a,x) memset(a, x, sizeof(a))
#define forit(it,s) for(__typeof(s.begin()) it = s.begin(); it != s.end(); ++it)
#define MAXN 1000001

int n, p, q, r, s;
int a[MAXN];
ll b[MAXN];

inline ll get(int l, int r)
{
	if (r < 0) return 0;
	ll res = b[r];
	if (l)
		res -= b[l - 1];
	return res;
}

inline void solve()
{
	scanf("%d%d%d%d%d", &n, &p, &q, &r, &s);
	for (int i = 0; i < n; ++i)
	{
		a[i] = (1LL * i * p + q) % r + s;
		b[i] = a[i] + (i ? b[i - 1] : 0);
	}
	ll ans = 0;
	for (int i1 = 0, i2 = 0; i1 < n; ++i1)
	{
		while(i2 < n && get(i1, i2) < get(i2 + 1, n - 1))
			++i2;
		ll t1 = get(0, i1 - 1);
		ll t2 = get(i1, i2);
		ll t3 = get(i2 + 1, n - 1);
      ans = max(ans, t1 + t2 + t3 - max(t1, max(t2, t3)));
      if (i1 > i2 - 1) continue;
		t1 = get(0, i1 - 1);
		t2 = get(i1, i2 - 1);
		t3 = get(i2, n - 1);
      ans = max(ans, t1 + t2 + t3 - max(t1, max(t2, t3)));
	}
	printf("%.15lf\n", 1. * ans / b[n - 1]);
}

int main()
{
	#ifdef LOCAL
	freopen(fname".in", "r", stdin);
	freopen(fname".out", "w", stdout);
	#endif

	int tt;
	scanf("%d", &tt);
	for (int t = 0; t < tt; ++t)
	{
		printf("Case #%d: ", t + 1);
		solve();
	}
	return 0;
}
