#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
using namespace std;
vector<pair<double, int> > v;
int t, n;

int calc1()
{
	int ret = 0;
	for (int i = 0; i < n + n; i++)
	{
		if (v[i].second == 1)
			ret++;
		else if (ret > 0)
			ret--;
	}
	return n - ret;
}

int calc2()
{
	int ret = 0;
	for (int i = 0; i < n + n; i++)
	{
		if (v[i].second == 0)
			ret++;
		else if (ret > 0)
			ret--;
	}
	return ret;
}

int main()
{
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		v.clear();
		scanf("%d", &n);
		double m;
		for (int i = 0; i < n; i++)
		{
			scanf("%lf", &m);
			v.push_back(make_pair(m, 0));
		}
		for (int i = 0; i < n; i++)
		{
			scanf("%lf", &m);
			v.push_back(make_pair(m, 1));
		}
		sort(v.begin(), v.end());
		printf("Case #%d: %d %d\n", tt, calc1(), calc2());
	}
	return 0;
}
