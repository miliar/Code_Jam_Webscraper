#include<cstdio>

int main()
{
	int t;
	scanf("%d",&t);
	for(int k=0;k<t;k++)
	{
		double c,f,x,speed=2.0;
		scanf("%lf %lf %lf",&c,&f,&x);
		double ans=0;
		double a1,a2=x/speed;
		while(1)
		{
			a1=a2;
			a2=ans+c/speed+x/(speed+f);
			if(a1<=a2)
				break;
			else
			{
				ans+=c/speed;
				speed+=f;
			}
		}
		ans+=x/speed;
		printf("Case #%d: %.7lf\n",k+1,ans);
	}
	return 0;
}
