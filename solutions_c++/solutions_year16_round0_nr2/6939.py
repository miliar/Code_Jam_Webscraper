#include<bits/stdc++.h>

#define ll 		long long
#define sc(n)	scanf("%d",&n)
#define scll(n)	scanf("%lld",&n)

using namespace std;

int dp[110];
int main()
{
	
	int test, n, tno = 0;
	string s;
	sc(test);
	while(test--)
	{
		tno++;
		for(int i=0;i<110;i++)
			dp[i] = 0;
		cin>>s;
		n = (int)s.length();
		//base case
		if(s[0] == '-')
			dp[0] = 1;
		for(int i=1;i<n;i++)
		{
			if(s[i-1] == '+' && s[i] == '-')
				dp[i] = dp[i-1] + 2;
			else dp[i] = dp[i-1];
		}
		printf("Case #%d: %d\n",tno,dp[n-1]);
	}
}