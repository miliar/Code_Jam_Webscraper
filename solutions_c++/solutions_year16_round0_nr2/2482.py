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
#define M 105
void RI(){}
template<typename... T>
void RI( int& head, T&... tail ) {
    scanf("%d",&head);
    RI(tail...);
}
using namespace std;
typedef long long LL;
int t,n,dp[M][2];
char in[M];
int main()
{
	RI(t);
	REP(tt,1,t)
	{
		scanf("%s", in+1);
		n = strlen(in+1);

		MSET(dp, 0);
		REP(i,1,n)
		{
			//0 -
			if(in[i]=='-')
			{
				dp[i][0] = dp[i-1][0];
			}
			else
			{
				dp[i][0] = dp[i-1][1] + 1;
			}

			//1 +
			if(in[i]=='+')
			{
				dp[i][1] = dp[i-1][1];
			}
			else
			{
				dp[i][1] = dp[i-1][0] + 1;
			}
		}

		printf("Case #%d: %d\n",tt,dp[n][1]);
	}
	return 0;
}

