#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<time.h>
#include<string>
#include<set>
#include<map>
#include<vector>
#include<algorithm>
#include<iostream>
#include<queue>
using namespace std;




int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);

	double eps = 0.0000001;
	int TT;
	scanf("%d", &TT);
	for (int T = 0; T < TT; T++)
	{
		printf("Case #%d: ", T + 1);

		int n;
		scanf("%d", &n);
		double v, t;
		scanf("%lf%lf", &v, &t);
		double s0, t0, s1, t1;
		scanf("%lf%lf", &s0, &t0);
		if (n == 1)
		{
			if (fabs(t - t0) > eps)
				printf("IMPOSSIBLE\n");
			else
				printf("%.9lf\n", v / s0);
			continue;
		}
		scanf("%lf%lf", &s1, &t1);
		if (t - t0 > eps && t - t1 > eps ||
			t - t0 < -eps && t - t1 < -eps)
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		if (fabs(t1 - t0) < eps)
		{
			if (s0 < s1)
				swap(s0, s1);
			printf("%.9lf\n", v / (s0 + s1));
			continue;
		}
		double v1 = v * (t - t0) / (t1 - t0), v0 = v - v1;
		printf("%.9lf\n", max(v0 / s0, v1 / s1));
	}

	return 0;
}