#include <iostream>
#include <cstdio>
using namespace std;
double ans,F,C,X;
void rec(double time, double profit, double money,int test)
{
	double b=X-money;
	double t=b/double(profit);
	if(time>ans)
		return;
	ans=min(ans,time+t);
	t=0;
	b=0;
	b=C;
	t=b/profit;
	if(test>100000)
		return;
	cout<<test<<endl;
	rec(time+t,profit+F,0,test+1);

}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tt,k,i,j;
	double t,time,profit,b,c,d,e,f,g,h;
	scanf("%d",&tt);
	for(k=1;k<=tt;k++)
	{
		scanf("%lf%lf%lf",&C,&F,&X);
		ans=X/double(2);
		time=0;
		profit=2;
		for(i=1;i<=10000000;i++)
		{
			b=X;
			t=b/double(profit);
			if(time>ans)
				break;
			ans=min(ans,time+t);
			t=0;
			b=0;
			b=C;
			t=b/profit;
			time=time+t;
			profit=profit+F;
		}
		printf("Case #%d: %.7f\n",k,ans);
	}
	return 0;
}