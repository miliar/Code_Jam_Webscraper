#include<stdio.h>

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out_bl.txt","w",stdout);
	int t,m;
	double c,f,x,a,total;
	scanf("%d",&t);
	for(m=1;m<=t;++m)
	{
		scanf("%lf %lf %lf",&c,&f,&x);
		a=2;
		total=0;
		while(1)
		{
			if(x/a<=(c/a+x/(a+f)))
			{
				total+=x/a;
				break;
			}
			else
			{
				total+=c/a;
				a+=f;
			}
		}
		printf("Case #%d: %.7f\n",m,total);
	}
	return 0;
}