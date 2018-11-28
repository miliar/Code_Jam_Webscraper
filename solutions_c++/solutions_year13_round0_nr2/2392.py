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

const int h = 111;
int n, m;
int a[h][h];
int mr[h], mc[h];

int main() {
  freopen("b-large.in", "r", stdin);  // -small-attempt0
  freopen("b-large.out", "w", stdout);  // -large
  int test, T;
  for (test = 1, scanf("%d", &T); test <= T; ++test) {
    scanf("%d%d", &n, &m);
    REP(i, n) REP(j, m) scanf("%d", &a[i][j]);
    REP(i, n) {
      mr[i] = 0;
      REP(j, m) smax(mr[i], a[i][j]);
    }
    REP(j, m) {
      mc[j] = 0;
      REP(i, n) smax(mc[j], a[i][j]);
    }
    bool ok = true;
    REP(i, n) REP(j, m) if (a[i][j] != mr[i] && a[i][j] != mc[j]) {
      ok = false;
    }
    printf("Case #%d: %s\n", test, ok ? "YES" : "NO");
  }
  return 0;
}
