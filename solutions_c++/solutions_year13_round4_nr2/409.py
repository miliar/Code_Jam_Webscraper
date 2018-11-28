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

ll getMx(ll N, ll x)
{
	ll ans = 0;
	while (x)
	{
		N /= 2;
		ans += N;
		x = (x-1)/2;
	}
	return ans + 1;
}

ll getMin(ll N, ll x)
{
	ll ans = 0;
	x = N - x - 1;
	while (x)
	{
		N /= 2;
		x = (x-1)/2;
	}
	return N;
}

ll solve1(ll N, ll P)
{
	ll l = 0;
	ll r = N;
	while (l + 1 < r)
	{
		ll m = (l + r)/2;
		if (getMx(N, m) <= P)
			l = m;
		else
			r = m;
	}
	return l;
}

ll solve2(ll N, ll P)
{
	ll l = 0;
	ll r = N;
	while (l + 1 < r)
	{
		ll m = (l + r)/2;
		if (getMin(N, m) <= P)
			l = m;
		else
			r = m;
	}
	return l;
}

void solve()
{
	ll N, P;
	scanf("%lld%lld", &N, &P);
	N = 1ll << N;
	ll a = solve1(N, P);
	ll b = solve2(N, P);
	printf("%lld %lld\n", a, b);
}
int main()
{
	int curTime = GetTickCount();
	freopen("Btest.txt", "r", stdin);
	freopen("Bout.txt", "w", stdout);

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