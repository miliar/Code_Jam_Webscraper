#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
using namespace std;

typedef long long LL;
#define pb push_back
#define mp make_pair
#define REP(i,n) FOR(i,0,n)
#define FOR(i,a,b) for(int i = a; i < b; i++)
#define ROF(i,a,b) for(int i=a;i>b;i--)
#define GI ({int t;scanf("%d",&t);t;})
#define GL ({LL t;scanf("%lld",&t);t;})
#define GD ({double t;scanf("%lf",&t);t;})
#define GC ({char t;scanf("%c",&t);t;})
#define SET(x,a) memset(x,a,sizeof(x))
#define ALL(x) (x.begin(),x.end())
#define INF (int)1e9
#define fii freopen("in.txt","r",stdin)
#define fio freopen("out.txt","w",stdout)
#define MOD 1000000007
template<class T> inline T big(T a,T b) {return a>b?a:b;} 
template<class T> inline T small(T a,T b) {return a<b?a:b;} 


int main(int argc,char **argv) {
  int kase=GI,s=1;
  while(kase--) {
    printf("Case #%d: ",s++);
    map<int,int> m;
    int t,t1,cnt=0,ans;
    t=GI;
    REP(i,4) REP(j,4) {
      if((i==(t-1))) m[GI]=1;
      else GI;
    }
    t=GI;
    REP(i,4) REP(j,4) {
      t1=GI;
      if((i==(t-1))) if(m[t1])cnt++,ans=t1;
    }
    if(!cnt) printf("Volunteer cheated!\n");
    else if(cnt==1) printf("%d\n",ans);
    else printf("Bad magician!\n");
  }


}
