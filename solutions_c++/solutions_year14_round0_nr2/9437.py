#include<cstdio>
#define eps 1e-8
double c,f,x;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;
	scanf("%d",&test);
	for(int tt=1;tt<=test;tt++)
	{
		printf("Case #%d: ",tt);
		scanf("%lf%lf%lf",&c,&f,&x);
		double t=0,per=2;
		double ans=x/per;
		while(1)
		{
			double tmp=t+c/per+x/(per+f);
			if(tmp>ans+eps)break;
			ans=tmp;
			t+=c/per;
			per+=f;
		}
		printf("%.7f\n",ans);
	}
	return 0;
}
