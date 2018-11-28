#include <cstdio>
#include <stack>
#include <algorithm>

using namespace std;

const int M = 2e3+10;

#define llg long long
#define pii pair<llg, llg>

const llg mod = 1000002013;

int n,m;
struct xxx {
  int x,c;
} a[M];

inline llg total (llg a) {
  return (a*(a+1)/2)%mod;
}

inline bool comp (xxx a, xxx b) {
  return a.x != b.x ? a.x < b.x : a.c < b.c;
}

inline llg solve () {
  stack<pii> s;
  scanf ("%d %d", &n, &m);

  llg init = 0;
  for (int i = 0;i < m;i ++) {
    int o,e,p;
    scanf ("%d %d %d", &o, &e, &p);

    init = (init+total (e-o-1)*p)%mod;
    a[i*2].x = o; a[i*2].c = -p;
    a[i*2+1].x = e; a[i*2+1].c = p;
  }

  sort (a, a+m*2, comp);

  llg ans = 0;
  for (int i = 0;i < m*2;i ++) {
    if (a[i].c < 0) {
      s.push (pii (a[i].x, -a[i].c));
    } else {
      while (a[i].c > 0) {
      	pii t = s.top (); s.pop ();
      	llg mi = min (t.second, (llg)a[i].c);

      	ans = (ans+total (a[i].x-t.first-1)*mi)%mod;

      	t.second -= mi;
      	a[i].c -= mi;
      	if (t.second > 0) {
      	  s.push (t);
      	}
      }
    }
  }
  return ((ans-init)%mod+mod)%mod;
}

int main () {
  int test;
  scanf ("%d", &test);

  for (int Case = 1;Case <= test;Case ++) {
    printf ("Case #%d: %lld\n", Case, solve ());
  }
}
