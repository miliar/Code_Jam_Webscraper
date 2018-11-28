#include <iostream>
#include <algorithm>
#include <queue>
#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

#define N 600
#define inf 0x3f3f3f3f
#define eps 1e-8
#define ll long long

int cnt[17];
int main()
{
	freopen("a.out","w",stdout);
	freopen("a.in","r",stdin);
	int T,cas=0,a,x;
	cin>>T;
	while (T--)
	{
		double C,F,X;
		scanf("%lf%lf%lf",&C,&F,&X);
		double v=2,t=0;
		double ans=X/v;
		for (int i=1;;i++)
		{
			t+=C/v;
			v+=F;
			if (t+X/v<ans) ans=t+X/v;
			else break;
		}
		printf("Case #%d: %.7lf\n",++cas,ans);
	}
}