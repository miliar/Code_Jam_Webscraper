#include <cstdio>

int main(int argc, char const *argv[])
{
	int t;
	double c, f, x, rate, cookies, res, temp;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i)
	{
		cookies = 0.0;
		res = 0.0;
		rate = 2.0;
		scanf("%lf%lf%lf", &c, &f, &x);
		if(x <= c)
		{
			temp = x/rate;
		}
		else
		{
			temp = (x/rate);
			while(1)
			{
				res += (c/rate);
				rate += f;
				if((res + (x/rate)) > temp)
					break;
				temp = res + (x/rate);
			}
		}
		printf("Case #%d: %.7lf\n", i, temp);
	}
	return 0;
}