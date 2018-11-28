#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<string>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<string>
 
using namespace std;
#define s(n)                    scanf("%d",&n)
#define sf(n)                   scanf("%lf",&n)
#define ss(n)                   scanf("%s",n)
#define sc(n)                   {char temp[4]; ss(temp); n=temp[0];}
#define INF                     (int)1e9
#define LINF                    (long long)1e18
#define swap(a,b)                int temp; temp=a;a=b;b=temp;
#define EPS                     1e-9
#define maX(a,b)                ((a)>(b)?(a):(b))
#define miN(a,b)                ((a)<(b)?(a):(b))
#define abS(x)                  ((x)<0?-(x):(x))
#define FOR(i,a,b)              for(int i=a;i<b;i++)
#define FORREV(k,a,b)           for(int i=a;i>b;i--)
#define REP(i,n)                FOR(i,0,n)
#define REP1(i,n)               FOR(i,1,n)
#define FOREACH(v,c)            for( typeof((c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define CASEN(n)                int cas=1;while(scanf("%d",&n)!=EOF)
#define CASE(T)                 int T;scanf("%d ",&T);while(T--)
//#define mp                      make_pair
#define FF                      first
#define SS                      second
#define tri(a,b,c)              mp(a,mp(b,c))
#define XX                      first
#define YY                      second.first
#define ZZ                      second.second
#define pb                      push_back
#define fill(a,v)               memset(a,v,sizeof a)
#define pb                      push_back  
#define all(x)                  x.begin(),x.end()
#define SZ(v)                   ((int)(v.size()))
#define SORT(v)                 sort((v).begin(),(v).end())
#define DREP(a)                 sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind)          (lower_bound(all(arr),ind)-arr.begin())
#define FILEI                    freopen("input.txt","r",stdin);
#define FILEO                    freopen("out.txt","w",stdout);
#define MOD                      100000000
#define SIZE(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))
#define MP(X,Y) make_pair(X,Y)
typedef long long int64;
typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
 
template<class T> inline T sqr(T x){return x*x;}
typedef pair<int,int> ipair;
template<class T> inline T lowbit(T n){return (n^(n-1))&n;}
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}
 
#define LOCAL 1
#if LOCAL
#define Get getchar()
#else
#define Get getchar_unlocked()
#endif
int getInt() { int a=0,s=1; char c=0; while(c<33) c=Get; if(c=='-') {s=-1; c=Get;} while(c>33) {a=(a<<3)+(a<<1)+c-'0'; c=Get;} return a*s; }
 
///////////////////////////////   ENDTEMPLATE_BY_SAGAR55    ////////////////////////////////

struct data{
    int s;int f;int d;
};
bool my_cmp(const data& a, const data& b)
{
    if(a.d!=b.d) return a.d<b.d;
    if(a.f!=b.f) return a.f<b.f;
    return a.s>b.s;
} 
 
bool cmp(const vector<int>& a,const vector<int>& b){
  for(int i=2;i>=0;i--){
    if(a[i]<b[i])return true;
    else if(a[i]==b[i])continue;
    else return false;
  }
} 
typedef long long LL;
typedef pair<int,int> PII;
typedef pair<LL,LL> PLL;
typedef pair<int,PII> TRI;
 
typedef vector<int> VI;
typedef vector<LL> VL;
typedef vector<PII> VII;
typedef vector<PLL> VLL;
typedef vector<TRI> VT;
 
typedef vector<VI> VVI;
typedef vector<VL> VVL;
typedef vector<VII> VVII;
typedef vector<VLL> VVLL;
typedef vector<VT> VVT;
main()
{
	double a[1005] ,b[1005]; 
FILEO;FILEI;
	int  n,ans1,ans2, p, q,cse=1;
	CASE(T){
		ans1=ans2=0;
		s(n);
		REP(i,n)sf(a[i]);
		REP(i,n)sf(b[i]);
		sort(a,a+n);
		sort(b,b+n);
		p=q=n-1;
		REP(i,n){
			if(a[p] > b[q])
			{
				p--;	
				q--;
				ans1++;
			}
			else
				q--;
		}
		p=q=n-1;
		REP(i,n)
		{
			if(a[p] > b[q])
			{
				p--;
				ans2++;
			}
			else
			{
				p--;
				q--;
			}
		}
 
		printf("Case #%d: %d %d\n", cse++, ans1, ans2);
	}
	return 0;
}