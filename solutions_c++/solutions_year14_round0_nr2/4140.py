#include <stdio.h>

int main()
{
	int T;

	scanf("%d", &T);
	for( int t=1; t<=T; t++ )
	{
		double c, f, x;
		scanf("%lf %lf %lf", &c, &f, &x);

		double r = 2, ans = 0;
		for( ; c/r+x/(f+r) < x/r; )
		{
			ans += c / r;
			r += f;
		}
		ans += x / r;

		printf("Case #%d: %.7lf\n", t, ans);
	}
	return 0;
}

