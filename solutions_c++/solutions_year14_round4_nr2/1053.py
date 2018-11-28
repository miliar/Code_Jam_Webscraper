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

int n;
VI a;

void solve(){
  scanf("%d",&n);
  a.resize(n);
  FOR(i,n) scanf("%d",&a[i]);  
  int ret = 0;
  FOR(kk,n) {
    int mini = -1;
    FOR(i,n) if(a[i] > 0) if(mini==-1 || a[mini]>a[i]) { mini = i; }
    //vlavo..
    int left=0;
    int right=0;
//    printf("mini: %d\n",mini);
    FOR(i,mini) if(a[i]>0) left++;
    FR(i,mini+1,n) if(a[i]>0) right++;
    ret+= min(left,right);
//    printf("ret: %d %d %d\n",ret, left, right);
    a[mini]=0;
  }
  printf("%d\n",ret);
}

int main(){
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);

     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
