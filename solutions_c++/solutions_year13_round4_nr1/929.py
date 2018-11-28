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

vector<pair<LL, LL> > z;
vector<pair<LL, LL> > k;

LL price(LL dist) {
  return (n + n - (dist - 1)) * dist / 2;
}

void solve(){
  z.clear(); k.clear();
  scanf("%d %d",&n,&m);
  LL v1 = 0;
  FOR(i,m){
    long long x,y;
    LL cnt;
    scanf("%lld %lld %lld",&x,&y,&cnt);
    z.PB(MP(x,cnt));
    k.PB(MP(y,cnt));
    v1 += cnt * price(y-x);    
  }
//  printf("v1: %lld\n",v1);
  sort(ALL(z)); 
  sort(ALL(k));
  LL v2 = 0;
  priority_queue<pair<LL,LL> > Q;
  int i = 0;
  int j = 0;
  while( i < z.size() || j < k.size()) {
    if( i < z.size() && z[i].first <= k[j].first) {
      Q.push(MP(z[i].first, z[i].second)); 
      i++;
    } else {
      // treba vybrat k[j].second prvkov z Q
      LL cnt = k[j].second;
//      printf("%lld %lld\n", k[j].first, k[j].second);
      while(cnt > 0){
        pair<LL, LL> e = Q.top();
//        printf("top: %lld %lld\n",e.first, e.second);
        Q.pop();
        v2 += min(cnt, e.second) * price(k[j].first - e.first);
        LL delta = min(cnt, e.second);
        cnt -= delta;
        e.second -= delta;
        if(e.second > 0) {
          Q.push(e);
        }
      }
//      printf("v2: %lld\n",v2);
      j++;
    }
  }
//  printf("%lld\n",v2);
  printf("%lld\n",v1 - v2);
}

int main(){
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);

     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
