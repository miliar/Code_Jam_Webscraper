#include<stdio.h>
#define inf 1e9
double c, f, x,dp,cnt;
double fun ( double a )
{
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,o=0;
	scanf("%d", &t );
	while ( t-- )
	{
		double ans = inf;
		scanf("%lf%lf%lf", &c,&f,&x);
		double a=0.0,dp=0,cnt=2.0,ko=0;
		for (;;)
		{
			ko=x/cnt+dp;
			if(ans>ko)
			ans=ko;
			else
			break;
			dp+=c/cnt;
			cnt+=f;
		}
		printf("Case #%d: %0.7lf\n",++o,ans);  
	}
}
