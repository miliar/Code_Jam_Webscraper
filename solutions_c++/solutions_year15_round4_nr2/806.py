#if 0==0

#include<stdio.h>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
	
	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
	//freopen("B-large-practice.in", "r", stdin);
	//freopen("B-large-practice.out", "w", stdout);
	//freopen("B-large.in", "r", stdin);
	//freopen("B-large.out", "w", stdout);
	

	int T;
	
	scanf("%d", &T);
	for (int i_case = 1 ; i_case <= T ; i_case++)
	{		
		int n;

		double v, x;
		double r[101], c[101], t[101];
		double ans;
		bool ok = true;

		scanf("%d%lf%lf", &n, &v, &x);

		if (n == 1)
		{
			scanf("%lf%lf", &r[0], &c[0]);

			if (c[0] == x)
			{
				ans = v/r[0];
			} else
			{
				ok = false;
			}
		} else
		if (n == 2)
		{
			scanf("%lf%lf", &r[0], &c[0]);
			scanf("%lf%lf", &r[1], &c[1]);

			if (c[0] < x - 1e-9 && c[1] < x - 1e-9) ok = false;
			if (c[0] > x + 1e-9 && c[1] > x + 1e-9) ok = false;

			if (fabs(c[0] - c[1]) < 1e-9)
			{
				if (fabs(c[0] - x) < 1e-9)
					ans = v/(r[0]+r[1]);
				else
					ok = false;
			} else
			{		
				c[0] -= x;
				c[1] -= x;

				t[0] = v * c[1]/(r[0]*(c[1] - c[0]));
				t[1] = v * c[0]/(r[1]*(c[0] - c[1]));

				ans = max(t[0], t[1]);
			}
		}

		printf("Case #%d: ", i_case);

		if (ok)
			printf("%.9f\n", ans);
		else
			printf("IMPOSSIBLE\n");
	}

	return 0;
}

#endif