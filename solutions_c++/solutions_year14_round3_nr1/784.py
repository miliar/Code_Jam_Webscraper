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
 int cas=1;
 f2=fopen("output.txt","w");	
 int t;
 fscanf(f1,"%d",&t);
 while(t--)
  {
   ll a,b;
   fscanf(f1,"%lld/%lld",&a,&b);
   //cout<<a<<" "<<b<<endl;	
   ll ans=0;
   ll g=gcd(a,b);
   a/=g,b/=g;
   if((b&(b-1)))
   {
    fprintf(f2,"Case #%d: impossible\n",cas);
    cas++;
    continue;
   }
   while(a<b)
   {
   	ans++;
   	b/=2;
   }
   fprintf(f2,"Case #%d: %d\n",cas,ans);
   cas++;
  }


return 0;
}



