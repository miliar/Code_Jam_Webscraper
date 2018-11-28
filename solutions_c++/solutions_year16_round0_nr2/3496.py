//Author: sagarkaniche
#include <bits/stdc++.h>
#define ll long long
using namespace std;
#define si(x) scanf("%d",&x)
#define sdb(x) scanf("%lf",&x)
#define sll(x) scanf("%lld",&x)
#define pb push_back
#define res 1000000007
typedef pair<int,int> pp;

int dp[200][2];
int main()
{
	int t,cnt=1;
	si(t);
	while(t--)
	{
		int i;
		string str;
		cin>>str;
		for(i=0;i<str.size();i++)
			if(str[i]=='+') str[i]='1';
			else str[i]='0';
		int temp = str[0]-'0';
		dp[0][temp]=0;
		dp[0][(temp+1)%2]=1;
		for(int i=1;i<str.size();i++)
		{
			temp = str[i] - '0';
			dp[i][temp] = dp[i-1][temp];
			dp[i][(temp+1)%2] = dp[i][temp] + 1; 
		}
		printf("Case #%d: %d\n",cnt++, dp[str.size()-1][1]);
	}
	return 0;
}