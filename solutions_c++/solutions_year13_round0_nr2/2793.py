/*Author : Vineet Kumar */
#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<climits>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<bitset>
#include<stack>
#include<queue>
using namespace std;

#define FOR(i,a,b) 	for(int i= (int )a ; i < (int )b ; ++i)
#define rep(i,n) 	FOR(i,0,n)
#define INF		INT_MAX
#define ALL(x) 		x.begin(),x.end()
#define LET(x,a)	__typeof(a) x(a)
#define IFOR(i,a,b) 	for(LET(i,a);i!=(b);++i)
#define EACH(it,v) 	IFOR(it,v.begin(),v.end())
#define pb 		push_back
#define sz(x) 		int(x.size())
#define mp 		make_pair
#define fill(x,v)	memset(x,v,sizeof(x))
#define max(a,b)	((a)>(b)?(a):(b))
#define min(a,b)	((a)<(b)?(a):(b))
#define	si(n)		scanf("%d",&n)
#define pi(n)		printf("%d ",n)
#define pil(n)		printf("%d\n",n)
#define sl(n)		scanf("%lld",&n)
#define sd(n)		scanf("%lf",&n)
#define ss(n)		scanf("%s",n)
#define scan(v,n)	vector<int> v;rep(i,n){ int j;si(j);v.pb(j);}
#define mod (int)(1e9 + 7)
typedef pair<int,int> PI;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;
int n,m;
int g[11][11],ans[11][11],done[11][11];
int check(int c,int x)
{
	if(c==0)
	{
		FOR(i,1,m)
			if(g[x][i]!=g[x][0])
				return 0;
		return 1;
	}
	else
	{
		FOR(i,1,n)
			if(g[i][x]!=g[0][x])
				return 0;
		return 1;
	}
}
int main()
{
	int i,j,t,x,test = 1,y;
	for(si(t);t--;)
	{
		printf("Case #%d: ",test++);
		si(n);
		si(m);
		rep(i,n)
			rep(j,m)
			{
				si(g[i][j]);
				ans[i][j] = 2;
				done[i][j] = 0;
			}
		rep(i,n)
			rep(j,m)
			{
				if(done[i][j])
					continue;
				if(g[i][j] == 1)
				{
					x = check(0,i);
					if(x)
					{
						rep(k,m)
						{
							ans[i][k] = g[i][j];
							done[i][k] = 1;
						}
					}
					else
					{
						y = check(1,j);
						if(y)
						{
							rep(k,n)
							{
								ans[k][j] = g[i][j];
								done[k][j] = 1;
							}
						}
					}
				}
			}
		int flag = 0;
		rep(i,n)
		{
			rep(j,m)
			{
				if(ans[i][j] != g[i][j])
				{
					flag = 1;
					break;
				}
			}
			if(flag)
				break;
		}
		if(flag)
			printf("NO\n");
		else
			printf("YES\n");
	}
	return 0;
}

