#include <algorithm>
#include <iostream>
#include <iomanip>
using namespace std;
const int MAX = 105;
pair<long double, long double> p[MAX];
long double x, v;
int n;
bool check(long double t)
{
	long double cur = 0.0, tmp = 0;
	int ptr = n - 1;
	while (ptr >= 0)
	{
		long double hv = p[ptr].second * t;
		if (cur + hv >= v)
		{
			tmp = tmp * cur + (v - cur) * p[ptr].first;
			cur = v;
			tmp /= cur;
			break;
		}
		else
		{
			tmp = tmp * cur + hv * p[ptr].first;
			cur += hv;
			tmp /= cur;
		}
		ptr--;
	}
	if (ptr == -1)
		return false;
	long double mx = tmp;
	cur = 0.0, tmp = 0;
	ptr = 0;
	while (ptr < n)
	{
		long double hv = p[ptr].second * t;
		if (cur + hv >= v)
		{
			tmp = tmp * cur + (v - cur) * p[ptr].first;
			cur = v;
			tmp /= cur;
			break;
		}
		else
		{
			tmp = tmp * cur + hv * p[ptr].first;
			cur += hv;
			tmp /= cur;
		}
		ptr++;
	}
	if (ptr == n)
		return false;
	long double mn = tmp;
	return (mn - 1e-16 <= x && x <= 1e-16 + mx);
}
int main()
{
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int _ = 1; _ <= t; _++)
	{
		cin >> n >> v >> x;
		for (int i = 0; i < n; i++)
			cin >> p[i].second >> p[i].first;
		sort(p, p + n);
		long double l = 0.0, r = 1e12 + 5.0;
		for (int i = 0; i < 2000; i++)
		{
			long double mid = (l + r) * 0.5;
			if (check(mid))
				r = mid;
			else
				l = mid;
		}
		if (r > 1e12)
			cout << "Case #" << _ << ": IMPOSSIBLE\n";
		else
			cout << "Case #" << _ << ": " << setprecision(8) << fixed << r << "\n";
	}
	return 0;
}
