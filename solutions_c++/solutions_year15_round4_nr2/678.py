#pragma warning(disable:4996)
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <utility>
#include <vector>
#include <queue>
#include <set>
#include <map>
using namespace std;
#define mp make_pair
#define maxn 105
#define inf 0x3f3f3f3f
#define LL __int64
#define pr pair<LL,LL>
#define eps 1e-10
struct node
{
	double v,x;
}a[maxn];
int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);
	int t,cas = 0;
	cin>>t;
	int n;
	double v,x,vv,xx;
	while(t--)
	{
		cin>>n>>v>>x;
		for (int i = 0; i < n; i++)
		{
			scanf("%lf %lf",&vv,&xx);
			a[i].v = vv;
			a[i].x = xx;
		}
		double ans = 0;
		bool fail = 0;
		if(n == 1)
		{
			if(fabs(a[0].x-x)<eps)
				ans = v/a[0].v;
			else
				fail = 1;
		}
		else if(n==2)
		{
			if(a[0].x<x && a[1].x<x)
				fail = 1;
			else if(a[0].x>x && a[1].x>x)
				fail = 1;
			else if(fabs(a[0].x-x)<eps || fabs(a[1].x-x)<eps)
			{
				if(fabs(a[0].x-x)<eps && fabs(a[1].x-x)<eps)
				{
					ans = v/(a[0].v+a[1].v);
				}
				else if(fabs(a[0].x-x)<eps)
				{
					ans = v/a[0].v;
				}
				else
				{
					ans = v/a[1].v;
				}
			}
			else
			{
				double v1 = v*(x-a[1].x)/(a[0].x-a[1].x);
				ans = max(v1/a[0].v,(v-v1)/a[1].v);
			}
		}
		printf("Case #%d: ",++cas);
		if(fail)puts("IMPOSSIBLE");
		else printf("%.10lf\n",ans);
	}
	return 0;
}