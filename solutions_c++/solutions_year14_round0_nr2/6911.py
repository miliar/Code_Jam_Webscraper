#include <iostream>
#include <algorithm>
using namespace std;

const int ITER = 150;

double c, f, x;

bool can(double t)
{
	double v = 2;
	double cur_t = 0;

	while (true)
	{
		if ((t - cur_t) * v >= x)
			return true;

		double next_t = cur_t + c / v;
		if (next_t > t)
			break;

		double payback_t = next_t + c / (v + f);
		if (payback_t > t)
			break;

		cur_t = next_t;
		v += f;
	}

	double cnt = (t - cur_t) * v;
	return cnt >= x;
}

void solve()
{
	scanf("%lf%lf%lf", &c, &f, &x);

	double L = 0, R = 1e5;
	for (int i = 0; i < ITER; i++)
	{
		double M = (L + R) / 2;
		if (can(M))
			R = M;
		else
			L = M;	
	}

	printf("%.10lf\n", R);
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int t;
	scanf("%d", &t);

	for (int i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}

	return 0;	
}