#include <bits/stdc++.h>

using namespace std;

#define FOR(i,s,e) for(int (i)=(s);(i)<(int)(e);(i)++)
#define REP(i,e) FOR(i,0,e)
#define RFOR(i,e,s) for(int (i)=(e)-1;(i)>=(int)(s);(i)--)
#define RREP(i,e) RFOR(i,e,0)

#define all(o) (o).begin(), (o).end()
#define psb(x) push_back(x)
#define mp(x,y) make_pair((x),(y))

typedef long long ll;
typedef pair<int, int> PII;
typedef priority_queue<int, vector<int>, greater<int>> PQI;
typedef priority_queue<PII, vector<PII>, greater<PII>> PQII;

const double EPS = 1e-10;
const int N = 32;
int t, n, j;
int c[N];

ll calc_diviser(ll x) {
  for (ll i=2LL; i*i<=x; i++) {
    if (x%i == 0LL) return i;
  }
  return 0LL;
}

int main() {
  scanf("%d ", &t);
  scanf("%d %d", &n, &j);

  puts("Case #1:");
  int cnt = 0;
  FOR(i,1,(int)(1<<n)) {
    if (!(i&1) || !(i&(1<<(n-1)))) continue;
    vector<ll> res;
    FOR(b,2,11) {
      ll x = 0;
      ll bb = 1LL;
      REP(k,n) {
        if ((1<<k)&i) x += bb;
        bb *= (ll)b;
      }
      ll y = calc_diviser(x);
      if (y) res.psb(y);
    }

    if (res.size()==9) {
      RREP(k,n) printf("%d", (1<<k)&i ? 1 : 0);
      REP(k,9) printf(" %lld", res[k]);
      puts("");
      cnt++;
    }
    if (cnt==j) break;
  }

  return 0;
}

