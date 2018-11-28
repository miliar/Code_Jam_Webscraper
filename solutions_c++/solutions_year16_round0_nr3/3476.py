// In the name of GOD
// A fan of Michal Danilak a.k.a Mimino
#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define ll long long
#define ull unsigned long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define vi vector<int>
#define piii pair < int,pair <int,int> >
#define f first
#define s second
#define MAXN 2000000
#define MOD 1000000007
#define IOS ios_base::sync_with_stdio(0)
#define PI 3.1415926535897932384626
int dx[4]={-1,1,0,0};
int dy[4]={0,0,-1,1};
bool  isone(ll,int);
int count(ll);
ll exp(ll,ll,ll);
ll GCD(ll,ll);
int isprime[MAXN];
int cnt=0;
vector<int> primes;
ll base(string x,int base)
{
	ll ret=0;
	ll mul=1;
	for(int i=x.length()-1;i>=0;i--)
	{
		ret+=(mul*(x[i]-'0'));
		mul=mul*1LL*base;
	}
	return ret;
}
bool check(string x)
{
	for(int j=2;j<=10;j++)
	{
		ll number=base(x,j);
		int ok=0;
		for(int i=0;((1LL*primes[i]*primes[i])<=number) && (i<primes.size());i++)
		{
			if(!(number%(1LL*primes[i])))
			{
				ok=1;
				break;
			}
		}
		if(!ok)	return false;
	}
	return true;
}
void calc(string a,int idx,int len)
{
	if(idx==(len-1))
	{
		string b=a+"1";
		if(check(b) && (cnt<50))
		{
			cout<<b<<" ";
			cnt++;
			string x=b;
			for(int j=2;j<=10;j++)
			{
				ll number=base(x,j);
				int ok=0;
				for(int i=0;((1LL*primes[i]*primes[i])<=number) && (i<primes.size());i++)
				{
					if((number%(1LL*primes[i]))==0LL)
					{
						cout<<primes[i]<<" ";
						break;
					}
				}
			}
			cout<<"\n";
		}
		return ;
	}
	if(cnt<50)
	{
	string b=a+"0";
	string c=a+"1";
	calc(b,idx+1,len);
	calc(c,idx+1,len);
	}
	return ;
}
void sieve()
{
	for(ll i=2;i<MAXN;i++)
	{
		if(!isprime[i])
		{
			for(ll j=1LL*i*i;j<MAXN;j+=i)
				isprime[j]=1;
			primes.pb(i);
		}
	}
	return ;
}
int main()
{
	IOS;
	#ifndef ONLINE_JUDGE
	freopen("C-small-attempt0.in", "r", stdin);
    freopen("QR_C_sout2.txt", "w", stdout);
	#endif
	int x,y,z;
	cin>>x>>y>>z;
	cout<<"Case #1:\n";
	cnt=0;
	sieve();
	string a="1";
	calc(a,1,16);
	return 0;
}

ll GCD(ll a,ll b)
{
   if(!b) return a;
   else   return GCD(b,a%b);
}
ll exp(ll a,ll b,ll c)
{
	ll ret=1LL;
	ll mult=a;
	while(b)
	{
		if(b&1)	ret=(ret*mult)%c;
		mult=(mult*mult)%c;
		b>>=1;
	}
	return ret;
}
int count(ll x)
{
   int ret=0;
   while(x)
   {
		   if(x&1)  ret++;
		   x>>=1LL;
   }
   return ret;
}

bool isone(ll x,int pos)
{
	 return x&(1<<pos);
}





