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
 	ll t,n,i,c1,c2,j,ans,flag;
 	cin>>t;
 	string s;
 	for(i=1;i<=t;i++)
 	{ 	
 		
 		c1=c2=0;
 		cin>>s;
//					printf("Case #%lld: %lld\n",i,tmp);
		if(s[0]=='+')
		{
			c1++;
			flag=0;
		}
		else
		{
			c2++;
			flag=1;
		}
		for(j=1;j<s.length();j++)
		{
			if(s[j]=='+' && flag==1)
			{
				c1++;
				flag=0;
			}
			else if(s[j]=='-' && flag==0)
			{
				c2++;
				flag=1;
			}
		}
		if(s[0]=='+')
		{
			if(c1==c2)
			ans=c1*2;
			else
			ans=c2*2;
		}
		else
		{
			if(c1==c2)
			ans=c1*2-1;
			else
			ans=c2*2-1;
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
 	}
	return 0;
}
