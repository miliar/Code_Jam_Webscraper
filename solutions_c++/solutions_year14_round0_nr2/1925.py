#include <stdio.h>

double c,f,x;

int main()
{
	int T;
	int ca = 1;
	int i,j;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		double ans = x/2;
		double t = 0;
		for(int i=1;i<=x;i++)
		{
			t += c/((i-1)*f+2);
			if( t > ans ) break;
			if( t + x/(i*f+2) < ans ) ans = t + x/(i*f+2);
		}
		printf("Case #%d: %.7f\n",ca++,ans);
	}
	return 0;
}

