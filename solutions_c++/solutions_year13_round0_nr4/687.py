#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <complex>
#include <numeric>
#include <bitset>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>

using namespace std;

#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define FOR(i, a, b) for (int i(a), _b(b); i < _b; ++i)
#define REP(i, n) FOR (i, 0, n)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define FORE(e, v) for (int e = head[v]; e >= 0; e = E[e].next)
#define UN(a) sort(all(a)), (a).erase(unique(all(a)), (a).end())
#define CL(a, v) memset(a, v, sizeof a)
#define pb push_back
#define X first
#define Y second

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

const int INF = 1000000000;
const ll INF_LL = 1000000000000000000LL;
const double pi = 2 * acos(0.0);

template<class T> void smin(T& a, T b) { if (a > b) a = b; }
template<class T> void smax(T& a, T b) { if (a < b) a = b; }
template<class T> T gcd(T a, T b) { return b == 0 ? a : gcd(b, a % b); }
template<class T> T sqr(T a) { return a * a; }

template<class T> void outp(const vector<T>& v) {
  REP(i, sz(v)) cout << v[i] << (i + 1 == sz(v) ? '\n' : ' ');
}
template<class T> void outp(T* v, int n) {
  REP(i, n) cout << *v++ << (i + 1 == n ? '\n' : ' ');
}

const int h = 222;
int n;
int k[h], t[h];
int a[h][h];
int s[h];
bool y[1<<20];

int main() {
  freopen("d-small-attempt2.in", "r", stdin);  // -small-attempt0
  freopen("d-small-attempt2.out", "w", stdout);  // -large
  int test, T;
  for (test = 1, scanf("%d", &T); test <= T; ++test) {
    scanf("%d%d", k+0, &n);
    REP(i, k[0]) scanf("%d", a[0]+i);
    FOR(i, 1, n+1) {
      scanf("%d%d", t+i, k+i);
      REP(j, k[i]) scanf("%d", a[i]+j);
    }
    CL(s, 0);
    REP(i, n+1) REP(j, k[i]) ++s[a[i][j]];
    REP(i, n) --s[t[i+1]];
    vi e;
    y[0] = true;
    FOR(u, 1, 1<<n) {
      y[u] = false;
      e.clear();
      REP(i, n) if (u&1<<i) e.pb(i+1);
      REP(i, sz(e)) {
        ++s[t[e[i]]];
        REP(j, k[e[i]]) --s[a[e[i]][j]];
      }
      REP(i, sz(e)) {
        if (s[t[e[i]]] > 0 && y[u^1<<(e[i]-1)]) y[u] = true;
      }
      REP(i, sz(e)) {
        --s[t[e[i]]];
        REP(j, k[e[i]]) ++s[a[e[i]][j]];
      }
    }
    int v = (1 << n) - 1;
    printf("Case #%d:", test);
    if (!y[v]) {
      printf(" IMPOSSIBLE\n");
    } else {
      CL(s, 0);
      REP(j, k[0]) ++s[a[0][j]];
      REP(e, n) {
//        printf("\nv = %d\n", v);
//        FOR(i, 1, 5) printf("%d ", s[i]); printf("\n");
        REP(i, n) if ((v&1<<i) && s[t[i+1]] && y[v^(1<<i)]) {
          --s[t[i+1]];
          REP(j, k[i+1]) ++s[a[i+1][j]];
          v ^= 1<<i;
          printf(" %d", i+1);
          break;
        }
      }
      printf("\n");
    }
  }
  return 0;
}
