#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <cassert>

#define LL long long

using namespace std;

struct elem
{
	int s;
	int f;
	int amount;
};
const int maxn = 100005;

inline bool intersect(elem e1, elem e2)
{
	return max(e1.s, e2.s) <= min(e1.f, e2.f);
}

elem a[maxn];
int prec[maxn];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++)
	{
		printf("Case #%d: ", test);
		int n, m;
		scanf("%d%d", &n, &m);
		assert(n < maxn);
		//int total = 0;
		for (int q = 1; q <= m; q++)
		{
			scanf("%d%d%d", &a[q].s, &a[q].f, &a[q].amount);
			//total += a[q].amount;
		}
		prec[1] = 0;
		for (int j = 2; j <= n; j++)
			prec[j] = prec[j - 1] + (j - 1);
		LL answer = 0;
		int cnt = m;
		while(true)
		{
			int best = 0;
			int spec1, spec2;
			for (int first = 1; first <= cnt; first++)
				for (int second = 1; second <= cnt; second++) if ((a[first].amount > 0) && (a[second].amount > 0) && 
				(first != second) && (intersect(a[first], a[second])) && (a[first].s <= a[second].f) && (a[second].s <= a[first].f))
				{
					int was = prec[a[first].f - a[first].s] + prec[a[second].f - a[second].s];
					int nnew = prec[a[first].f - a[second].s] + prec[a[second].f - a[first].s];
					int new_profit = -was + nnew;
					if (new_profit > best)
					{
						best = new_profit;
						spec1 = first;
						spec2 = second;
					}
				}
			if (best == 0)
				break;
			
			//cnt++;
			int tt = min(a[spec1].amount, a[spec2].amount);
			a[spec1].amount -= tt;
			a[spec2].amount -= tt;
			answer += (LL)best * (LL) tt;

			int t1 = a[spec1].s;
			int t2 = a[spec2].f;
			int t3 = a[spec2].s;
			int t4 = a[spec1].f;

			cnt++;
			a[cnt].s = t1;
			a[cnt].f = t2;
			a[cnt].amount = tt;

			cnt++;
			a[cnt].s = t3;
			a[cnt].f = t4;
			a[cnt].amount = tt;
			

		}
		//printf("cnt = %d\n", cnt);
		cout << answer << endl;
	}
}