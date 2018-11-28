//#pragma warning (disable: 4786)
//#pragma comment (linker, "/STACK:16777216")

#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<iostream>
#include<fstream>
#include<iomanip>
#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
#define maxim 100
#define LLD long long int
#define LLU long long unsigned
#define HD short int
#define HU short unsigned
#define ui unsigned
#define pi acos(-1.0)
#define inf (1<<29)
#define CLR(a) memset(a,0,sizeof(a))
#define SET(a) memset(a,-1,sizeof(a))
#define pb push_back
#define sz(a) ((int)a.size())
#define all(a) a.begin(),a.end()
#define eps 1e-9
#define rep(i,init,n) for(i=init;i<n;i++)
#define rem(i,init,n) for(i=init;i>n;i--)
#define foreach(i, c) for( __typeof( (c).begin() ) i = (c).begin(); i != (c).end(); ++i )
#define _abs(a) ((a)<0?(-(a)):(a))
#define area(x1,y1,x2,y2,x3,y3) ( x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2) )
#define sqr(x) ((x)*(x))
#define distSqr(x1,y1,x2,y2) ( sqr(x1-x2) + sqr(y1-y2) )
#define spDist(lat1,long1,lat2,long2,r) ( r * acos( sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(long1-long2) ) )
#define isEq(a,b) (fabs(a-b)<eps)
#define STR string
#define LF double
#define IT iterator
#define VI vector<int>
#define VLLD vector<LLD>
#define VS vector<STR>
#define VLF vector<LF>
#define MII map<int,int>
#define MIB map<int,bool>
#define MSI map<STR,int>
#define MSB map<STR,bool>
#define MSS map<STR,STR>
#define M2dII map<int,map<int,int> >
#define QI queue<int>
#define SI stack<int>
#define PII pair< int, int >
#define PPI pair< PII, int >
#define ff first
#define ss second
#define VPII vector<PII>
#define MP make_pair

#define chk(a,k) ((bool)(a&(1<<(k))))
#define set0(a,k) (a&(~(1<<(k))))
#define set1(a,k) (a|(1<<(k)))

#define chkA(a,k) (bool)(a[(k)>>5] & (1<<((k)&31)))
#define setA0(a,k) (a[(k)>>5] &= ~(1<<((k)&31)))
#define setA1(a,k) (a[(k)>>5] |= (1<<((k)&31)))

#define SD(a) scanf("%d",&a)
#define SU(a) scanf("%u",&a)
#define SHD(a) scanf("%hd",&a)
#define SHU(a) scanf("%hu",&a)
#define SLLD(a) scanf("%lld",&a)
#define SLLU(a) scanf("%llu",&a)
#define SF(a) scanf("%f",&a)
#define SLF(a) scanf("%lf",&a)
#define SC(a) scanf("%c",&a)
#define SS(a) scanf("%s",a)

int diru[] = {-1,-1,-1,0,0,1,1,1};
int dirv[] = {-1,0,1,-1,1,-1,0,1};

using namespace std;

#define DEB(args...) {dbg,args; cerr<<endl;}
struct debugger { template<typename T> debugger& operator,(const T& v) { cerr<<v<<" "; return *this; } } dbg ;

template< class T > T sq(T n) { return n*n; }
template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }
template< class T > bool inside(T a, T b, T c) { return a<=b && b<=c; }
template< class T > void setmax(T &a, T b) { if(a < b) a = b; }
template< class T > void setmin(T &a, T b) { if(b < a) a = b; }
template< class T > T power(T N,T P){  return (P==0)?  1: N*power(N,P-1); }

LF dp[22][22][22][22] ;
bool isV[22][22][22][22] ;
int x,y ;

LF cal(int n, int level, int l, int r, int a, int b, int lastx, int lasty)
{
          //DEB(lastx,lasty) ;

          if(lastx==x && lasty==y)      return 1 ;
          if(n==0)            return 0 ;

          if(isV[n][level][l][r])                 return dp[n][level][l][r] ;

          LF ret ;

          if(l==a+1 && r==b+1)          ret = cal(n-1,level+1,0,0,a+2,b+2,0,level*2) ;
          else if(l==a+1)                     ret = cal(n-1,level,l,r+1,a,b,(level)*2-r,r) ;
          else if(r==b+1)                     ret = cal(n-1,level,l+1,r,a,b,-(level)*2+l,l) ;
          else
          {
                    ret = ( cal(n-1,level,l+1,r,a,b,-(level)*2+l,l) + cal(n-1,level,l,r+1,a,b,(level)*2-r,r) ) / (LF)2.0 ;
          }

          isV[n][level][l][r] = 1 ;

          return dp[n][level][l][r] = ret  ;
}

int main()
{
	int n,T,t=1,m,i,j,k;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	//while(scanf("%d",&n)==1)
	{
	          SD(n) ;
	          SD(x) ;
	          SD(y) ;
	          CLR(isV) ;

	          printf("Case #%d: %.12lf\n",t,cal(n-1,1,0,0,1,1,0,0));

		//rep(i,0,n)
			//scanf("%d",&m);
		//printf("Case %d: ",t);
	}
	return 0;
}
