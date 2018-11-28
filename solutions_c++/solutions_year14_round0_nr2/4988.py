#include<stdio.h>
int main()
{
	int n;
	double C,F,X;
	double P;
	double T;
	double tc,txOld,txNew;
	int m;
	int i,j;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		P=2.0;
		T=0.0;
		scanf("%lf %lf %lf",&C,&F,&X);
		txNew=X/P;
		for(j=0;j<100000;j++)
		{
			tc=C/(P+F*j);
			txOld=txNew;
			txNew=X/(P+F*(j+1));
			if(tc+txNew>txOld)
			{
				break;
			}
			T+=tc;
		}
		T+=txOld;
		printf("Case #%d: %.7lf\n",i+1,T);
	}
	return 0;
}