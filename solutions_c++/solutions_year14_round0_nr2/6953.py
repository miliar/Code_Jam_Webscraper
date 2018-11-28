#include <stdio.h>
int	test_case;
double c,f,x,ans;
int main()
{
	int i;
	double f2;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&test_case);
	for(i=1;i<=test_case;i++)
	{
		scanf("%lf %lf %lf",&c,&f,&x);
		f2=2.0;
		ans=0.0;
		while(1)
		{
			if(x*(f2+f) > c*(f2+f)+x*f2) // x/f2 > c/f2 + x/(f2+f)
			{
				ans+=c/f2;
			}
			else
				break;
			f2+=f;
		}
		ans+=x/f2;
		printf("Case #%d: %.7lf\n",i,ans);
	}
	return 0;
}