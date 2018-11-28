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
int t,n,ans,tot;
char in[M];
int main()
{
	int x;
	scanf("%d",&t);
	REP(tt,1,t)
	{
		ans = 0;
		tot = 0;
		scanf("%d", &n);
		scanf("%s", in);

		REP(i,0,n)
		{
			x = in[i]-'0';
			if(tot<i)
			{
				ans += i-tot;
				tot += i-tot;
			}
			tot += x;
		}
		printf("Case #%d: %d\n",tt,ans);
	}
	return 0;
}

