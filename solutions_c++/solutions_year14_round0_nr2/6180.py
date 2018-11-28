#include <cstdio>
int main()
{
	int T;
	int tt = 1;
	scanf("%d", &T);
	while(T--)
	{
		double C, F, X;
		scanf("%lf %lf %lf", &C, &F, &X);
		double prod = 2.0;
		double nowT = 0.0;
		for(int i = 1 ; ; i++)
		{
			double ed1 = X/prod;
			double ed2 = C/prod+X/(prod+F);
			if(ed1 < ed2)
			{
				printf("Case #%d: %.7f\n", tt, nowT+ed1);
				break;
			}
			else
			{
				nowT += C/prod;
				prod += F;	
			}
		}
		tt++;
	}
	return 0;
}
