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


int N,P,R,S;

string sorted(string x) {
  sort(ALL(x));
  return x;
}

int getOrder(char x, string order) {
  if(order[0]==x) return 0;
  if(order[1]==x) return 1;
  if(order[2]==x) return 2;
}

pair<int,int> getSortedPair(int x, int y) {
  if(x<y) return MP(x,y);
  return MP(y,x);
}

bool solvable(int p, int r, int s, string &ret, string order) {
  if( (p+r+s)==1) {
    if(p>0) ret += "P";
    if(r>0) ret += "R";
    if(s>0) ret += "S";
    return true;
  }
  int np=0, nr=0, ns=0;
  vector<pair<int, string> > e;
  e.PB(MP(p,"p"));
  e.PB(MP(r,"r"));
  e.PB(MP(s,"s"));
  sort(ALL(e));
  //printf("%d %d %d\n",e[0].first, e[1].first, e[2].first);

  map<string, int> poc;
  poc["pr"]=0;
  poc["rs"]=0;
  poc["ps"]=0;  

  // e2 s e0
  int d = (e[2].first - e[1].first);
  poc[sorted(""+e[2].second+""+e[0].second)] += d;
  e[2].first -= d;
  e[0].first -= d;
  if(e[0].first < 0 ) return false;

  //printf("%d %d %d\n",e[0].first, e[1].first, e[2].first);

  assert(e[0].first %2 == 0);
  d = e[0].first / 2;
  poc[sorted(e[0].second + e[1].second)] += d;
  poc[sorted(e[0].second + e[2].second)] += d;
  e[0].first -= d;
  e[0].first -= d;
  e[1].first -= d;
  e[2].first -= d;  
  //printf("%d %d %d\n",e[0].first, e[1].first, e[2].first);  

  d = e[1].first;
  poc[sorted(e[1].second + e[2].second)] += d;
  e[1].first -= d;
  e[2].first -= d;
  //printf("%d %d %d\n",e[0].first, e[1].first, e[2].first);
  assert(e[0].first ==0);
  assert(e[1].first ==0);
  assert(e[2].first ==0);  
  np = poc["pr"];
  nr = poc["rs"];
  ns = poc["ps"];
  string rett = "";

  // vypocitat novy ordering..
  pair<int,int> ordP = getSortedPair(getOrder('P',order), getOrder('R', order));
  pair<int,int> ordR = getSortedPair(getOrder('R',order), getOrder('S', order));
  pair<int,int> ordS = getSortedPair(getOrder('P',order), getOrder('S', order));
  vector<pair<pair<int,int>, char > > ordSort;
  string newOrder = "";
  ordSort.PB(MP(ordP, 'P'));
  ordSort.PB(MP(ordR, 'R'));  
  ordSort.PB(MP(ordS, 'S'));
  sort(ALL(ordSort));
  FOR(i,3) newOrder += ordSort[i].second;
  bool solv = solvable(np, nr, ns, rett, newOrder );
  if(!solv) return false;
  // rett rozmenit.. podla order..
  ret = "";
  FORSZ(i,rett) {
    if(rett[i]=='P') {
      if(getOrder('P',order) < getOrder('R', order))
        ret += "PR";
      else
        ret += "RP";
    }
    if(rett[i]=='S') {
      if(getOrder('P',order) < getOrder('S', order))      
        ret += "PS";
      else 
        ret += "SP";
    }
    if(rett[i]=='R') {
     if(getOrder('R',order) < getOrder('S', order))      
       ret += "RS";
     else 
       ret += "SR";
    }
  }

  return true;
}

void solve(){
  scanf("%d %d %d %d",&N,&R,&P,&S);
  map<string, int> poc;
  string ret = "";
  bool solv = solvable(P,R,S,ret, "PRS");
  if(!solv) {
    printf("IMPOSSIBLE\n");
  } else {
    printf("%s\n",ret.c_str());
  }
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
