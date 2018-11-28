#include <cstdio>
#include <cstring>

int main()
{
	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; ++t)
	{
		double c, f, x;
		scanf("%lf%lf%lf", &c, &f, &x);

		double ans = x / 2;
		double nf = 2;
		double nt = 0;
		for (; ;)
		{
			nt += c / nf;
			nf += f;
			double tmp = nt + x / nf;
			if (tmp > ans)
				break;
			ans = tmp;
		}
		printf("Case #%d: %.7lf\n", t, ans);
	}

	return 0;

}
