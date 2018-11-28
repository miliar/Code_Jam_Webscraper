#include<iostream>

using namespace std;

int ca,num;
double c,f,x;
void init()
{
	scanf("%d",&num);
	while (num--)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		double ans=x/2.0, abi=2,t=0;
		for (int i=1; i<=x; i++)
		{
			t+=c/abi;
			abi+=f;
			ans=min(ans,t+x/abi);
		}
		printf("Case #%d: %.7lf\n",++ca,ans);
	}
}
int main()
{
	init();
	return 0;
}
