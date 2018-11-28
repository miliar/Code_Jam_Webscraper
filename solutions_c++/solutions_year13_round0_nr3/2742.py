#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <map>
#include <vector>
using namespace std;
long long zsqrt(long long x)
{
	long long mid, l = 0, r = 10000000;
	while (l < r)
	{
		mid = (l + r + 1) >> 1;
		if (mid * mid <= x) l = mid;
		else r = mid - 1;
	}
	return l;
}
int ispa(long long x)
{
	long long hi = 1, lo = 1;
	while (hi <= x) hi *= 10;
	hi /= 10;
	while (lo <= hi)
	{
		if ((x / lo) % 10 != (x / hi) % 10)
			return 0;
		lo *= 10, hi /= 10;
	}
	return 1;
}
int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int tot;
	cin >> tot;
	long long st, en;
	for (int tt = 1; tt <= tot; tt++)
	{
		int ans = 0;
		cin >> st >> en;
		long sst = st, een = en;
		st = zsqrt(st);
		en = zsqrt(en);
		for (long long i = st; i <= en; i++)
		{
			if (ispa(i) && ispa(i * i) && i * i <= een && i * i >= sst)
				ans++;
		}
		printf("Case #%d: %d\n", tt, ans);
	}
	return 0;
}
