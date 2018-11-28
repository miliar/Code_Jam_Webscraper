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

int node ;
char in[3844496] ;
int trie[1125087][27] ;
map<int,int> dp[5][1125087] ;
int cs ;

void ins(char *s)
{
          int i,cur=0 ;

          for(i=0;s[i];i++)
          {
                    if(trie[cur][s[i]-'a']==0)
                              trie[cur][s[i]-'a'] = ++node ;

                    cur = trie[cur][s[i]-'a'] ;
          }

          trie[cur][26] = 1 ;
}

int cal(int cur, int i, int last)
{
          if(in[i]==0)
          {
                    return trie[cur][26] ? 0 : 4001 ;
          }

          if(last>4)          last = 4 ;

          if(dp[last][cur].find(i) != dp[last][cur].end())   return dp[last][cur][i] ;

          int ret = 4001,j ;

          if(trie[cur][26])             ret = min(ret,cal(0,i,last)) ;

          if(trie[cur][in[i]-'a'])      ret = min(ret,cal(trie[cur][in[i]-'a'],i+1,last+1)) ;

          if(last>3)
                    rep(j,0,26)
                    {
                              if(j != in[i]-'a' && trie[cur][j])
                              {
                                        ret = min(ret,1+cal(trie[cur][j],i+1,0)) ;
                              }
                    }

          return dp[last][cur][i] = ret ;
}

int main()
{
	int n,T,t=1,m,i,j,k;
	FILE * fp = fopen ("garbled_email_dictionary.txt","r");

	while(fscanf (fp, "%s", in) == 1)
	{
	          ins(in) ;
	}

	//DEB(node) ;

	//puts("sds") ;

	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	//while(scanf("%d",&n)==1)
	{
	          SS(in) ;

	          printf("Case #%d: %d\n",t,cal(0,0,4));

	          rep(i,0,5)
                              rep(j,0,1125087)
                                        dp[i][j].clear() ;

		//rep(i,0,n)
			//scanf("%d",&m);
		//printf("Case %d: ",t);
	}
	return 0;
}
