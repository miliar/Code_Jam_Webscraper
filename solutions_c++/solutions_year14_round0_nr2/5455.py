#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <iostream>
#include <queue>

using namespace std;


int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int tt = 0; tt < t; tt++)
	{
		double c, f, x;
		scanf("%lf%lf%lf", &c, &f, &x);

		double ans = x / 2.0;
		double tm = 0, cur = 0, add = 2;
		while (tm < ans)
		{
			ans = min(ans, tm + x / add);
			tm += c / add;
			add += f;
		}
		printf("Case #%d: %.7lf\n", tt + 1, ans);
	}
	

	return 0;
}