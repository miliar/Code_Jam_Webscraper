/*********************************************************
                                                
         mmmm      #          mmmm   mmmm   mmmm 
  mmm   m"  "m  mmm#   mmm   "   "# "   "# "   "#
 #"  "  #  m # #" "#  #"  #      m"     m"     m"
 #      #    # #   #  #""""    m"     m"     m"  
 "#mm"   #mm#  "#m##  "#mm"  m#mmmm m#mmmm m#mmmm
                                                 
*************************************************************/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>

//defines
#define MOD 1000000007LL
#define SIZE 100000009
#define MAXX 100000009
#define LL long long
#define ULL unsigned long long
#define ABS(x) ((x)<0?-(x):(x))
#define SQR(x) ((x)*(x))
#define CUBE(x) ((x)*(x)*(x))
#define SD(x) inp(x)
#define SD2(n,m) SD(n);SD(m)
#define SLL(n) scanf("%lld",&n)
#define SLU(n) scanf("%llu",&n)
#define SS(n) scanf("%s",n)
#define pnl printf("\n")
#define REP(i,n) for(__typeof(n) i=0;i<(n);i++)
#define FOR(i,a,b) for(__typeof(b) i=(a);i<(b);++i)
#define FORE(i,a,b) for(__typeof(b) i=(a);i<=(b);++i)
#define FORD(i,a,b,d) for(__typeof(b) i=(a);i<(b);i+=(d))
#define FORR(i,n,e) for(__typeof(n) i=(n);i>=(e);--i)
#define FORRD(i,n,e,d) for(__typeof(n) i=(n);i>=(e);i-=(d))
#define REP_IT(it,m) for(it=m.begin();it!=m.end();it++)
#define FORI(it,s) for(__typeof((s).begin()) (it)=(s).begin();(it)!=(s).end();(it)++)
#define FOREACH(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define UNIQUE(v) sort(ALL(v)),v.erase(unique(ALL(v)),v.end())
#define FILL(a,b) memset(a,b,sizeof(a))
#define ALL(v) (v).begin(), (v).end()
#define RALL(v) (v).rbegin(), (v).rend()
#define checkbit(n,b) (((n)>>(b))&1)
#define PB push_back
#define MP make_pair
#define XX first
#define YY second
#define db(...) {}
#define dbt(...) {}
#define TEST int T;cin>>T;FORE(t,1,T)
#define getcx getchar_unlocked
//defines

template<typename T>inline void inp(T &n)
{
  n=0;
  int ch=getcx();
  int sign=1;
  while(ch<'0'||ch>'9')
    {
      if(ch=='-')sign=-1;
      ch=getcx();
    }
  while(ch>='0'&&ch<='9')
    {
      n=(n<<3)+(n<<1)+ch-'0',ch=getcx();
    }
  n=n*sign;
}

using namespace std;
double _st;
void pre()
{
}
void doThis()
{ 
  
}
void end(){
#ifdef dexter
  fprintf(stdout,"\nTIME: %.3lf sec\n",(double)(clock()-_st)/(CLOCKS_PER_SEC));
#endif
}
int main()
{
#ifdef dexter
  freopen("/home/dexter/Desktop/Dropbox/ZONE/inout/input.txt","r",stdin);
  freopen("/home/dexter/Desktop/Dropbox/ZONE/inout/output.txt","w",stdout);
  _st = clock();
#endif
  //  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int f[4][4],s[4][4];
  TEST
    {
      int a,b;
      cin>>a;a--;
      REP(i,4)
	REP(j,4)
	cin>>f[i][j];
      cin>>b;b--;
      REP(i,4)
	REP(j,4)
	cin>>s[i][j];
      int count=0,ans=0;
      REP(i,4)
	REP(j,4)
	if(f[a][i]==s[b][j])
	  {
	    count++;
	    ans = f[a][i];
	  }
      printf("Case #%d: ",t);
      if(count==0)
	cout << "Volunteer cheated!\n";
      if(count==1)
	cout << ans <<endl;
      if(count>1)
	cout << "Bad magician!\n";
    }
  return 0;
}
