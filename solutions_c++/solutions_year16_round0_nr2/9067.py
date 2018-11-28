#include<iostream>
using namespace std;
string in;
const int inf=1000000007;
int dp[2][2][101][101];//inv, plus, a, b
inline char change(bool c)
{
	if(c)return '-';
	return '+';
}
bool ok(int a,int b,bool plus)
{
	char c=change(plus);
	for(int i=a;i<=b;i++)
		if(in[i]==c)return false;
	return true;
}
int go(int a,int b,bool plus=true,bool inv=false)
{ 
	if(dp[inv][plus][a][b]!=inf)return dp[inv][plus][a][b];
	dp[inv][plus][a][b]=inf-1000;
	if(ok(a,b,plus))
	{
		dp[inv][plus][a][b]=0;
		dp[!inv][!plus][a][b]=min(1,dp[!inv][!plus][a][b]);
		
		dp[!inv][plus][a][b]=0;
		dp[inv][!plus][a][b]=min(1,dp[inv][!plus][a][b]);
		return 0;
	}
	char opsign=change(plus);
	if(!inv)
	{
		for(int i=b;i>=a;i--)
		{
			dp[inv][plus][a][b]=min(dp[inv][plus][a][b],go(a,i,!plus,!inv)+1);
			dp[inv][plus][a][b]=min(dp[inv][plus][a][b],go(a,i,plus,inv));
			if(in[i]==opsign)break;

		}
		for(int i=b;i>=a;i--)
		{
			dp[inv][plus][a][b]=min(dp[inv][plus][a][b],go(a,i,plus,!inv)+2);
			dp[inv][plus][a][b]=min(dp[inv][plus][a][b],go(a,i,!plus,inv)+1);
			if(in[i]!=opsign)break;
		}
	}
	else
	{
		for(int i=a;i<=b;i++)
		{
			dp[inv][plus][a][b]=min(dp[inv][plus][a][b],go(i,b,!plus,!inv)+1);
			dp[inv][plus][a][b]=min(dp[inv][plus][a][b],go(i,b,plus,inv));
			if(in[i]==opsign)break;
		}
		for(int i=a;i<=b;i++)
		{
			dp[inv][plus][a][b]=min(dp[inv][plus][a][b],go(i,b,plus,!inv)+2);
			dp[inv][plus][a][b]=min(dp[inv][plus][a][b],go(i,b,!plus,inv)+1);
			if(in[i]!=opsign)break;
		}

	}
	return dp[inv][plus][a][b];
}
int main()
{
	ios::sync_with_stdio(false);
//	cin.tie(0);
	int t;
	cin >> t;

	for(int i=1;i<=t;i++)
	{
		cin >> in;
		for(int k=0;k<4;k++)
			for(int a=0;a<=100;a++)
				for(int b=0;b<=100;b++)
					dp[k/2][k%2][a][b]=inf;
		int ans=go(0,in.size()-1);
		cout << "Case #"<<i<<": "<<ans<<"\n";
	}

}
