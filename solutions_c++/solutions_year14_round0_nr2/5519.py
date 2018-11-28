#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;

const double INF = 1e18;

const int T = (int)2e5;

double solve()
{
 	double c, f, x;
 	scanf("%lf%lf%lf", &c, &f, &x);

	double speed = 2.0;
	double cur_time = 0.0;
	double best_time = INF;

	for (int i = 0; i < T; i++)
	{
	 	best_time = min(best_time, cur_time + x / speed);
	 	cur_time += (c / speed);
	 	speed += f;
	}

	return best_time;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#endif

	int it;
	scanf("%d", &it);
	for (int i = 0; i < it; i++)
	{
	 	printf("Case #%d: %.10lf\n", i + 1, solve());
	}


 	return 0;
}