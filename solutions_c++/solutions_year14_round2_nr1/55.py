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
  char t[111];
  int n;
  vector<string> s;
  typedef pair<char, int> pci;
  vector<vector<pci>> g;

  void input() {
    scanf("%d", &n);
    s.clear();
    REP(i, n) {
      scanf("%s", t);
      s.pb(t);
    }
  }

  void solve() {
    g.resize(n);
    REP(i, n) {
      g[i].clear();
      REP(j, sz(s[i])) {
        int k = 1;
        while (j+1 < sz(s[i]) && s[i][j] == s[i][j+1]) ++j, ++k;
        g[i].pb(pci(s[i][j], k));
      }
    }
    bool ok = true;
    int ans = 0;
    REP(i, n) if(sz(g[i]) != sz(g[0])) ok = false;
    if (ok) {
      REP(j, sz(g[0])) {
        REP(i, n) if(g[0][j].X != g[i][j].X) ok = false;
        int cur = INF;
        FOR(l, 1, 101) {
          int sum = 0;
          REP(i, n) sum += abs(l - g[i][j].Y);
          smin(cur, sum);
        }
        ans += cur;
      }
    }
    if (ok) outp("%d", ans);
    else outp("Fegla Won");
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
  freopen("a-large.in", "r", stdin);  // -small-attempt0
  freopen("a-large.out", "w", stdout);  // -large
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
