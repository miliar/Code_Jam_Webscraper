#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;

int main()
{
	int t,ys;

	freopen("B-large.in","r",stdin);
	freopen("Bres2.out","w",stdout);
	scanf("%d",&t);
	ys=0;
	while (t--)
	{
		double C,F,X;
		scanf("%lf%lf%lf",&C,&F,&X);
		double speed=2.0;
		double ans=X/speed;
		double time=0;
		while (1)
		{
			time+=C/speed;
			speed+=F;
			if (ans<time+X/speed)
				break;
			ans=min(ans,time+X/speed);
		}
		printf("Case #%d: %.7f\n",++ys,ans);
	}

	return 0;
}
