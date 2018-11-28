#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <map>
#include <set>
#include <assert.h>

using namespace std;

typedef long long ll;
#define mp make_pair
#define mt(a, b, c) mp(a, mp(b, c))

const int FARMS = 100010;

double t[FARMS];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	t[0] = 0;
	scanf("%d", &tests);
	for (int q = 0; q < tests; q++)
	{
		double c, f, x;
		double ans = 1e7;
		scanf("%lf %lf %lf", &c, &f, &x);
		for (int i = 1; i < FARMS; i++)
			t[i] = t[i - 1] + c / (2.0 + (i - 1) * f);
		for (int i = 0; i < FARMS; i++)
		{
			double cur = t[i] + x / (2 + i * f);
			ans = min(cur, ans);
		}
		printf("Case #%d: %.10lf\n", q + 1, ans);
	}
	return 0;
}