/* theCodeGame */
//{{{
#include<iostream>
#include<algorithm>
#include<cmath>
#include<climits>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<deque>
#include<stack>
#include<bitset>
#include<set>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<ctime>
#include<map>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>
#include<iomanip>
#include<cctype>
//#undef thecodegame
#ifdef thecodegame
    #include<debug.h>
#else
    #define DBG_ARR(a,b,c) {}
    #define DBG_MAT(a,s,b,c) {}
    #define DBG_VECT(a) {}
    #define db(...) {}
    #define dbt(x, ...) {}
#endif

using namespace std;

#define assert(f) {if(!(f)){fprintf(stderr,"Line-->%d  Assertion failed: %s \n",__LINE__,#f);exit(1);}}
#define MOD 	 1000000007LL
#define LL 		 long long
#define ULL      unsigned long long
#define ABS(x)   ((x)<0?-(x):(x))
#define SQR(x) 	 ((x)*(x))
#define CUBE(x)  ((x)*(x)*(x))
#define SD(n)    scanf("%d",&n)
#define SD2(n,m) scanf("%d %d",&n,&m)
#define SLL(n)   scanf("%LLd",&n)
#define SLU(n)   scanf("%LLu",&n)
#define SS(n)    scanf("%s",n)
#define pnl      printf("\n")
#define REP(i,n)        for(__typeof(n) i=0;i<(n);i++)
#define FOR(i,a,b)      for(__typeof(b) i=(a);i<(b);++i)
#define FORE(i,a,b)     for(__typeof(b) i=(a);i<=(b);++i)
#define FORD(i,a,b,d)   for(__typeof(b) i=(a);i<(b);i+=(d))
#define FORR(i,n,e)     for(__typeof(n) i=(n);i>=(e);--i)
#define FORRD(i,n,e,d)  for(__typeof(n) i=(n);i>=(e);i-=(d))
#define REP_IT(it,m)    for(it=m.begin();it!=m.end();it++)
#define FORI(it,s) 	    for(__typeof((s).begin()) (it)=(s).begin();(it)!=(s).end();(it)++)
#define FOREACH(it, X)  for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define UNIQUE(v)       sort(aLL(v)),v.erase(unique(aLL(v)),v.end())
#define FILL(a,b)       memset(a,b,sizeof(a))
#define ALL(v)          (v).begin(), (v).end()
#define RALL(v)         (v).rbegin(), (v).rend()
#define checkbit(n,b)    ( ((n) >> (b)) & 1)
#define pb push_back
#define mp make_pair
#define XX first
#define YY second

const double PI=acos(-1.0);
const double EPS=1e-11;
template<typename T>inline T mod(T N,T M){return (N%M+M)%M;}
template<typename T>inline void checkmin(T &a,T b){if(b<a)a=b;}
template<typename T>inline void checkmax(T &a,T b){if(b>a)a=b;}
class minHeap{public:bool operator()(int& c1,int& c2){return c1>c2;}};
class maxHeap{public:bool operator()(int& c1,int& c2){return c1<c2;}};


//}}}
#define SIZE 20
#define MAXX 100000009
int n,m,a[101][101];
int row(int i)
{
    int t=a[i][0];
    for(int j=0;j<m;j++)
    if(a[i][j]!=t) return 0;
    return 1;
    }
int column(int j)
{
    int t=a[0][j];
    for(int i=0;i<n;i++)
    if(a[i][j]!=t) return 0;
    return 1;
    }
void precompute(){

}//end precompute

void doThis(int jkl){
                    int trace=1;
                  cin>>n>>m;
                  for(int i=0;i<n;i++)
                  for(int j=0;j<m;j++)
                  cin>>a[i][j];
                  int max=a[0][0];
                  for(int i=0;i<n;i++)
                  for(int j=0;j<m;j++)
                  if(a[i][j]>max) max=a[i][j];
                  int to[101][101];
                  for(int i=0;i<n;i++)
                  for(int j=0;j<m;j++)
                  to[i][j]=max;
                  for(int i=0;i<n;i++)
                  if(row(i)==1) {
                                int tem=a[i][0];
                                for(int j=0;j<m;j++)
                                to[i][j]=tem;
                                }
                  for(int j=0;j<m;j++)
                  {
                          if(column(j)==1) {
                                           int tem=a[0][j];
                                           for(int i=0;i<n;i++)
                                           to[i][j]=tem;
                                           }
                  }

                  for(int i=0;i<n;i++)
                  for(int j=0;j<m;j++)
                  if(a[i][j]!=to[i][j]) {trace=0;break;}
                  if(trace==1) cout<<"Case #"<<jkl<<": YES"<<endl;
                  else cout<<"Case #"<<jkl<<": NO"<<endl;

}//end solve

int main(){
#ifdef amy
	freopen("C:\\A\\in.txt","r",stdin);freopen("C:\\A\\out.txt","w",stdout);freopen("C:\\A\\out.txt","w",stderr);
#endif
precompute();
int cases = 1;
scanf("%d",&cases);
FORE(i,1,cases){doThis(i);}
#ifdef amy
#endif
return 0;
}//end main
