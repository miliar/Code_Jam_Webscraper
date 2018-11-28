#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <cassert>

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <bitset>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef long double ldouble;

const ll mod = 1000002013ll;

struct data
{
	ll l, r, p;
	data() { l = r = p = 0; }
	data(const ll &_l, const ll &_r, const ll &_p) { l = _l, r = _r, p = _p; }
};

struct ev
{
	ll t, p;
	ev() { t = p = 0; }
	ev(const ll &_t, const ll &_p) { t = _t; p = _p; }
};

data a[1010];
ev b[2020], st[1010];
int n, m, sz;
ll ans;

bool operator<(const ev &a, const ev &b) { return (a.t != b.t ? a.t < b.t : a.p > b.p); }

ll fc(const ll &x) { return ((x + 1) * x / 2ll) % mod; }

ll pop(ll t, ll x)
{
	ll ans = 0;
	while (sz > 0 && x > 0)
	{
		ll dg = min(st[sz - 1].p, x);
		st[sz - 1].p -= dg; x -= dg;
		ans = (ans + dg * fc(t - st[sz - 1].t)) % mod;
		if (st[sz - 1].p == 0) sz--;
	}
	return ans;
}

int main()
{
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);

	int tst; scanf("%d", &tst);
	for (int ts = 1; ts <= tst; ts++)
	{
		printf("Case #%d: ", ts);
		scanf("%lld%d", &n, &m); ans = 0, sz = 0;
		for (int i = 0; i < m; i++)
		{
			scanf("%lld%lld%lld", &a[i].l, &a[i].r, &a[i].p);
			b[2 * i].t = a[i].l, b[2 * i].p = a[i].p;
			b[2 * i + 1].t = a[i].r, b[2 * i + 1].p = -a[i].p;
		}
		sort(b, b + 2 * m);
		for (int i = 0; i < 2 * m; i++)
		{
			if (b[i].p > 0) st[sz++] = b[i];
			else ans = (ans + pop(b[i].t, -b[i].p)) % mod;
		}
		for (int i = 0; i < m; i++)
			ans = (ans + mod - fc(a[i].r - a[i].l) * a[i].p % mod) % mod;
		printf("%lld\n", ans);
	}

	return 0;
}