#include<cstdio>
#include<cstring>
#include<iostream>
#include<queue>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<string>
using namespace std;
typedef long long ll;
const int N = 1005;
char s[N];
int dp[N][2];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,ca=1;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",ca++);
		scanf("%s",s);
		int n=strlen(s);
		dp[0][0]=dp[0][1]=0;
		for(int i=1;i<=n;i++)
		{
			if(s[i-1]=='+')
			{
				dp[i][0]=min(dp[i-1][0],dp[i-1][1]+1);
				dp[i][1]=min(dp[i-1][1]+2,dp[i-1][0]+1);
			}
			else
			{
				dp[i][1]=min(dp[i-1][1],dp[i-1][0]+1);
				dp[i][0]=min(dp[i-1][0]+2,dp[i-1][1]+1);
			}
		}
		printf("%d\n",dp[n][0]);
	}
	return 0;
}

