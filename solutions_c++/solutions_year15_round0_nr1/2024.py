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


int main()
{ freopen("input.in","r",stdin);
  freopen("output.txt","w",stdout);
  int cas=1;
  test
  {
  	int l;
  	string s;
  	cin>>l>>s;
  	int sum=s[0]-48;
  	int ans=0;
  	for(int i=1;i<l+1;i++)
  	{
  		if(sum<i)
  		{
  			ans+=i-sum;
			sum+=i-sum;	
  		}
		sum+=s[i]-48;  		
  	}
   cout<<"Case #"<<cas<<": "<<ans<<endl;
   cas++;
  }

  return 0;
}

