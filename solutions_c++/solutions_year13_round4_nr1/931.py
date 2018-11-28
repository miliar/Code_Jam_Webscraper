//Tadrion
#include <cstdio>
#include <vector>
#include <iostream>
#include <deque>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>
using namespace std;
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define CLEAR(x) (memset(x,0,sizeof(x)))
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#define VAR(v, n) __typeof(n) v = (n)
#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define FOREACH(i, c) for(VAR(i,(c).begin()); i != (c).end(); ++i)
#define DBG(v) cout<<#v<<" = "<<v<<endl; 
#define IN(x,y) ((y).find(x)!=(y).end())
#define ST first
#define ND second
#define PB push_back
#define PF push_front
#define MP make_pair
typedef long long int LL;
typedef pair<int,int> PII;
typedef vector<int> VI;

int T,N,M;
int o,e,c;

const LL MOD = 1000002013LL;

LL c1(int o, int e) {
  LL res = 0;
  int cnt = e-o;
  FOR(i,1,cnt) {
    res += N+1-i;
    res%=MOD;
  }
  return res;
}

multiset< pair<int,int> > s;

void eraseOne(PII p) {
  s.erase(s.find(p));
}

int main() {  
  scanf("%d",&T);
  FOR(ttt,1,T) {
    LL resp = 0;
    scanf("%d %d",&N,&M);
    FOR(i,1,M) {
      scanf("%d %d %d",&o,&e,&c);
      resp += c * c1(o,e); 
      resp%=MOD;
      FOR(j,1,c) {
      s.insert(MP(o,-e));
      }
    }
    LL res = 0;
    while(!s.empty()) {
      PII p = *(s.begin());
      eraseOne(p);
      if(p.ST == -p.ND) continue;
      
      int lower = p.ST;
      int upper = -p.ND;
      PII maxx = PII(-1,-1);
      FOREACH(it,s) {
	if(it->ST <= upper && -it->ND > upper) {
	  maxx = MAX(maxx,*it);
	}
	//	printf("%d %d\n",maxx.ST,maxx.ND);
      }
      if(maxx == PII(-1,-1)) {
	res += c1(lower,upper);
	res%=MOD;
      }
      else {
	int lower2=maxx.ST;
	int upper2=-maxx.ND;
	eraseOne(maxx);
	s.insert(MP(lower,-upper2));
	s.insert(MP(lower2,-upper));
      }
      
    }
    
    //LL res = calc();
    printf("Case #%d: %lld\n",ttt,(resp-res+MOD+MOD)%MOD);
  }
  return 0;
}
