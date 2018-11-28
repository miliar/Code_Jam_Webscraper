#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;

ll b,m;
ll ans[50][50];
ll dp[50];

void init()
{
	for(ll i=0;i<50;i++)
	{
		for(ll j=0;j<50;j++)
			ans[i][j]=0;
		dp[i]=0;	
	}
	
}

void build()
{
	ll i,j;
	for(i=b;i>=0;i--)
	{
		for(j=i+1;j<=b;j++)
		{
			if(m>=dp[j]+dp[i])
			{
				ans[i][j]=1;
				dp[i]+=dp[j];
				
				if(dp[i]==m)
				break;
				
			}
		}
	}
	
}

int main() {
	
	ll tc;cin>>tc;
	
	for(ll t=1;t<=tc;t++)
	{
		
		cin>>b>>m;
		init();
		b--;
		dp[b]=1;
		build();
		
		cout<<"Case #"<<t<<": ";
		
		if(dp[0]==m)
		{
			cout<<"POSSIBLE\n";	
		
			for(ll i=0;i<=b;i++)
			{
				for(ll j=0;j<=b;j++)
				{
					cout<<ans[i][j];
				}
				cout<<"\n";
			}
		}
		
		else
		{
			
			cout<<"IMPOSSIBLE\n";
			
		}
	
	}
	
	return 0;
}