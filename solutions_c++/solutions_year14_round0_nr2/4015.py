#include<stdio.h>

int main()
{
	int t,c=1;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&t);
	while(t)
	{
		double C,F,X,rate=2.00000000,ans=0.000000000;
		scanf("%lf %lf %lf", &C, &F, &X);
		while(1)
		{
			if((C/rate)+(X/(rate+F))>(X/rate))
			{
				ans += X/rate;
				break;
			}
			else
			{
				ans += C/rate;
				rate+=F;
			}
		}
		printf("Case #%d: %.7f\n",c,ans);
		t--;
		c++;
	}
	return 0;
}