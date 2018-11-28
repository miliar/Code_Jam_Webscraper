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

struct build {
  int x0, y0, x1, y1;

  void inp() { scanf("%d%d%d%d", &x0, &y0, &x1, &y1); }

  int dist(const build& a) {
    int dx = 0;
    if (x0 > a.x1) dx = x0 - a.x1 - 1;
    if (a.x0 > x1) dx = a.x0 - x1 - 1;
    int dy = 0;
    if (y0 > a.y1) dy = y0 - a.y1 - 1;
    if (a.y0 > y1) dy = a.y0 - y1 - 1;
    return max(dx, dy);
  }
};

const int B = 1011;
int w, h, n;
build b[B];
int e[B][B];

class TestCase {
 public:
  void input() {
    scanf("%d%d%d", &w, &h, &n);
    REP(i, n) b[i].inp();
  }

  int d[B];
  bool us[B];

  void add(int a, int b, int w) {
    e[a][b] = e[b][a] = w;
  }

  int dist(int s, int t) {
    fill_n(d, n, INF);
    CL(us, 0);
    d[s] = 0;
    REP(i, n) {
      int u = -1;
      REP(j, n) if (!us[j] && (u == -1 || d[j] < d[u])) u = j;
      if (u == t) return d[u];
      us[u] = true;
      REP(v, n) if (!us[v] && e[u][v] != -1)
        smin(d[v], d[u] + e[u][v]);
    }
    return -1;
  }

  void solve() {
    if (n == 0) {
      outp("%d", w);
      return;
    }
    CL(e, -1);
    REP(i, n) {
      add(i, n, b[i].x0);
      add(i, n+1, w-1 - b[i].x1);
      FOR(j, i+1, n) add(i, j, b[i].dist(b[j]));
    }
    n += 2;
    outp("%d", dist(n-2, n-1));
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
  freopen("c-large.in", "r", stdin);  // -small-attempt0
  freopen("c-large.out", "w", stdout);  // -large
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
