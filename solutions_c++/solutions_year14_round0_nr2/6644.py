#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;

int T;
double C,F,X;

double solve()
{
	if(X<C)return X/2.0;

	double rate=2.0;
	double ans=-1.0;
	double Time=0.0;
	for(int i=0;i<100000;i++)
	{
		double tmp1=Time+C/rate+X/(rate+F);
		double tmp2=Time+X/rate;
		if(tmp1<=tmp2)
		{
			Time=Time+C/rate;
			rate+=F;
		}else
		{
			ans=tmp2;
			break;
		}
	}
	return ans;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int idx=1;idx<=T;idx++)
	{
		scanf("%lf %lf %lf",&C,&F,&X);
		printf("Case #%d: %.7lf\n",idx,solve());
	}
	return 0;
}
