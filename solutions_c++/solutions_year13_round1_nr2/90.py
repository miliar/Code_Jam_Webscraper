#include <algorithm>
typedef long long ll;

#include <queue>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <set>
#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }

using namespace std;

int main(){
  const int T = getInt();

  REP(cc, T){
    const int e = getInt();
    const int r = getInt();
    const int n = getInt();
    vector<int> v(n);
    vector<pair<int, int> > s(n);

    REP(i,n){
      v[i] = getInt();
      s[i].first  = v[i];
      s[i].second = -i;
    }
    sort(s.rbegin(), s.rend());

    vector<int> mustHave(n);
    vector<int> canUse(n);
    REP(i,n) mustHave[i] = e;
    REP(i,n) canUse[i]   = 0;

    REP(i,n){
      const int p = -s[i].second;
      for(int j = p - 1, now = mustHave[p] - r;
	  j >= 0;
	  j--, now = max(0, now - r)){
	canUse[j] = max(now, canUse[j]);
      }
      for(int j = p + 1, now = canUse[p] + r;
	  j < n;
	  j++, now = min(e, now + r)){
	mustHave[j] = min(now, mustHave[j]);
      }
    }
    // REP(i,n) printf("(%d %d) ", mustHave[i], canUse[i]); puts("");

    ll ans  = 0;
    int now = e;
    REP(i,n){
      if(now > canUse[i]){
	ans += static_cast<ll>(v[i]) * (now - canUse[i]);
	now = canUse[i];
      }
      now = min(e, now + r);
    }

    printf("Case #%d: %lld\n", cc + 1, ans);
  }

  return 0;
}
