#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>


using namespace std;


double timee[1000000];


double oldGetTime(double c, double f, double x, int n)
{
	double speed = 2;
	double ans = 0;
	for(int i = 0; i < n; i++)
	{
		ans += c / speed;
		speed += f;
	}
	return ans + x / speed;
}


double getTime(double c, double f, double x, int n)
{
	double speed = 2 + n * f;
//	double ans = 0;
//	for(int i = 0; i < n; i++)
//	{
//		ans += c / speed;
//		speed += f;
//	}
//	double res = ans + x / speed;
	return timee[n] + x / speed;
}


int sum = 0;
int ff[1000146];


void solve(int ts)
{
	double c, f, x;
	scanf("%lf%lf%lf", &c, &f, &x);
	int l = 0;
	int r = max(x / f + 1046, x / c + 1046);
	timee[0] = 0;
	for(int i = 1; i <= r; i++)
	{
		timee[i] = timee[i - 1] + c / (2 + f * (i - 1));
		//fprintf(stderr, "%lf ", timee[i]);
	}
//	for(int i = 0; i < 10; i++)
//	{
//		fprintf(stderr, "%lf vs %lf\n", getTime(c, f, x, i), oldGetTime(c, f, x, i));
//	}
//	exit(0);
	while(r - l > 5)
	{
		int m1 = (2 * l + r) / 3;
		int m2 = (l + 2 * r) / 3;
		double f1 = getTime(c, f, x, m1);
		double f2 = getTime(c, f, x, m2);
		if(f1 < f2)
			r = m2;
		else
			l = m1;
	}
	double res = getTime(c, f, x, 0);
	for(int i = l; i <= r; i++)
		res = min(res, getTime(c, f, x, i));
	printf("Case #%d: %.7lf\n", ts, res);
}


int main()
{
	freopen("B-large.in","r",stdin);
//	freopen("B-small-attempt3.in","r",stdin);
	//freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int t;
	scanf("%d", &t);
	for(int i = 0; i < t; i++)
		solve(i + 1);
	fprintf(stderr, "%d\n", sum);
}