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
#include <sys/resource.h>
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
void stackSizeUnlimited() { struct rlimit rl; getrlimit(RLIMIT_STACK, &rl); rl.rlim_cur = RLIM_INFINITY; setrlimit(RLIMIT_STACK, &rl); }
///////////////////////////////////////////////////////////////////////////////////
// }}}

int n,m;
int ret;
char a[105][105];
int ps[105];
int pr[105];
bool res[105][105];
bool vis[105][105];

bool dnu(int x, int y) {
  return (0<=x && x<n && 0<=y && y<m);
}

pair<int,int> getDif(char x) {
  if(x=='^') return MP(-1,0);
  if(x=='>') return MP(0,+1);
  if(x=='v') return MP(+1,0);
  if(x=='<') return MP(0,-1);
}

void resolve(int x, int y, pair<int,int> dif) {
  if(!dnu(x,y)) {
    ret++;
    return;
  }
  if(a[x][y]=='.') {
    resolve(x+dif.first, y+dif.second, dif);
    return;
  }  
  if(res[x][y]) return;
  if(vis[x][y]) return;
  vis[x][y]=true;
  res[x][y]=true;
  pair<int,int> diff = getDif(a[x][y]);    
  resolve(x+diff.first, y+diff.second, diff);
}

void solve(){
  ret = 0;
  scanf("%d %d\n",&n,&m);
  FOR(i,n) scanf("%s\n",a[i]);
  CL(ps);
  CL(pr);  
  FOR(i,n) FOR(j,m) if(a[i][j]!='.') { pr[i]++; ps[j]++; }
  FOR(i,n) FOR(j,m) if(a[i][j]!='.' && pr[i]==1 && ps[j]==1) {
    printf("IMPOSSIBLE\n"); 
    return;
  }
  CL(res); CL(vis);
  FOR(i,n) FOR(j,m) if(a[i][j]!='.') if(!res[i][j]) {
    resolve(i,j,getDif(res[i][j]));
  }
  printf("%d\n",ret);
  return;
}

int main(){
  stackSizeUnlimited();
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);

     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
