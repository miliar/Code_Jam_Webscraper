/*	Jayesh Lahori	    */
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<set>

using namespace std;

/* General Declarations */

#define INF		1000000007
#define LL		long long int
#define SI(n)		scanf("%lld",&n);
#define SC(c)		scanf("%c",&c);
#define SS(s)		scanf("%s",s);
#define FOR(x,a,b)	for(LL x=a;x<b;x++)
#define REP(i,n)	for(LL i=0;i<n;i++)
#define MP		make_pair
#define PB		push_back


/* Container's */

#define	VI		vector<LL>
#define PLL             pair<LL,LL>  /* A Single Pair  */
#define VP		vector<PLL> /* Vector of Pairs */
#define VS		vector<string>
#define VVI		vector<VI>
#define VVS		vector<VS>

int main()
{
	LL tc;
	SI(tc);
	LL cpy=tc;
	while(tc--)
	{
		LL r,t,j,y;
		LL ans=0;
		SI(r);
		SI(t);
		j=0;
		LL ct=0;
		while(1)
		{
			y= (((r+1+j)*(r+1+j)) - ((r+j)*(r+j)));
			if(y<=t)
			{
				ans=ans+y;
				j+=2;
				t-=y;
				ct++;
			}
			else
				break;
		}
		printf("Case #%lld: %lld\n",cpy-tc,ct);
	}
	return 0;
}
