#include <cmath>
#include <iostream>
typedef long long ll;

#include <queue>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }

#include <set>
using namespace std;

ll get(const vector<ll> &v, int i){
  if(i == 0) return 0;
  return v[i - 1];
}

long double solve(){
  const int n = getInt();
  const int p = getInt();
  const int q = getInt();
  const int r = getInt();
  const int s = getInt();

  vector<ll> v(n);
  REP(i,n) v[i] = ((ll)i * p + q) % r + s;

  REP(i,n-1) v[i+1] += v[i];
  const ll all = v[n - 1];

  long double ret = 1.0;
  for(int i = 0; i <= n; i++){
    const ll rest = get(v, n) - get(v, i);
    const ll exp = get(v, i) + rest / 2;
    const int idx = lower_bound(v.begin(), v.end(), exp) - v.begin();

    if(idx == n) continue;

    const ll a = get(v, i);

    for(int j = -5; j <= 5; j++){
      const int ii = idx + j;
      if(ii < 0) continue;
      if(ii > n) continue;
      const ll b = get(v, ii) - get(v, i);
      const ll c = get(v, n) - get(v, ii);

      if(a + b + c != all) throw "error";
      const ll mx = max(a, max(b, c));
      ret = min(ret, (long double)mx / all);
    }
  }

  return ret;
}

int main(){
  const int t = getInt();
  REP(i,t){
    printf("Case #%d: %.10f\n", i + 1, 1.0 - (double)solve());
  }
  return 0;
}










