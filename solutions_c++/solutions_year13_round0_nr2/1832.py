// pre-written code {{{
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <numeric>
#include <iostream>
#include <cassert>
#include <set>
#define FOR(i,n) for(int _n=n,i=0;i<_n;++i)
#define FR(i,a,b) for(int _b=b,i=a;i<_b;++i)
#define CL(x) memset(x,0,sizeof(x))
#define PN printf("\n");
#define MP make_pair
#define PB push_back
#define SZ size()
#define ALL(x) x.begin(),x.end()
#define FORSZ(i,v) FOR(i,v.size())
#define FORIT(it,x) for(__typeof(x.begin()) it=x.begin();it!=x.end();it++)
using namespace std;
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
///////////////////////////////////////////////////////////////////////////////////
// }}}

int n,m;
int a[105][105];
int sm[105],rm[105];

void solve(){
  scanf("%d %d",&n,&m);
  FOR(i,n) FOR(j,m) scanf("%d",&a[i][j]);
  CL(sm); CL(rm);
  FOR(i,n) FOR(j,m) {
    rm[i] = max(rm[i],a[i][j]);
    sm[j] = max(sm[j],a[i][j]);    
  }
  bool ok=true;
  FOR(i,n) FOR(j,m) if(a[i][j] < min(rm[i],sm[j])) ok=false;
  if(ok) printf("YES\n"); else printf("NO\n");
}

int main(){
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);

     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
