#pragma	comment(linker, "/STACK:100000000")
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iostream>
#include <list>
using namespace std;

typedef long long ll;
#define mod 1000000007
#define pi acos(-1.0)
#define eps 1e-9

int a[100005], n, k;

double solve(int i, int k1, int k2, double p, int mask)
{
	if(i == n)
	{
		if(k1 == k / 2 && k2 == k / 2)
			return p;
		return 0;
	}
	double res = 0;
	if(mask & (1 << i))
	{
		res += solve(i + 1, k1 + 1, k2, p * a[i] / 100.0, mask);
		res += solve(i + 1, k1, k2 + 1, p * (1.0 - a[i] / 100.0), mask);
	}
	else
	{
		res += solve(i + 1, k1, k2, p, mask);
	}
	return res;
}

double brute()
{
	double res = 0;
	for(int mask = 0; mask < (1 << n); mask++)
	{
		int cnt = 0;
		for(int j = 0; j < n; j++)
			if(mask & (1 << j))
				cnt++;
		if(cnt == k)
			res = max(res, solve(0, 0, 0, 1, mask));
	}
	return res;
}

int main()
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-attempt1.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		scanf("%d %d", &n, &k);
		for(int i = 0; i < n; i++)
		{
			int x, y;
			scanf("%d.%d", &x, &y);
			a[i] = x * 100 + y;
		}
		sort(a, a + n);
		double p1 = 1, p2 = 1;
		int cnt50 = 0;
		int L = k / 2 - 1;
		int R = n - k / 2;
		int x = 0;
		if(a[L] == 50 && a[R] == 50)
		{
			while(L >= 0 && a[L] == 50)
			{
				cnt50++;
				L--;
				x++;
			}
			while(R < n && a[R] == 50)
			{
				cnt50++;
				R++;
			}
		}
		for(int i = 0; i <= L; i++)
			p1 *= (100.0 - a[i]) / 100.0;
		for(int i = R; i < n; i++)
			p2 *= a[i] / 100.0;
		int nn = n;
		if(cnt50 > 0)
		{
			for(int i = x + 1; i <= cnt50; i++)
			{
				int j = i;
				while(n > 0 && j % 2 == 0)
				{
					j /= 2;
					n--;
				}
				p1 *= j;
			}
			while(n > 0)
			{
				p1 /= 2;
				n--;
			}
		}
		n = nn;
		//printf("Case #%d: %.10lf %.10lf\n", t, p1 * p2, brute());
		printf("Case #%d: %.10lf\n", t, brute());
	}
	return 0;
}