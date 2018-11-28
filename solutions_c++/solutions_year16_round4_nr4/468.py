#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstring>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

#define SIZE(x) (int((x).size()))
#define rep(i,l,r) for (int i=(l); i<=(r); i++)
#define repd(i,r,l) for (int i=(r); i>=(l); i--)
#define rept(i,c) for (typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)

#ifndef ONLINE_JUDGE
#define debug(x) { cerr<<#x<<" = "<<(x)<<endl; }
#else
#define debug(x) {}
#endif

char g[20][20];
int can[20], op[20];

void lemon()
{
	int n; scanf("%d",&n);
	int best=100000;
	rep(i,1,n) scanf("%s",g[i]+1);
	rep(state,0,(1<<(n*n))-1)
	{
		int flag=1;
		rep(i,1,n) { can[i]=0; op[i]=0; }
		rep(i,1,n)
			rep(j,1,n)
			{
				if (g[i][j]=='1' && (state&(1<<((i-1)*n+j-1))))
				{
					flag=0; break;
				}
				if (g[i][j]=='1' || (state&(1<<((i-1)*n+j-1)))) 
				{
					can[i]|=(1<<(j-1));
					op[j]|=(1<<(i-1));
				}
			}
		if (!flag) continue;
		int fail=0;
		rep(i,1,n)
		{
			int ok=0;
			int s=can[i];
			int x=s;
			while (x>0)
			{
				int t=0;
				rep(i,1,n)
					if (x&(1<<(i-1)))
						t|=op[i];
				if (__builtin_popcount(t)<=__builtin_popcount(x))
				{
					ok=1; break;
				}
				x=(x-1)&s;
			}
			if (!ok) { fail=1; break; }
		}
		if (!fail) 
		{
			int cost=__builtin_popcount(state);
			if (cost<best) best=cost;
		}
	}
	printf("%d\n",best);
}

int main()
{
	ios::sync_with_stdio(true);
	#ifndef ONLINE_JUDGE
		freopen("D.in","r",stdin);
	#endif
	int tcase; scanf("%d",&tcase);
	rep(nowcase,1,tcase)
	{
		printf("Case #%d: ",nowcase);
		lemon();
	}
	return 0;
}

