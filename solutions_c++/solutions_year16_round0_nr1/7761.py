#include <bits/stdc++.h>
using namespace std;

long long int dp[1000005][2];
long long int ans(long long int n,bool one)
{
	if(dp[n][one]!=-1)return dp[n][one];
	long long int orig = n;
	bool hasreach[12] = {0};
	char str[32];
	if(one)hasreach[0] = 1;
	while(1)
	{
		sprintf(str,"%lld",n);
		int len = strlen(str);
		for(int i = 0;i<len;i++)
		{
			hasreach[str[i]-'0'] = 1;
		}
		int sum = 0;
		for(int i = 0;i<=9;i++)
		{
			sum += hasreach[i];
		}
		if(sum==10)return dp[orig][one] = n;
		n += orig;
	}
}
long long int ans2(long long int n)
{
	long long int multip = 1;
	while(!(n % 10))
	{
		n /= 10;
		multip *= 10;
	}
	return multip*ans(n, multip>1?1:0);
}
int main()
{
	memset(dp,-1,sizeof(dp));
	int tc;
	scanf("%d",&tc);
	for(int i = 1;i<=tc;i++)
	{
		printf("Case #%d: ",i);
		int n;
		scanf("%d",&n);
		if(!n)
		{
			printf("INSOMNIA\n");
		}
		else printf("%lld\n",ans2(n));
	}
}

