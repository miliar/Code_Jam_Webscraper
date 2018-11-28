#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

const int MAXN = 1 << 20;
int n, p, q, r, s;
int a[MAXN];
long long pref[MAXN];

void solve (){
  scanf("%d%d%d%d%d", &n, &p, &q, &r, &s);
  for (int i = 0; i < n; ++i)
    a[i] = (i*(long long)p + q)%r + s; 

  pref[0] = a[0];
  for (int i = 1; i < n; ++i)
    pref[i] = pref[i-1] + a[i];

  long long best = 1LL << 60LL;
  int pos = 0;
  for (int i = 0; i < n; ++i){
    
    pos = max(pos, i);
    while (pref[n-1] - pref[pos] > best) ++pos;

    for (int j = pos; j < n; ++j){
      long long pos0, pos1, pos2;
      pos0 = pos1 = pos2 = 0;
      if (i > 0) pos0 = pref[i-1];
      if (j < n-1) pos1 = pref[n-1] - pref[j];
      pos2 = pref[j];
      if (i > 0) pos2 -= pref[i-1];
      long long s = max(pos0, pos1);
      s = max(s, pos2);
      if (pos0 > best || pos2 > best) break;
      best = min(best, s);
    }
  }

  printf("%.10lf\n", 1 - best*1.0/pref[n-1]);
}

int main (void){
  int tc; scanf ("%d", &tc);
  for (int i = 1; i <= tc; ++i){
    printf("Case #%d: ", i);
    solve();
  }

  return 0;
}


