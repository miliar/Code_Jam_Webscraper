#include <stdio.h>
#include <limits>

int main()
{
	int TT;
	scanf("%d",&TT);
	for (int tt = 1; tt <= TT; tt++)
	{
		double c,f,x;
		scanf("%lf%lf%lf",&c,&f,&x);

		double ans = std::numeric_limits<double>::max();
		double nujeok = 0.0;
		double current = 2;

		for (int i = 0; i < 1000000; i++)
		{
			if (nujeok + x / current < ans)
				ans = nujeok + x / current;

			nujeok += c / current;
			current += f;
		}

		printf("Case #%d: %.7f\n", tt, ans);
	}
}