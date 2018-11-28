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
int solve(string& s,int n)
{
	int i,ans=0;
				for(i=1;i<n;i++)
				{
					if(s[i]^s[i-1])
					{
						ans++;
					}
				}
				if(s[n-1]=='-')
					ans++;
		return ans;
}
int main()
    {
		//freopen("in.txt","r",stdin);
  		//freopen("out.txt","w",stdout);
		ios_base::sync_with_stdio(false);
		int i,n,t,ans,j;
		cin>>t;
		string s;
		for(j=1;j<=t;j++)
		{
			cin>>s;
			n=s.length();
			cout<<"Case #"<<j<<": ";
			ans=solve(s,n);
			cout<<ans<<"\n";
		}
    return 0;
}
