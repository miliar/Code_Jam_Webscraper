#include<bits/stdc++.h>
#define REP(x,y,z) for(int x=y;x<=z;x++)
#define FORD(x,y,z) for(int x=y;x>=z;x--)
#define MSET(x,y) memset(x,y,sizeof(x))
#define FOR(x,y) for(__typeof(y.begin()) x=y.begin();x!=y.end();x++)
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define SZ size()
#define M 1005
using namespace std;
typedef long long LL;
int t,n,in[M];
int ans;
int main()
{
	scanf("%d",&t);
	REP(tt,1,t)
	{
		ans = M;
		scanf("%d",&n);
		REP(i,1,n)scanf("%d",&in[i]);
		
		REP(i,1,1000)
		{
			int cnt=0, x;
			REP(j,1,n) if(in[j] > i)
			{
				x = in[j] - i;
				cnt += x/i;
				if(x%i) cnt++;
			}
			ans = min(ans, cnt+i);
		}
		printf("Case #%d: %d\n",tt,ans);
	}
	return 0;
}

