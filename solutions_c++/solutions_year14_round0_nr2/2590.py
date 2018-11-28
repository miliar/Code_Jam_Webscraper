#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;
#define mid ((l+r)>>1)
const long long INF = 1e9 + 7;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int ncase;
	cin >> ncase;
	int ks = 1;
	while (ncase--)
	{
		double c, f, x;
		double p = 2;
		cin >> c >> f >> x;
		double ans = x / p;
		double t = 0;
		while (t <= ans)
		{
			t += c / p;
			p += f;
			ans = min(ans, t + x / p);
		}
		printf("Case #%d: %.7lf\n", ks++, ans);
	}
	return 0;
}