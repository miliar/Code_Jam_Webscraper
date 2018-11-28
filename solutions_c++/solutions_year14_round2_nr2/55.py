#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdarg>
#include <cstdio>
#include <ctime>
#include <cmath>
#include <complex>
#include <numeric>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <thread>
#include <mutex>

using namespace std;

#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define FOR(i, a, b) for (int i(a), _b(b); i < _b; ++i)
#define REP(i, n) FOR(i, 0, n)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
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

class TestCase {
 public:
  static const int h = 31;
  int a, b, k;
  vi da, db, dk;
  vi va, vb;

  void input() {
    scanf("%d%d%d", &a, &b, &k);
  }

  vi d(int n) {
    vi res;
    while (n) {
      res.pb(n&1);
      n >>= 1;
    }
    while (sz(res) < h) res.pb(0);
    return res;
  }

  ll r[h][2][2];

  ll f(int u, bool ya, bool yb, bool yk) {
    if (u < 0) return !ya && !yb && !yk;
    if (!yk) {
      int ma = ya ? va[u] : (1<<(u+1));
      int mb = yb ? vb[u] : (1<<(u+1));
      return ll(ma) * mb;
    }
    ll& res = r[u][ya][yb];
    if (res != -1) return res;
    res = 0;
    REP(ca, 2) if (!ya || ca <= da[u])
      REP(cb, 2) if (!yb || cb <= db[u]) {
        int ck = ca & cb;
        if (!yk || ck <= dk[u]) res += f(u-1,
            ya && (ca == da[u]), yb && (cb == db[u]), yk && (ck == dk[u]));
      }
    return res;
  }

  void solve() {
    da = d(a);
    db = d(b);
    dk = d(k);
    int ca = 0, cb = 0;
    REP(u, h) {
      ca += da[u]<<u;
      va.pb(ca);
      cb += db[u]<<u;
      vb.pb(cb);
    }
    CL(r, -1);
    outp("%I64d", f(h-1, true, true, true));
  }

  string out;
 private:
  static const int L = 1024;
  char buf[L+1];

  void outp(const char* fmt, ...) {
    va_list args;
    va_start(args, fmt);
    vsnprintf(buf, L, fmt, args);
    va_end(args);
    out.append(buf);
  }
};

mutex io_mutex;
int itest, ntest;
vector<string> answer;

void work() {
  while (true) {
    io_mutex.lock();
    if (itest >= ntest) {
      io_mutex.unlock();
      break;
    }
    int wtest = itest;
    ++itest;
    cerr << "Case " << wtest+1 << " started\n";
    TestCase test;
    test.input();
    io_mutex.unlock();
    test.solve();
    answer[wtest].swap(test.out);
  }
}

void output(int test, const string& ans) {
  printf("Case #%d: %s\n", test + 1, ans.c_str());
}

int main() {
  freopen("b-large.in", "r", stdin);  // -small-attempt0
  freopen("b-large.out", "w", stdout);  // -large
  itest = 0;
  scanf("%d", &ntest);
  answer.resize(ntest);
#ifdef MULTITHREADING
  vector<thread> threads;
  REP (i, thread::hardware_concurrency()) threads.pb(thread(work));
  REP (i, sz(threads)) threads[i].join();
  REP (i, ntest) output(i, answer[i]);
#else
  REP (i, ntest) {
    cerr << "Case " << i+1 << " started\n";
    TestCase test;
    test.input();
    test.solve();
    output(i, test.out);
  }
#endif
  cerr << endl << endl << "TIME: " << clock() << endl;
  return 0;
}
