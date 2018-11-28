#include <stdio.h>

int t;
double c,f,x;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&t);
	for(int ncase=1;ncase<=t;++ncase)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		double ans=0,t1,t2,a=2;
		while(1)
		{
			t1 = x/a;
			t2 = c/a+x/(a+f);
			if(t1<=t2)
			{
				ans += t1;
				break;
			}
			ans += c/a;
			a += f;
		}
		printf("Case #%d: %.7f\n",ncase,ans);
	}
	return 0;
}