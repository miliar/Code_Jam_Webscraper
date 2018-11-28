#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <list>
#include <set>
#include <map>
#include <iostream>

#define pb push_back
#define mp make_pair
//#define TASKNAME ""

#ifdef DEBUG
#define eprintf(...) fprintf(stderr,__VA_ARGS__)
#else
#define eprintf(...)
#endif

#define TIMESTAMP(x) eprintf("[" #x "] Time = %.3lfs\n",clock()*1.0/CLOCKS_PER_SEC)

#ifdef _WIN32
#define LLD "%I64d"
#else
#define LLD "%lld"
#endif

#define sz(x) ((int)(x).size())
#define forn(i, n) for (int i = 0; i < (n); i++)

using namespace std;

typedef long double ld;
typedef long long ll;
typedef vector<ll> vll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef pair<int, int> pii;
typedef pair <ll, ll> pll;
typedef vector<pii> vpii;

const int inf = 1e9;
const double eps = 1e-7;
const int INF = inf;
const double EPS = eps;

#ifdef DEBUG
struct __timestamper {
	~__timestamper(){
		TIMESTAMP(end);
	}
} __Timestamper;
#else
struct __timestamper {};
#endif

/*Template end*/

struct Source {
  ld maxw;
  ld c;
  bool operator<(const Source &s2) const {
    return c > s2.c;
  }
};

ld calc(const vector<ld> &rs, const vector<ld> &cs, ld maxt) {
  const int n = sz(rs);

  vector<Source> ss1, ss2;
  ld ans = 0;
  forn (i, n) {
    ld cur = rs[i] * maxt;
    ans += cur;
    if (fabs(cs[i]) <= eps) {
    } else if (cs[i] > eps) {
      ss1.pb({ cs[i] * cur, cs[i] });
    } else if (cs[i] < -eps) {
      ss2.pb({ -cs[i] * cur, -cs[i] });
    } else {
      assert(false);
    }
  }

  sort(ss1.begin(), ss1.end());
  sort(ss2.begin(), ss2.end());

  ld s1 = 0, s2 = 0;
  for (auto x : ss1) s1 += x.maxw;
  for (auto x : ss2) s2 += x.maxw;
  if (s1 < s2) {
    swap(s1, s2);
    ss1.swap(ss2);
  }
  for (Source s : ss1) {
    ld need = min(s1 - s2, s.maxw);
    ans -= need / s.c;
  }
  return ans;
}

ld read() {
  double x;
  scanf("%lf", &x);
  return x;
}

void solve() {
  int n;
  scanf("%d", &n);
  ld v0 = read();
  ld t0 = read();

  vector<ld> rs(n), cs(n);
  int have = 0;
  forn (i, n) {
    rs[i] = read();
    cs[i] = read();
    cs[i] -= t0;
    if (cs[i] >= -eps) have |= 1;
    if (cs[i] <= eps) have |= 2;
  }
  if (have != 3) {
    printf("IMPOSSIBLE\n");
    return;
  }
  ld L = 0, R = int(1e9);
  forn (step, 100) {
    ld M = (L + R) / 2;
    if (calc(rs, cs, M) >= v0) {
      R = M;
    } else {
      L = M;
    }
  }
  assert(fabs(R - L) < 1e-12);
  printf("%.18e\n", (double)((L + R) / 2));
}

bool endsWith(string a, string b) {
  return a.length() >= b.length() && string(a, a.length() - b.length()) == b;
}

int main(int argc, char *argv[]) {
  {
    string fn = "";
    if (argc >= 2) fn = argv[1];
    if (endsWith(fn, ".in")) fn = string(fn, 0, fn.length() - 3);
    freopen((fn + ".in").c_str(), "r", stdin);
    freopen((fn + ".out").c_str(), "w", stdout);
  }

  int TC;
  assert(scanf("%d", &TC) >= 1);
  for (int TN = 1; TN <= TC; TN++) {
    eprintf("Case #%d:\n", TN);
    printf("Case #%d: ", TN);
    try {
      solve();
    } catch (...) {
      eprintf("Caught exception at test case #%d\n", TN);
      return 1;
    }
  }
  return 0;
}
