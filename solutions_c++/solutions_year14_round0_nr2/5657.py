#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <iostream>

using namespace std;

typedef long long big;

double C,F,X;
int main()
{
	int x,y,cas,cass,i,j;
	double now,ans;
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&cas);
	for(cass=1;cass<=cas;cass++)
	{
		scanf("%lf%lf%lf",&C,&F,&X);
		ans=2e9;
		now=0;
		for(i=0;i<=100000;i++)
		{
			ans=min(ans,now+X/(i*F+2));
			now+=C/(i*F+2);
		}
		printf("Case #%d: ",cass);
		printf("%.7f\n",ans);
	}
}
