#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <map>
using namespace std;
#define LL long long
int dp[105];



int main()
{
	char s[105];
	int T,cas = 1;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%s",s);
		int len = strlen(s);
		if(s[0] == '+') dp[0] = 0;
		else dp[0] = 1;
		for(int i=1;i<len;++i)
		{
			if(s[i] == '+')
				dp[i] = dp[i-1];
			else
			{
				if(s[i-1] == '+')
					dp[i] = dp[i-1] + 2;
				else
					dp[i] = dp[i-1];
			}
		}
		printf("Case #%d: %d\n", cas++, dp[len - 1]);
	}
	return 0;
}