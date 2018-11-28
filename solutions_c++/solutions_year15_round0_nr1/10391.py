		//CodeJam ________ Challenge 
		// template by vicky002
#include<bits/stdc++.h>
using namespace std;
#define X first
#define Y second
#define in_t(x) 		scanf("%d",&x)
#define in_l(x) 		scanf("%ld",&x)
#define in_ll(x) 		scanf("%lld",&x)
#define out_t(x) 		printf("%d",x)
#define out_l(x) 		printf("%ld",x)
#define out_ll(x) 		printf("%lld",x)
#define mp make_pair
#define ph push
#define pb push_back
#define REP(i,a,n)			 for(int _tmp=n,i=a;i<=_tmp;++i)
#define DEP(i,a,n) 			 for(int _tmp=n,i=a;i>=_tmp;--i)
#define rep(i,a,n) 			 for(int i=(a);i<(n);++i)
#define dep(i,a,n) 			 for(int i=(a);i>=(n);--i)
#define test() 				 ll T;read(T);while(T--)
#define ALL(x,S) 			 for(__typeof((S).end()) x=S.begin();x!=S.end();x++)
#define eps 				1e-8
#define pi 					3.1415926535897
#define sqr(x) 				((x)*(x))
#define MAX(a,b) 			a=max(a,b)
#define MIN(a,b) 			a=min(a,b)
#define SZ(x) 				((int)(x).size())
#define CPY(a,b) 			memcpy(a,b,sizeof(a))
#define CLR(a) 				memset(a,0,sizeof(a))
#define POSIN(x,y) 			(1<=(x)&&(x)<=n&&1<=(y)&&(y)<=m)
#define all(x) 				(x).begin(),(x).end()
#define COUT(S,x) 			cout<<fixed<<setprecision(x)<<S<<endl
typedef long long int ll;
typedef double lf;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<lf,lf> pff;
const int inf=0x20202020;
const int mod=1000000007;
const int DX[]={1,0,-1,0},DY[]={0,1,0,-1};
ll powmod(ll a,ll b) {ll res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
ll powmod(ll a,ll b,ll mod) {ll res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
ll gcd(ll a,ll b) { return b?gcd(b,a%b):a;}
//////////////////////////////////////////////////////////////////////////////
int main() {
#ifndef ONLINE_JUDGE
	freopen("1.in","rt",stdin);
	freopen("1.out","wt",stdout);
#endif
	string str;
    int T,n,cnt=0,temp=0,i,j;
    cin>>T;
    REP(j,1,T){
           cin>>n;
           cin>>str;
           cnt=0;
           temp=0;
           int l=str.length();
           for(i=0;i<l;++i){
           	     int s=str[i]-'0';
           	     if(i==0){
           	     	temp=temp+s;continue;}
           	     if(i<=temp) temp=temp+s;
           	     else {
           	     	cnt=cnt+(i-temp);
           	     	temp=temp+s+(i-temp);
           	     }

          }
          
           cout<<"Case #"<<j<<": "<<cnt<<endl;
    }
	return 0;
}