#include<bits/stdc++.h>
using namespace std;
#define ll long long 
#define ull unsigned long long 
#define m(a,i,n) memset(a,i,n)
#define f(i,n) for(i=0;i<n;i++)
#define sc(a) scanf("%lld",&a)
#define vect_int vector<int>
#define pb(x) push_back(x)
#define lb lower_bound
#define ub upper_bound
#define pf(a) printf("%lld\n",a)
/*inline void Scan_f(int& a)
{
	char c = 0;
	while(c<33)
	c= getc(stdin);
	a = 0;
	while(c>33)
	{
		a = a*10 + c - '0';
		c = getc(stdin);
	}
}*//*
ll gcd(ll a,ll b)
{
	if(b == 0)
	{
	    return a;
	}
	else
	{
		return gcd(b, a % b);
	}
}*/
//map<pair<ll,ll>,ll>  :: iterator itr;
//M[make_pair(a,b)]++;
int main() { 
	// your code goes here
 	ios_base::sync_with_stdio(false);
 	ll t,n,i,j;
 	cin>>t;
 	for(i=1;i<=t;i++)
 	{ 
		string s,ans;
 		cin>>s;
 		ans+=s[0];
 		
 		for(j=1;j<s.length();j++)
 		{
 			if(s[j]>=ans[0])
 			{
 				ans=s[j]+ans;
			}
			else
			ans+=s[j];
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
 	}
	return 0;
}
