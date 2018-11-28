#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <climits>
using namespace std;

int main ()
{
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int TC; scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++)
	{
		double c, f, x; scanf("%lf%lf%lf", &c, &f, &x);
		double ans = 0, r = 2;
		while (1)
		{
			double t1 = x/r, t2 = c/r, t3 = x/(f+r);
			if (t1 <= t2 + t3)
			{
				ans += t1; break;
			}
			else
			{
				ans += t2; r += f;
			}
		}
		printf("Case #%d: ", tc);
		printf("%.7f\n", ans);
	}

}