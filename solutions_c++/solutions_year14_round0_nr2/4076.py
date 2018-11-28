#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int k = 1; k <= t; k++)
	{
		double c, f, x;
		scanf("%lf %lf %lf", &c, &f, &x);
		double cur = 2;
		double res = 0;
		while (x / cur > c / cur + x / (cur + f))
		{
			res += c / cur;
			cur += f;
		}
		res += x / cur;
		printf("Case #%d: %lf\n", k, res);
	}
	return 0;
}