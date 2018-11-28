#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,cas = 0;
	scanf("%d",&t);
	double C,F,X;
	while(t--)
	{
		scanf("%lf%lf%lf",&C,&F,&X);
		double nowtime = 0;
		int nowhouse = 0;
		double Mincost = X/2;
		while(1)
		{
			double p = 2+(nowhouse)*F;
			double nowcost = nowtime + C/p;
			nowtime = nowcost;
			nowhouse++;
			p += F;
			nowcost += X/p;
			if(nowcost < Mincost)
				Mincost = nowcost;
			else break;
		}
		printf("Case #%d: %.7lf\n",++cas,Mincost);
	}
	return 0;
}