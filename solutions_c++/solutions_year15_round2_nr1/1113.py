/*Author: Rishul Aggarwal*/

#include<bits/stdc++.h>

#define mod 1000000007
#define ll long long
#define rep(i,a,b) for(int i=a;i<=b;i++)
#define in(type,x) scanf("%" #type,&x)
#define debug(args...) {dbg,args; cerr<<endl;}
#define test int t;\
in(d,t);\
while(t--)

using namespace std;

struct debugger
{template<typename T> debugger& operator,(const T& v)
{cerr<< v <<" ";
return *this;
}
}dbg;

ll gcd(ll a,ll b) {if(b==0) return a; return gcd(b,a%b);}

ll power(ll b,ll exp,ll m) {ll ans=1; b%=m; while(exp){if(exp&1) ans=(ans*b)%m; exp>>=1; b=(b*b)%m; } return ans; }

ll dp[1000002];

int check(int n)
{
	int rev=0,d;
	do
	{
		d=n%10;
		n/=10;
		rev=rev*10+d;
	}while(n);
	return rev;
}

void solve()
{
	rep(i,1,20) dp[i]=i;
	
	for(int i=21;i<=1000000;i++)
	{
		dp[i]=1+dp[i-1];
		int rev=check(i);
		int newrev=check(rev);
		if(rev<i && newrev==i) dp[i]=min(dp[i],1+dp[rev]);
	}	
}

int main()
{ freopen("input.in","r",stdin);
  freopen("output.txt","w",stdout);
  int cas=1;
  solve();
  test
  {
   int n;
   cin>>n;
   cout<<"Case #"<<cas<<": "<<dp[n]<<endl;
   cas++;
  }

  return 0;
}

