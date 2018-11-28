#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back

int main()
{
	
	freopen("ip.txt","r",stdin);
	freopen("op.txt","w",stdout);
	bool dp[5][5][5];
	ll i,j,k;
	
	for(i=1;i<=4;i++)
	{
		for(j=1;j<=4;j++)
		{
			for(k=1;k<=4;k++)dp[i][j][k] = true;
		}
	}
	
	for(i=1;i<=4;i++)
	{
		for(j=1;j<=4;j++)
		{
			for(k=1;k<=2;k++)
			{
				if(i%k==0 || j%k==0)
				{
					dp[k][i][j] = false;
				}
			}
		}
	}
	
	
	dp[3][2][3] = dp[3][3][2] = dp[3][3][3] = dp[3][3][4] = dp[3][4][3] = dp[4][3][4] = dp[4][4][3] = dp[4][4][4] = false;
	
	ll t,x,r,c,co;
	cin>>t;
	co = 1;
	while(t--)
	{
		cin>>x>>r>>c;
		cout<<"Case #"<<co++<<": ";
		if(dp[x][r][c])
		{
			cout<<"RICHARD\n";
		}
		else
		{
			cout<<"GABRIEL\n";
		}
		
	}
	
    return 0;
}

