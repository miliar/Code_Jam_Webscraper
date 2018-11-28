#include<stdio.h>
int main()
{
	double c,f,x,i,res=0.0,rate;
	int t,j;
	scanf("%d",&t);
	for(j=1;j<=t;j++)
	{
		res=0.0;
		scanf("%lf%lf%lf",&c,&f,&x);
		i=c/f;
		rate=2.0;
		while(1)
		{
			if(((rate*i)+c)>x)
			break;
			else
			{
				res+=c/rate;
				rate+=f;
			}
		}
		//rate-=f;
		res+=x/rate;
		printf("Case #%d: %0.7lf\n",j,res);
	}
	return 0;
}
