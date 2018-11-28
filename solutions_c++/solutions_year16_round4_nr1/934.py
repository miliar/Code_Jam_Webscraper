#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
int test,dp[13][3],p[3],n;
string dfs(int dep,int now)
{
//	cout<<dep<<' '<<now<<endl;
	if (dep==n)
	{
		if (now==0) return string("R");
		else if (now==1) return string("P");
		else if (now==2) return string("S");
	}
	string temp1=dfs(dep+1,now),temp2=dfs(dep+1,(now+2)%3);
	string temp3=temp1+temp2,temp4=temp2+temp1;
	//cout<<temp3<<' '<<temp4<<endl;
	return min(temp3,temp4);
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("12.out","w",stdout);
	cin>>test;
	dp[0][0]=1;
	for (int i=1;i<=12;i++) 
	{
		dp[i][0]=dp[i-1][0]+dp[i-1][1];
		dp[i][1]=dp[i-1][1]+dp[i-1][2];
		dp[i][2]=dp[i-1][2]+dp[i-1][0];
	}
	for (int kk=1;kk<=test;kk++)
	{
		printf("Case #%d: ",kk);
		cin>>n>>p[0]>>p[1]>>p[2];
		if (p[0]==dp[n][0]&&p[1]==dp[n][1]&&p[2]==dp[n][2]) cout<<dfs(0,0);
		else if (p[0]==dp[n][2]&&p[1]==dp[n][0]&&p[2]==dp[n][1]) cout<<dfs(0,1);
		else if (p[0]==dp[n][1]&&p[1]==dp[n][2]&&p[2]==dp[n][0]) cout<<dfs(0,2);
		else printf("IMPOSSIBLE");
		printf("\n");
	}
	return 0;
}
