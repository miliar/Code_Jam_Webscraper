#include <stdio.h>
int main()
{
	int t,k;
	scanf("%d",&t);
	k=t;
	while(t--)
	{
		double c,f,x,ans=0.0,cf;
		scanf("%lf %lf %lf",&c,&f,&x);
		cf=2.0;
		while(true)
		{
			if(x/cf<c/cf+x/(cf+f))
			{
				ans=ans+x/cf;break;
			}
			else
			{
				ans=ans+c/cf;
				cf+=f;
			}
		}
		printf("Case #%d: %.6lf\n",k-t,ans);
	}
	return 0;
}
