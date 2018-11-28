#include<bits/stdc++.h>
using namespace std;
char s[1001];int dp[1001];
int main()
{
	int t,i,p=1;
	scanf("%d",&t);
	
	while(t--)
	{
		int n,friends=0,result=0;
		scanf("%d",&n);
		
		scanf("%s",s);
		dp[0]=s[0]-48;
		for(i=1;i<=n;i++)
		{
			dp[i]=dp[i-1]+s[i]-48;
		}
		if(s[0]-48==0)
		friends++;
		for(i=1;i<=n;i++)
		{
			if(s[i]==48)
			continue;
			if(i>dp[i-1]+friends)
			{
				friends+=i-(dp[i-1]+friends);
				
			}
		}
                 //cout<<friends<<endl;
		printf("Case #%d: %d\n",p,friends);
                   p++;
	}
	return 0;
}
