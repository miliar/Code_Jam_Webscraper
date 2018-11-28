#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <cassert>
#include <numeric>
#include <string>
#include <cstring>
#include <cmath>
using namespace std;

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) 42
#endif

typedef long long int int64;

bool eq(double a, double b)
{
	return fabs(a - b) < 1e-9;
}

bool ls(double a, double b)
{
	return a < b && !eq(a, b);
}

vector<pair<double, double> >  fix(vector<pair<double, double> > list)
{
	vector<pair<double, double> > res;
	sort(list.begin(), list.end());
	for (auto p : list)
	{
		if (res.empty() || !eq(res.back().first, p.first))
			res.push_back(p);
		else
			res.back().second += p.second;
	}
	return res;
}

void fail(int test)
{
	printf("Case #%d: IMPOSSIBLE\n", test);
}

void suc(int test, double a)
{
	printf("Case #%d: %.10lf\n", test, a);
}

void solve(int test)
{
	int n;
	scanf("%d", &n);
	double v, x;
	scanf("%lf%lf", &v, &x);
	vector<pair<double, double> > list(n);
	for (int i = 0; i < n; i++)
		scanf("%lf%lf", &list[i].second, &list[i].first);
	list = fix(list);

	if (list.size() == 1)
	{
		if (!eq(list[0].first, x))
		{
			fail(test);
			return;
		}
		double ans = v / list[0].second;
		suc(test, ans);
		return;
	}

	double v1 = v * (x - list[1].first) / (list[0].first - list[1].first);
	double v2 = v - v1;

	if (ls(v1, 0) || ls(v2, 0))
		fail(test);
	else
		suc(test, max(v1 / list[0].second, v2 / list[1].second));
}

int main()
{
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
#endif

	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
		solve(i + 1);

	return 0;
}
