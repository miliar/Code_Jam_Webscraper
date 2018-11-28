#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

const double eps = 1e-10;

class pipe
{
public:
	double r, c;
};
double v, x;
pipe p[110];
bool succ;
int n;

bool cmp1(const pipe &a, const pipe &b)
{
	return a.c < b.c;
}

bool cmp2(const pipe &a, const pipe &b)
{
	return a.c > b.c;
}

double getmin(double t)
{
	sort(p, p + n, cmp1);
	double curV = 0, ret = 0;
	for(int i = 0; i < n; ++i)
	{
		if(curV + p[i].r * t >= v)
		{
			ret = (curV * ret + (v - curV) * p[i].c) / v;
			return ret;
		}
		else
		{
			ret = (curV * ret + (p[i].r * t) * p[i].c) / (curV + p[i].r * t);
			curV += p[i].r * t;
		}
	}
	return 1e100;
}

double getmax(double t)
{
	sort(p, p + n, cmp2);
	double ret = 0;
	double curV = 0;
	for(int i = 0; i < n; ++i)
	{
		if(curV + p[i].r * t >= v)
		{
			ret = (curV * ret + (v - curV) * p[i].c) / v;
			return ret;
		}
		else
		{
			ret = (curV * ret + (p[i].r * t) * p[i].c) / (curV + p[i].r * t);
			curV += p[i].r * t;
		}
	}
	return -1e100;
}

bool check(double t)
{
	double mn = getmin(t), mx = getmax(t);
	if(mn - eps < x && mx + eps > x)
	{
		succ = true;
		return true;
	}
	return false;
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int cas = 1; cas <= T; ++cas)
	{
		succ = false;
		scanf("%d", &n);
		scanf("%lf%lf", &v, &x);
		double mxTime = 0;
		for(int i = 0; i < n; ++i)
		{
			scanf("%lf%lf", &p[i].r, &p[i].c);
			mxTime = max(mxTime, v / p[i].r);
		}
		double l = 0, r = 1e12;
		int cnt = 0;
		while(cnt < 300)
		{
			double mid = (l + r) / 2;
			if(check(mid))
				r = mid;
			else
				l = mid;
			cnt++;
		}
		printf("Case #%d: ", cas);
		if(!succ)
			printf("IMPOSSIBLE\n");
		else
			printf("%.9f\n", (double)l);
	}
	return 0;
}
