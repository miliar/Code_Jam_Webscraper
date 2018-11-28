#include <cstdio>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <string>
#include <cstring>
#include <iostream>
#include <windows.h>

using namespace std;

#pragma comment(linker, "/STACK:167772160")
typedef long long ll;
typedef pair<int, int> pii;
const int INF = 1e9;
const double EPS = 1e-9;

const ll MOD = 1000002013;

ll N, M;

struct interval
{
	ll l, r, n;

	interval(){}

	interval(ll _l, ll _r, ll _n) :
	l(_l), r(_r), n(_n)
	{}

	ll getCost()
	{
		ll cnt = r - l;
		ll ans = cnt*N - (cnt - 1) * cnt/2;
		ans %= MOD;
		return (ans * n) % MOD;
	}
	void scan()
	{
		scanf("%lld%lld%lld", &l, &r, &n);
	}
	
	bool operator < (const interval & other) const
	{
		if (l != other.l)
			return l < other.l;
		return r < other.r;
	}

} I[100500];

vector<interval> x;

void add(interval v)
{
	int to = x.size();
	for (int i = 0; i < to; ++i)
	{
		if (v.n == 0)
			break;
		if (x[i].r < v.l)
			continue;
		if (x[i].l > v.r)
			continue;
		if (x[i].l < v.l && x[i].r < v.r)
		{
			ll n = min(x[i].n, v.n);
			x[i].n -= n;
			v.n -= n;
			x.push_back(interval(v.l, x[i].r, n));
			x.push_back(interval(x[i].l, v.r, n));
		}

		if (v.l < x[i].l && v.r < x[i].r)
		{
			ll n = min(x[i].n, v.n);
			x[i].n -= n;
			v.n -= n;
			x.push_back(interval(x[i].l, v.r, n));
			x.push_back(interval(v.l, x[i].r, n));
		}
	}
	x.push_back(v);
	sort(x.begin(), x.end());
	int cur = 0;
	for (int i = 0; i < x.size(); ++i)
	{
		if (x[i].n == 0)
			continue;
		if (cur > 0 && x[cur-1].l == x[i].l && x[cur-1].r == x[i].r)
		{
			x[cur-1].n += x[i].n;
			continue;
		}
		x[cur] = x[i];
		++cur;
	}
	while(x.size() > cur)
		x.pop_back();
}

bool check()
{
	for (int i = 0; i < x.size(); ++i)
	{
		for (int j = i + 1; j < x.size(); ++j)
		{
			if (x[i].l < x[j].l && x[i].r < x[j].r && x[i].r >= x[j].l)
				return false;
		}
	}
	return true;
}

void solve()
{
	scanf("%lld%lld", &N, &M);
	ll cur = 0;
	for (int i = 0; i < M; ++i)
	{
		I[i].scan();
		cur += I[i].getCost();
	}
	while (true)
	{
		x.clear();
		for (int i = 0; i < M; ++i)
		{
			add(I[i]);
		}
		if (check())
			break;
		M = x.size();
		for (int i = 0; i < M; ++i)
		{
			I[i] = x[i];
		}
	}
	for (int i = 0; i < x.size(); ++i)
	{
		cur -= x[i].getCost();
	}
	cur %= MOD;
	cur = (cur + MOD) % MOD;
	printf("%lld\n", cur);
}
int main()
{
	int curTime = GetTickCount();
	freopen("Atest.txt", "r", stdin);
	freopen("Aout.txt", "w", stdout);

	int T;
	scanf ("%d", &T);
	int nxt = 0;
	int step = (T + 999)/1000;
	for (int i = 0; i < T; ++i)
	{
		printf("Case #%d: ", i + 1);
		if (i < 1000 || i == nxt)
		{
			fprintf(stderr, "\rTest: %3d/%d     Time: %4d ms", i+1, T, (int)(GetTickCount() - curTime));
			if (i == nxt)
				nxt += step;
		}
		solve();
	}
	fprintf(stderr, "\rTest: Done/%d     Time: %4d ms         \n", T, (int)(GetTickCount() - curTime));
	return 0;
}