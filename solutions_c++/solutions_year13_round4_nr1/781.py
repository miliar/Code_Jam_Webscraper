#include <cstdio>
#include <algorithm>
using namespace std;
#define gm(x,y) (((x)%(y)+(y))%(y))

int T, N, M;
int oo, ee, pp;

struct event {
  int pos, n, d;
}e[2005];

int E;

bool cmp(event a, event b) {
  if (a.pos != b.pos) return a.pos < b.pos;
  else return a.d > b.d;
}

int sp[2005];
int sn[2005];
int s;

long long ans1, ans2;
long long mod = 1000002013;

int main() {
  scanf("%d", &T);
  for (int tc=1;tc<=T;++tc) {
    ans1 = ans2 = 0;
    scanf("%d%d", &N, &M);
    E = 0;
    for (int i=0;i<M;++i) {
      scanf("%d%d%d", &oo, &ee, &pp);
      long long k = ee-oo;
      ans1 = (ans1 + ((k*(1+k)/2)%mod * pp)%mod) % mod;
      
      e[E].pos = oo;
      e[E].n = pp;
      e[E].d = 1;
      ++E;
      e[E].pos = ee;
      e[E].n = pp;
      e[E].d = -1;
      ++E;
    }
    
    sort(e, e+E, cmp);
    s = 0;
    
    for (int i=0;i<E;++i) {
      if (e[i].d == 1) {
	sp[s] = e[i].pos;
	sn[s] = e[i].n;
	++s;
      } else {
	int n = e[i].n;
	while (n) {
	  if (n >= sn[s-1]) {
	    long long k = e[i].pos - sp[s-1];
	    long long ppp = sn[s-1];
	    ans2 = (ans2 + ((k*(1+k)/2)%mod * ppp)%mod) % mod;
	    
	    n -= sn[s-1];
	    --s;
	  } else {
	    long long k = e[i].pos - sp[s-1];
	    long long ppp = n;
	    ans2 = (ans2 + ((k*(1+k)/2)%mod * ppp)%mod) % mod;
	    
	    sn[s-1] -= n;
	    n = 0;
	  }
	}
      }
    }
    
    printf("Case #%d: %lld\n", tc, gm(ans2 - ans1, mod));
  }
  return 0;
}