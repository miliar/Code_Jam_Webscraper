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
#define GD ({long double t;scanf("%Lf",&t);t;})
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
    long double c=GD,f=GD,x=GD,t=2.0;
    long double ans=1e9,temp=0.0,prev=0.0;
    ans=x/t;
    prev=c/t;
    int cnt=0;
    while(ans>=temp) {
      t+=f;
      temp=prev+(x/t);
      ans=min(ans,temp);
      prev+=c/t;
    }
    
    printf("%.7Lf\n",ans);
  }
  
}
