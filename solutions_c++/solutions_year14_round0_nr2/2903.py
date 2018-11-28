#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
	int tc,t;
	double ans,r,time,y,c,f,X;
	for(scanf("%d",&tc),t=1;t<=tc;t++)
	{
		ans=100000000.0;
		scanf("%lf%lf%lf\n",&c,&f,&X);
		r=2.0;				// rate
		time=0;				// time until now
		for(int i=0;i<=5000000;i++)
		{
			y=(time+X/r);
//			printf("y=%lf t=%lf\n",y,X/r);
			ans=min(ans,y);
			time=time+c/r;
			r+=f;
			if(time>=(X/2))
				break;
		}
		printf("Case #%d: %0.8lf\n",t,ans);
	}
	return 0;
}