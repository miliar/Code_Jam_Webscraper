#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <map>
#include <set>
using namespace std;
typedef long long int64;
#define rep(x, n) for (int x = 1; x <= n; ++x)
#define zrp(x, n) for (int x = n; x; --x)
#define FOR(x, l, r) for (int x = l; x <= r; ++x)
#define foredge(i, x) for (int i = start[x]; i; i = e[i].l)
struct edge{int a, l;};
set<long long> S;
long long ans[505], now;
int d[505][10];
int n, j, t;

bool canDiv(long long now, int base, int p)
{
	long long s = 0, x = 1;
	rep(i, n)
	{
		if (now & 1)
			s = (s + x) % p;
		x = (x * base) %p;
		now >>= 1;
	}
	if (s == 0) return true;
	return false;
}

bool check(long long now)
{
	FOR(b, 2, 10)
	{
		bool flag = 0;
		for (int k = 3; k <= 1000; k += 2)
			if (canDiv(now, b, k))
			{
				d[t][b] = k;
				flag = 1;
				break;
			}
		if (!flag) return false;
	}
	return true;
}

int main()
{
	n = 32;
	j = 500;

	t = 1;
	while (t <= j)
	{
		now = (1LL << (n - 1)) + rand() % (1LL << (n - 1));
		if (now % 2 == 0) continue;
		if (S.find(now) != S.end())
			continue;
		if (!check(now)) continue;
		S.insert(now);
		ans[t] = now;
		++t;
	}

	printf("Case #1:\n");
	rep(i, j)
	{
		rep(w, n) printf("%d", (int)(ans[i] >> (n - w)) & 1);
		FOR(b, 2, 10) printf(" %d", d[i][b]);
		puts("");
	}
	return 0;
}
