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
{
	FILE *f1,*f2;
	f1=fopen("input.txt","r");
	f2=fopen("outputB.txt","w");
	int t;
	fscanf(f1,"%d",&t);
	int tests=1;
	while(t--)
	{
		double c,f,x;
		fscanf(f1,"%lf %lf %lf",&c,&f,&x);
		
		int n = (int)floor(x/c - 2.0/f);
		
		//debug(n);
		
		double ans=0.0,rate=2.0;
		
		if(x <= c) ans = x/2.0;
		
		else
		{		
		 rep(i,1,n)
		 {
		 	ans = ans + c/rate;
		 	rate = rate + f;
		 }
		 		 
		 ans = ans + x/rate;
		}
		 	
	    fprintf(f2,"Case #%d: %.7lf\n",tests,ans);
		
		tests++; 
	}
 
return 0;
}



