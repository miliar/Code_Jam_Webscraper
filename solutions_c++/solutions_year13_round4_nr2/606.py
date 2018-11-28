#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include <string>
#include <iomanip>
using namespace std;
int tolose(long long bet, long long ok, int t, int now)
{
	if (now >= ok)
		return 1;
	if (bet <= 0)
	{
		return 0;
	} else if (t >= 0)
	{
		bet--;
		bet >>= 1;
		now += (1 << t);
		if (now >= ok)
			return 1;
		return tolose(bet, ok, t - 1, now);
	} else
		return 1;
}
int towin(long long wor, long long ok, int t, long long now)
{
	if (now > ok)
		return 1;
	if (wor <= 0)
		return 0;
	else if (t >= 0)
	{
		wor--;
		wor >>= 1;
		now += (1LL << t);
		if (now > ok)
			return 1;
		return towin(wor, ok, t - 1, now);
	} else
		return 1;
}
int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int tot, tt;
	cin >> tot;
	for (tt = 1; tt <= tot; tt++)
	{
		long long n, p;
		cin >> n >> p;
		if (tt == 88)
			int ll = 1;
		long long l = 0, r = (1LL << n) - 1;
		long long vn = 1LL << n;
		while (l < r)
		{
			long long mid = (l + r + 1) >> 1;
			if (tolose(mid, p, n - 1, 0))
				r = mid - 1;
			else
				l = mid;
		}
		long long ans1 = l, ans2;
		l = 0, r = vn - 1;
		while (l < r)
		{
			long long mid = (l + r + 1) >> 1;
			if (towin(vn - mid - 1, vn - p - 1, n - 1, 0))
				l = mid;
			else
				r = mid - 1;
		}
		ans2 = l;
		cout << "Case #" << tt << ": " << ans1 << " " << ans2 << endl;
	}
	return 0;
}
