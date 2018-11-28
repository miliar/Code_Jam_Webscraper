#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif
#include<stdio.h>
void main()
{
	//freopen("B-small-attempt0.in","r",stdin);
	//freopen("B-small-attempt0.out","w",stdout);
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;t++)
	{
		double C, F, X, time, min;
		int n;
		scanf("%lf %lf %lf",&C,&F,&X);
		min=X/2;
		for(n=1;;n++)
		{
			time=C/2;
			for(int i=0;i<n-1;++i)
				time+=(C/(2+F*(i+1)));
			time+=(X/(2+F*n));
			if(time<min)
				min=time;
			else
				break;
		}
		printf("Case #%d: %.7f\n",t+1,min);
	}
}