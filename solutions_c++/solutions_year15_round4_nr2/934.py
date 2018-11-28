#include<string>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<map>
#include<vector>
#include<iostream>
#include<deque>
#include<queue>
#include<set>
#pragma comment(linker, "/STACK:102400000,102400000")
#define LL __int64
#define eps 1e-10
#define zero(x) ((x > +eps) - (x < -eps))
#define mem(a,b) memset(a,b,sizeof(a))
#define MOD 1000000007
#define INF 99999999
#define MAX 110
using namespace std;

struct NODE
{
	double v, c;
	bool operator < (const struct NODE & a )const
	{
		return c < a.c;
	}
}nodes[MAX];

int n;
double v, c;

int main()
{
	freopen("B-small-attempt2.in","r",stdin);
	freopen("B-small-attempt2.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int ii = 1; ii <= t; ii ++)
	{
		scanf("%d%lf%lf",&n,&v,&c);
		for(int i = 0; i < n; i ++)
		{
			scanf("%lf%lf",&nodes[i].v,&nodes[i].c);
		}
		if(n == 1)
		{
			if(fabs(nodes[0].c - c) < eps)
			{
				printf("Case #%d: %.10lf\n",ii,v / nodes[0].v);
			}
			else
			{
				printf("Case #%d: IMPOSSIBLE\n",ii);
			}
			continue;
		}
		sort(nodes,nodes+n);
		if(zero(nodes[0].c - c) > 0)
		{
			printf("Case #%d: IMPOSSIBLE\n",ii);
			continue;
		}
		if(zero(nodes[1].c - c ) < 0)
		{
			printf("Case #%d: IMPOSSIBLE\n",ii);
			continue;
		}
		if(zero(nodes[0].c - c) == 0)
		{
			if(zero(nodes[1].c - c) == 0)
			{
				printf("Case #%d: %.10lf\n",ii,v / (nodes[0].v + nodes[1].v));
			}
			else
			{
				printf("Case #%d: %.10lf\n",ii,v / nodes[0].v);
			}
			continue;
		}
		if(zero(nodes[1].c - c) == 0)
		{
			printf("Case #%d: %.10lf\n",ii,v / nodes[1].v);
			continue;
		}
		double ans;
		double v1, v2;
		v2 = v * (c - nodes[0].c) / (nodes[1].c - nodes[0].c);
		v1 = v * (nodes[1].c - c) / (nodes[1].c - nodes[0].c);
		ans =  max(v1 / nodes[0].v,v2 / nodes[1].v);
		printf("Case #%d: %.10lf\n",ii,ans);
	}
	return 0;
}