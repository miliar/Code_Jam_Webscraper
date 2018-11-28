#include<bits/stdc++.h>
using namespace std;
#define ull unsigned long long 
#define ll long long
#define MAX 100
#define pb push_back
#define gc getchar
#define mp make_pair
#define fast(){cin.sync_with_stdio(0);cin.tie(0);cout.tie(0);}
ll mulmod(ll a,ll b, ll c)
{ 
	long long x = 0,y=a;
	while(b > 0)
	{
		if(b%2 == 1){
		x = (x+y)%c;
	}
	y = (y*2)%c;
	b /= 2;
	}
	return x%c;
}
ll modulo(ll a,ll b,ll c)
{
	long long x=1,y=a;
	while(b > 0)
	{
	  if(b%2 == 1){
      x=(x*y)%c;
	}
	y = (y*y)%c; 
	b /= 2;
	}
  return x%c;
}
ll fun(string s, ll base)
{
	ll ans=0;
	int n=s.length();
	for(int i=0;i<n;i++)
		ans = ans*base + (ll)(s[i]-'0');
	return ans;
}
vector<int> witness;
int sz;
bool Miller(long long p)
{
    if(p<2)
    	return false;
    if(p!=2 && p%2==0)
    	return false;
    long long s=p-1;
    while(s%2==0)
	{
    	s/=2;
    }
    for(int i=0;i<sz;i++)
	{
    	long long a=witness[i],temp=s;
    	long long mod=modulo(a,temp,p);
    	while(temp!=p-1 && mod!=1 && mod!=p-1)
		{
	        mod=mulmod(mod,mod,p);
	        temp *= 2;
    	}
    	if(mod!=p-1 && temp%2==0)
		{
        	return false;
    	}
    }
    return true;
}
bool isprime(ll n)
{
    for(int i=0;i<sz;i++)
    if(n==witness[i])
        return true;
    for(int i=0;i<sz;i++)
    if(n%witness[i]==0)
        return false;
    return Miller(n);
}
int main()
{
	witness.pb(2);
    witness.pb(13);
   	witness.pb(23);
   	witness.pb(37);
    witness.pb(1662803);
    sz = 5;
    freopen("C-small-attempt1.in","r+",stdin);
	freopen("output3small.txt","w+",stdout);
	int t;
	cin>>t;
	int cases=0;
	while(t--)
	{
		cases++;
		int n, J;
		cin>>n>>J;
		cout<<"Case #"<<cases<<": \n";
		int cnt=0;
		for(int i=0;i<(1<<n-2) && cnt<J;i++)
		{
			string s="1";
			for(int j=0;j<n-2;j++)
			{
				if(i&(1<<j))
					s+="1";	
				else
					s+="0";
			}
			s+="1";
			bool f=0;
			vector<ll>P;
			for(ll k=2;k<=10;k++)
			{
				ll x=fun(s,k);
				P.pb(x);
				if(isprime(x))
				{f=1;break;}
			}
			vector<ll>Q;
			if(!f)
			{
				
				for(int k=0;k<P.size();k++)
				{
					ll temp=P[k];
					//cout<<temp<<endl;
					for(ll j=2;j<=sqrt(temp);j++)
					{
						if(temp%j==0)
						{
							Q.pb(j);
							break;	
						}
					}
				}
			}
			if(Q.size()==9)
			{
				cout<<s<<" ";
				for(int k=0;k<Q.size();k++)
					cout<<Q[k]<<" ";
				cout<<"\n";
				cnt++;
			}
		}
	}
}
