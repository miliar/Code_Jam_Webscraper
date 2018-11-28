#include<stdio.h>

double x,c,f,startf=2.0000000,sec=0.000000,ans=1000000000000.000000;

int main()
{
	int i,j,k,n=100100,q;
	scanf("%d",&q);
	for(k=1;k<=q;k++)
	{
		ans=1000000000000.00000;
		scanf("%lf %lf %lf",&c,&f,&x);
		for(i=0;i<n;i++)
		{
			sec=0.0000000;
			startf=2.0000000;
			for(j=0;j<i;j++)
			{
				sec+=c/startf;
				startf+=f;
			}
			sec+=x/startf;
			if(sec<ans)
				ans=sec;
			else
				break;
		}
		printf("Case #%d: %.7lf\n",k,ans);
	}
	
}
