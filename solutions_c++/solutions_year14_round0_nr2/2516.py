#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
#include<string>
#include<vector>
#include<cmath>
#include<queue>
#include<map>
#include<set>
using namespace std;
#define INF 1000000000
//typedef __int64 LL;
int t;
double c,f,x;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	int time=0;
	while(t--)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		double ans=0,spe=2.0,sum=0;
		while(1)
		{
			double f1,f2;
			double tmp=x-sum;
			if(tmp<=c)
			{
				ans+=(tmp/spe); break;
			}
			f1=tmp/spe;
			f2=c/spe;
			spe+=f;
			f2+=x/spe;
			if(f1<f2)
			{
				ans+=f1; break;
			}
			else
			{
				ans+=(c/(spe-f));
			}
		}
		printf("Case #%d: ",++time);
		printf("%.7lf\n",ans);
	}


    return 0;
}
