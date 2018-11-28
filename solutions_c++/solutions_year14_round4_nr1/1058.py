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

int x,n;
VI s;

bool solvable(int h) {
  if(h==n) return true;
  if(h*2<n) return false;
  int o = n - h;
  FOR(i,o) {
    //printf("%d %d\n",s[i],s[2*o-i-1]);
    if(s[i]+s[2*o-i-1] >x) return false;
  }
  return true;
}

void solve(){
  scanf("%d %d",&n,&x);  
  s.clear();
  s.resize(n);
  FOR(i,n) scanf("%d",&s[i]);
  sort(ALL(s));
  int left=0;
  int right=n+1;
  while(right-left>5) {
    int mid = (left+right)/2;
    if(solvable(mid)) {
      right = mid;
    } else {
      left = mid;
    }
  }
  //printf("%d\n",solvable(2));
//  printf("%d\n",solvable(right));
//  printf("%d %d\n",left,right);
  FR(i,left,right+1) if(solvable(i)) { printf("%d\n",i); return ;  }


}

int main(){
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);

     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
