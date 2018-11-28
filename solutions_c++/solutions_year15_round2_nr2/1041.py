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

int solve(int r,int c,int n)
{
	int x=r*c;
	int ret=INT_MAX;
		
	int po=pow(2,x);
	
	for(int k=0;k<po;k++)
	{
		bool occ[25][25]={0};
		int cnt=0;
		//k is bit vector representing occ cells
		for(int m=0;m<x;m++)
		{
			if(k&(1<<m))
			{
				cnt++;
				for(int i=0;i<r;i++){bool f=0; for(int j=0;j<c;j++) if(c*i+j==m) {f=1;occ[i][j]=1;break;} if(f) break;}				
			}
		}
		
		if(cnt!=n) continue;
		int val=0;
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				if(j+1<c)
				{
					if(occ[i][j] && occ[i][j+1]) val++;
				}
				if(i+1<r)
				{
					if(occ[i][j] && occ[i+1][j]) val++;
				}
			}
		}
		ret=min(ret,val);
	}
	return ret;
}

int main()
{ freopen("input.in","r",stdin);
  freopen("output.txt","w",stdout);
  int cas=1;
  //solve();
  test
  {
   int r,c,n;
   cin>>r>>c>>n;
   int ans=solve(r,c,n);
   cout<<"Case #"<<cas<<": "<<ans<<endl;
   cas++;
  }

  return 0;
}

