#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#include <assert.h>
#define stream istringstream
#define rep(i,n) for(int i=0; i<(int)n; i++)
#define repv(i,n) for(int i=n-1; i>=0; i--)
#define repl(i,n) for(int i=1; i<=(int)n; i++)
#define replv(i,n) for(int i=n; i>=1; i--)
#define FOR(i,a,b) for(int i=(int)a;i<=(int)b;i++)
#define foreach(i,n) for(__typeof((n).begin())i =(n).begin();i!=(n).end();i++)
#define sz(x) (int)x.size()
#define inf (1061109567)
#define pb(x) push_back(x)
#define ppb pop_back
#define all(x) x.begin(),x.end()
#define mem(x,y) memset(x,y,sizeof(x));
#define eps 1e-9
#define rev reverse
#define pii pair<int,int>
#define pll pair<i64,i64>
#define pmp make_pair
#define sdi(x) scanf("%d",&x)
#define sdii(x,y) scanf("%d%d",&x,&y)
#define sds(x) scanf("%s",x)
#define pfi(x) printf("%d\n",x);
#define uu first
#define vv second
using namespace std;
template<class T> inline T sqr(T x){return x*x;}
template<class T> inline T lcm(T a,T b) {if(a<0)return
lcm(-a,b);if(b<0)return lcm(a,-b);return a*(b/__gcd(a,b));}
template<class T> T power(T N,T P){ return (P==0)?  1: N*power(N,P-1); }
template<class T> string itoa(T a){if(!a) return "0";string ret;for(T i=a; i>0; i=i/10) ret.pb((i%10)+48);reverse(all(ret));return ret;}
typedef  long long i64;
typedef unsigned long long ui64;
double log(double N,double B){  return (log10l(N))/(log10l(B)); }
vector< string > token( string a, string b ) {const char *q = a.c_str();while( count( b.begin(), b.end(), *q ) ) q++;vector< string >
oot;while( *q ) {const char *e = q;while( *e && !count( b.begin(), b.end(), *e ) ) e++;oot.push_back( string( q, e ) );q = e;while( count( b.begin(),
b.end(), *q ) ) q++;}return oot;
}

//bool operator < ( const node& p ) const {      return w < p.w;   }
#define on(n,pos) (n | (1<<(pos)))
#define off(n,pos)  n & ~(1<<pos)
#define ison(n,pos) (bool)(n & (1<<(pos)))
string toBin(int n){ string s; repv(i,32)s+=(ison(n,i)+'0');return s;}
bool eq(long double a,long double b){return fabs(a-b)<eps;}
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)
#define pks printf("Case #%d: ",++ks);

using namespace std;

double a[1111],b[1111];
int n;

int dp[1<<11][1<<11];

int call(int m1,int m2)
{
		if(__builtin_popcount(m1)==n)return 0;
		if(dp[m1][m2]!=-1)return dp[m1][m2];
		int ans=0;
		rep(i,n)if(!ison(m1,i))
		{
			int flag=0;
			repv(j,n)if(!ison(m2,j))
			{
				if(b[j]>a[i])
				{
					flag=1;
					int ret=call(on(m1,i),on(m2,j));
					ans=max(ans,ret);
				}
			}
			if(flag==0)
			rep(j,n)if(!ison(m2,j))
			{
				int add=0;
				if(b[j]<a[i])add=1;
				
				int ret=add+call(on(m1,i),on(m2,j));
					ans=max(ans,ret);
			}
		}
		return dp[m1][m2]=ans;
		
}
int main() {
	
	READ("in");
	WRITE("Dsmall2");
	int t,ks=0;
	cin>>t;
	while(t--)
	{

		mem(dp,-1);
		cin>>n;
		rep(i,n)cin>>a[i];
		rep(i,n)cin>>b[i];
		//cout<<call(0,0)<<endl;
		
		
		
		
		sort(a,a+n);
		sort(b,b+n);
		
		
		int best=0;
		
				bool vis[12]={0};
				int good=0;
				rep(i,n)
				{
					int flag=0,idj=-1;
					rep(j,n)if(!vis[j])
					{
						if(idj==-1)	idj=j;
						if(b[j]>a[i])
						{
							vis[j]=1;
							flag=1;
							break;
						}
					}
					if(!flag)
					{
						vis[idj]=1;
						
						good++;
					}
					best=max(best,good);
				}
				//rep(i,n)cout<<a[i]<<" ";				puts("");				cout<<good<<endl;
		
		
		pks;
		cout<<call(0,0)<<" "<<best<<endl;
		//cerr<<ks<<endl;
		
		
		
		
		
	}
	return 0;
}
