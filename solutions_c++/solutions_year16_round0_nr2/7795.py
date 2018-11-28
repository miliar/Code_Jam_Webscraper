#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<iostream>
typedef long long ll;
int dp[105][105],a[105],c=1;
//typedef mod 1000000007;
using namespace std;
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t,i,j,k,n;
	char ch[105];
	scanf("%d",&t);
	while(t--)
	{
		memset(dp,0,sizeof(dp));
		scanf("%s",ch+1);
		n=strlen(ch+1);
		for(i=1;i<=n;i++)
		{
			if(ch[i]=='+')
			a[i]=0;
			else
			a[i]=1;
		}
		for(int r=1;r<=n;r++)
		{
			for(int l=r;l>=1;l--)
			{
				if(l==r)
				{
					dp[l][r]=a[r];
					continue;
				}
				if(a[r]==a[r-1])
				dp[l][r]=dp[l][r-1];
				else
				if(a[r])
				dp[l][r]=dp[l][r-1]+2;
				else
				dp[l][r]=dp[l][r-1];
				for(int k=r-1;k>l;k--)
				{
					if(a[k]==a[r]&&a[k])
					{
						dp[l][r]=min(dp[l][r],dp[l][r-1]+dp[k][r]+2);
					}
				}
			}
		}
		printf("Case #%d: %d\n",c++,dp[1][n]);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
 }
