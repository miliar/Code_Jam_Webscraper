#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
#include <map>
#define SZ(x) ((int)(x).size())
#define FOR(it, c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
using namespace std;
typedef long long LL;

int cs;
int lev=0;

bool go(vector<LL> &ans, vector<pair<LL, LL> > a, LL prev) {
  ++lev;
  fprintf(stderr,"lev=%d %d\n", lev, SZ(a));
  /*fprintf(stdout,"prev=%lld; ", prev);
  FOR(it, a) { fprintf(stdout,"(%lld, %lld) ", it->first, it->second); }
  fprintf(stdout, "\n");*/

  if (SZ(a)==1) return true;
  LL now=prev;
  map<LL, LL> f;
  for(int z=0;z<SZ(a);z++) {
    if(a[z].first < prev || a[z].first == 0) continue;

    f.clear();
    for(int j=0;j<SZ(a);j++) f[a[j].first] = a[j].second;

    now=a[z].first;
    if (now < 0) {
      for(int i=SZ(a)-1;i>=0;i--) {
        LL p = f[a[i].first];
        f[a[i].first + now] -= p;
      }
    } else {
      for(int i=0;i<SZ(a);i++) {
        LL p = f[a[i].first];
        f[a[i].first + now] -= p;
      }
    }
    int bad=0;
    FOR(it, f) if (it->second < 0) { { bad=1; break; }}
    if(bad==1) continue;

    ans.push_back(now);
    vector<pair<LL, LL> > b;
    FOR(it, f) if(it->second > 0) b.push_back(make_pair(it->first, it->second));
    if (go(ans, b, now)) { return true; }
    ans.pop_back();
  }
  --lev;
  return false;
}

void solve() {
  int P;
  scanf("%d", &P);
  vector<pair<LL, LL> > a(P);
  for(int i=0;i<P;i++) scanf("%lld", &a[i].first);
  for(int i=0;i<P;i++) scanf("%lld", &a[i].second);
  sort(a.begin(), a.end());

  LL g = a[0].second;
  for(int i=0;i<P;i++)
    g = __gcd(a[i].second, g);

  vector<LL> ans;
  LL nzero = 0;
  while((1LL<<nzero) < g) ++nzero;
  for(int i=0;i<nzero;i++) ans.push_back(0LL);
  for(int i=0;i<P;i++) a[i].second /= g;
  
  //now we have no zeros, hopefully
  go(ans, a, a[0].first);
  sort(ans.begin(), ans.end());

  printf("Case #%d:", cs);
  for(int i=0;i<SZ(ans);i++) printf(" %lld", ans[i]);
  puts("");
  
  fprintf(stderr, "Case #%d:", cs);
  for(int i=0;i<SZ(ans);i++) fprintf(stderr, " %lld", ans[i]);
  fprintf(stderr, "\n");
}

int main(void) {
  int T;
  scanf("%d", &T);
  for(cs=1;cs<=T;cs++) solve();
  return 0;
}
