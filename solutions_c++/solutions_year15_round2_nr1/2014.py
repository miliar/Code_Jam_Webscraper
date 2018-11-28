#include<bits/stdc++.h>
using namespace std;
#define N 1000006
#define ll long long
ll a[N],next[N][2],dist[N];
ll dp[N];

ll rev(ll n)
{
	ll i,rev = 0;
	for(i=n;i>0;i/=10) rev = rev*10 + i%10;
	return rev;
}
void pre()
{	ll i;
	memset(dp,N,sizeof(dp));
	dp[1] = 1;
	for(i=2;i<=1000000;++i){
		if(rev(rev(i)) == i){
		
		dp[i] = min(dp[rev(i)]+1,dp[i-1]+1);
		//cout<<"rev"<<rev(i)<<" "<<rev(rev(i))<<endl;
		}
		else
		dp[i] = dp[i-1] + 1;
		//cout<<i<<" "<<dp[i]<<endl;
		//if(i==23) break;
	}
	//while(1) continue;
	//bfs();
}

int main()
{
	pre();
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	ll n;
	cin>>t;
	int j = 1;
	while(t--){
		cin>>n;
		cout<<"Case #"<<j<<": "<<dp[n]<<endl;
		j++;
	}
	return 0;
}
