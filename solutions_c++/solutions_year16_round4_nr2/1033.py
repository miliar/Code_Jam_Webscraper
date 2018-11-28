#include <bits/stdc++.h>
using namespace std;
int n,k;
double a[211];
bool u[20];
double dp[211][211][211];
double solve(int i,int Y,int N)
{
	if(Y==0 && N==0) return 1;
	if(Y<0 || N<0 || i<0) return 0;
	if(dp[i][Y][N]!=-1) return dp[i][Y][N];
	//cout<<i<<' '<<Y<<' '<<N<<endl;
	double ans=0;
	if(u[i])
		ans=solve(i-1,Y-1,N)*a[i] + solve(i-1,Y,N-1)*(1-a[i]);
	else
		ans=solve(i-1,Y,N);
	return dp[i][Y][N]=ans;
}
double dfs(int i,int cnt)
{
	if(cnt>k) return 0;
	if(cnt+n-i<k) return 0;
	if(i==n)
	{
	assert(cnt==k);
		//cout<<i<<endl;
		for(int i=0;i<n;i++)
			for(int j=0;j<=k/2;j++)
				for(int l=0;l<=k/2;l++)
					dp[i][j][l]=-1;
		return solve(n-1,k/2,k/2);
	}
	u[i]=0;
	double ans=dfs(i+1,cnt);
	u[i]=1;
	return max(ans,dfs(i+1,cnt+1));
}
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	int T,no=0;
	cin>>T;
	while(T--)
	{
		cin>>n>>k;
		for(int i=0;i<n;i++)
			cin>>a[i];
		double ans=dfs(0,0);
		cout<<fixed<<setprecision(12);
		cout<<"Case #"<<++no<<": "<<ans<<'\n';
	}
}