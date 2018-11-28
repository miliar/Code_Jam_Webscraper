#include <cstdio>
#include <algorithm>

using namespace std;

const int N = 60;

#define llg long long

llg n,p,a[N];

inline void solve () {
  scanf ("%lld %lld", &n, &p);
  llg x = p-1,w = 0;
  for (int i = n-1;i >= 0;i --) {
    a[i] = x%2;
    x /= 2;
    w += a[i];
  }

  llg nub = 0;
  for (int i = 0;i < n;i ++) {
    if (a[i] == 1) {
      nub = n-i-1;
      break;
    }
  }

  w = max (w, nub);
  w = n-w;
  llg ans2 = (1ll<<n)-(1ll<<w);

  llg cnt = 0;
  for (int i = 0;i < n;i ++) {
    if (a[i] == 0) {
      break;
    }
    cnt ++;
  }
  llg ans1 = (1ll<<(cnt+1))-2ll;
  if (p == (1ll<<n)) {
    ans1 = p-1;
  }

  printf ("%lld %lld\n", ans1, ans2);
}

int main () {
  int test;
  scanf ("%d", &test);

  for (int Case = 1;Case <= test;Case ++) {
    printf ("Case #%d: ", Case);
    solve ();
  }
}
