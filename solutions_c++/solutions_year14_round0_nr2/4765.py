#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <float.h>

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int n_case;
double c, f, x, best;

void solve()
{
	for (int i = 0; ; i++)
	{
		double time = 0.0;
		double rate = 2.0;
		for (int k = 1; k <= i; k++)
		{
			time += c / rate;
			rate += f;
		}
		time += x / rate;

		if (best - time >= 0.0)
			best = time;
		else break;
	}
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("B-small-attempt1.in", "r", stdin);
	//freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	while(scanf("%d", &n_case) != EOF)
	{
		for (int t = 0; t < n_case; t++)
		{
			/// init
			best = INFINITY;
			/// read
			scanf("%lf%lf%lf", &c, &f, &x);
			/// calc
			solve();
			printf("Case #%d: %.7f\n", t+1, best);
		}
	}

	return 0;
}
