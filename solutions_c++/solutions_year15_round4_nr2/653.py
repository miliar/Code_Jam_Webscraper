#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <cstring>
#include <queue>
#include <deque>
#include <functional>
#include <climits>
#include <cassert>
#include <list>

#define mp make_pair
#define mt(a, b, c) mp(a, mp(b, c))
#define ABS(a) (((a) > 0) ? (a) : (-(a)))
#define ZERO(x) memset((x), 0, sizeof(x))
#define NEGATE(x) memset((x), 255, sizeof(x))

using namespace std;
typedef long long ll;

int main()
{
#ifdef XXX
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int t;
	cin >> t;

	for (int q = 0; q < t; q++)
	{
		int n;
		cin >> n;
		double v, x;
		cin >> v >> x;
		
		if (n == 1)
		{
			double t, r;
			cin >> r >> t;
			if (t != x)
			{
				printf("Case #%d: IMPOSSIBLE\n", q + 1);
				goto next_iter;
			}
			else
			{
				printf("Case #%d: %.10lf\n", q + 1, v / r);
				goto next_iter;
			}
		}

		if (n == 2)
		{
			double t1, t2, r1, r2;
			cin >> r1 >> t1 >> r2 >> t2;
			if (t1 == t2)
			{
				double t = t1;
				double r = r1 + r2;

				if (t != x)
				{
					printf("Case #%d: IMPOSSIBLE\n", q + 1);
					goto next_iter;
				}
				else
				{
					printf("Case #%d: %.10lf\n", q + 1, v / r);
					goto next_iter;
				}

			}
			else
			{
				double a2 = (x * v - t1 * v) / (r2 * t2 - r2 * t1);
				double a1 = (v - a2 * r2) / r1;
				if (a1 + 1e-9 < 0 || a2 + 1e-9 < 0)
				{
					printf("Case #%d: IMPOSSIBLE\n", q + 1);
					goto next_iter;
				}
				printf("Case #%d: %.10lf\n", q + 1, max(a1, a2));
				goto next_iter;
			}
		}
	next_iter:;

	}

	return 0;
}