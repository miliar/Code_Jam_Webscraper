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
ll n;
const int T = 100;
int t;

int main() {
  scanf("%d ", &t);
  REP(m,t) {
    scanf("%lld ", &n);

    if (!n) {
      printf("Case #%d: INSOMNIA\n", m+1);
      continue;
    }

    set<int> ds;
    REP(i,10) ds.insert(i);

    ll k = n;
    while (1) {
      ll tmp = k;
      int d;
      while (tmp) {
        d = (int)(tmp%10LL);
        ds.erase(d);
        tmp /= 10LL;
      }
      if (!ds.size()) {
        printf("Case #%d: %lld\n", m+1, k);
        break;
      }
      k += n;
    }
  }

  return 0;
}

