#include<iostream>
using namespace std;
#include<algorithm>
#include<vector>
#include<set>
#include<utility>
#include<string.h>
#include<math.h>
#define ll long long int
#define f first
#define s second
ll dp[40][5010][11],sp[100000001];
bool prime[100000001]={0};
set<pair<ll,vector<ll> > > ans;
void sieve()
{
	for(ll i=2;i<=10000;++i)
	{
		if(!prime[i])
		{
			for(ll j=2;i*j<=100000000;++j)
			{
				prime[i*j]=1;
				sp[i*j]=j;
			}
		}
	}
}
ll isprime(ll n)
{
	for(ll i=3;i<=sqrt(n);i+=2)
	{
		if(n%i==0)
			return i;
	}
	return 0;
}
int main()
{
	//ios_base::sync_with_stdio(false);cin.tie(0);
	ll t,i,j,r,n,k,count=0,d,base,counter=1;
	cin>>t;
	memset(dp,0,sizeof(dp));
	dp[2][1][10]=11;
	dp[2][1][2]=3;
	dp[2][1][3]=4;
	dp[2][1][4]=5;
	dp[2][1][5]=6;
	dp[2][1][6]=7;
	dp[2][1][7]=8;
	dp[2][1][8]=9;
	dp[2][1][9]=10;
	r=2;
	sieve();
	for(i=3;i<=16;++i,r*=2)
	{
		for(base=2;base<=10;++base)
		{
			for(j=1;j<=r;j+=2)
			{
				dp[i][j][base]=dp[i-1][(ll)ceil(j/2.0)][base]*base+1;
				dp[i][j+1][base]=dp[i-1][(ll)ceil(j/2.0)][base]*base-(base-1);
				//cout<<dp[i][j][base]<<endl;
			}
		}
	}
	while(t--)
	{
		cin>>n>>k;
		cout<<"Case #"<<counter++<<": "<<endl;
		r=(ll)(pow(2,n-2));
		for(j=1;j<=r;++j)
		{
			bool f=0;
			vector<ll> temp;
			for(i=2;i<=10;++i)
			{
				if(dp[n][j][i]<=100000000)
				{
					if(!prime[dp[n][j][i]])
					{
						f=1;
						break;
					}
					else
						temp.push_back(sp[dp[n][j][i]]);
				}
				else
				{
					ll p=isprime(dp[n][j][i]);
					if(p==0)
					{
						f=1;
						break;
					}
					else
						temp.push_back(p);
				}
			}
			if(f==0)
				ans.insert(make_pair(j,temp));
			if(ans.size()==k)
				break;
		}
		set<pair<ll,vector<ll> > >::iterator it;
		for(it=ans.begin();it!=ans.end();++it)
		{
			cout<<dp[n][(*it).f][10]<<" ";
			for(j=0;j<(*it).s.size();++j)
				cout<<(*it).s[j]<<" ";
			cout<<endl;
		}
	}
	return 0;
}
