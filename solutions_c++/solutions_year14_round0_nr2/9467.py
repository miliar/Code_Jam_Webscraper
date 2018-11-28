# include <stdio.h>

double x, f, c;
int tc;

int main()
{
	// freopen("a.txt", "r", stdin);
	// freopen("b.txt", "w", stdout);

	scanf("%d", &tc);

	for (int p = 0; p < tc; p ++)
	{
		printf("Case #%d: ", p + 1);

		scanf("%lf%lf%lf", &c, &f, &x);

		double cur = c / 2 + x / (2 + f);
		double goal = x / 2;
		double delta = c / 2;

		int n = 1;

		while (cur < goal)
		{
			goal = cur;
			delta += c / (2 + n * f);
			n ++;
			cur = delta + x / (2 + n * f);

			// printf("%.7lf %.7lf %.7lf", delta, cur, goal);
		}

		printf("%.7lf\n", goal);
	}
}