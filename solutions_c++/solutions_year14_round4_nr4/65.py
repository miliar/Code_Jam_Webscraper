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

const int mod = 1000000007;
void inc(int &x, int y) { x += y; if (x >= mod) x -= mod; }
int add(int x, int y) { inc(x, y); return x; }
int mul(int x, int y) { return (ll(x) * y) % mod; }

void dec(int &x, int y) { x -= y; if (x < 0) x += mod; }
int sub(int x, int y) { dec(x, y); return x; }

class TestCase {
 public:
  static const int M = 8, L = 11;
  int n, m;
  char s[M][L];
  int l[M], p[M][M];

  void input() {
    scanf("%d%d", &m, &n);
    REP(i, m) scanf("%s", s+i);
  }

  int t[M];
  int ans, w;

  void go(int i, int sum) {
    if (i == m) {
      if (ans < sum) ans = sum, w = 1;
      else if (ans == sum) ++w;
      return;
    }
    REP(u, n) {
      t[i] = u;
      int c = -1;
      REP(j, i) if (t[j] == u) smax(c, p[i][j]);
      go(i+1, sum + l[i] - c);
    }
  }

  void solve() {
    REP(i, m) l[i] = strlen(s[i]);
    REP(i, m) FOR(j, i+1, m) {
      int u = 0;
      while (u < min(l[i], l[j]) && s[i][u] == s[j][u]) ++u;
      p[i][j] = p[j][i] = u;
    }
    ans = 0;
    go(0, 0);
    outp("%d %d", ans, w);
  }

  string out;
 private:
  static const int _L = 1024;
  char buf[_L+1];

  void outp(const char* fmt, ...) {
    va_list args;
    va_start(args, fmt);
    vsnprintf(buf, _L, fmt, args);
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
  freopen("d-small-attempt0.in", "r", stdin);  // -small-attempt0
  freopen("d-small-attempt0.out", "w", stdout);  // -large
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
