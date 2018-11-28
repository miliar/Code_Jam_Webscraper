#include <stdio.h>
const double eps = 1e-6;


int main()
{
	int t, cnt;
	double c, f, x;
	double ans, tmp, r;
	
	scanf("%d", &t);
	for (cnt = 1; cnt <= t; cnt++)
	{
		scanf("%lf %lf %lf", &c, &f, &x);
		
		r = 2;
		ans = 0;

		while ((c/r + x/(r+f)) <= x/r)
		{
			ans += c/r;
			r += f;
		} 
		ans += x / r;
	
		printf("Case #%d: %.7f\n", cnt, ans);
	}
	return 0;
}
