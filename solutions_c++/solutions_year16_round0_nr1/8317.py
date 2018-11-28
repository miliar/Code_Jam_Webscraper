#include<iostream>
#include<cstdio>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<list>
#include<cstring>
#include<stack>
#include<queue>
using namespace std;
#define ll long long
#define vi vector<int>
#define vii vector<vi >
#define pp pair<int,int>
#define pb push_back
#define mp make_pair
#define ppl pair<ll,ll>
#define vl vector<ll>
#define vll vector<vl >
#define llu unsigned ll
#define all(c) c.begin(),c.end()
#define mod 1000000007
#define sc scanf
#define pf printf
ll power(ll a,ll b)
{
	if(!b)
		return 1;
	if(b==1)
		return a;
	ll temp=power(a,b/2);
	temp=(temp*temp);
	if(b&1)
		temp=(temp*a);
	return temp;
}
int main()
    {
		//freopen("in.txt","r",stdin);
  		//freopen("out.txt","w",stdout);
		ios_base::sync_with_stdio(false);
		ll t;
		ll n,i,j,temp,o,ans;
		cin>>t;
		//t=200;
		for(j=1;j<=t;j++)
		{
			cin>>n;
			cout<<"Case #"<<j<<":"<<" ";
			if(!n)
			{
				cout<<"INSOMNIA"<<"\n";
			}
			else
			{
				set<ll> s;
				i=1;
				o=n;
				ans=n;
				while((s.size()!=10))
				{
					ans=n;
					temp=n;
					while(temp)
					{
						s.insert(temp%10);
						temp/=10;
					}
					i++;
					n=o*i;
				}
				cout<<ans<<"\n";
			}
		}
    return 0;
}
