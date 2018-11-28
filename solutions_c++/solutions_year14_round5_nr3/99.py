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
typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pii;

const int INF = 1000000000;
const ll INF_LL = 1000000000000000000LL;
const double pi = 2 * acos(0.0);

template<class T> void smin(T& a, T b) { if (a > b) a = b; }
template<class T> void smax(T& a, T b) { if (a < b) a = b; }
template<class T> T gcd(T a, T b) { return b == 0 ? a : gcd(b, a % b); }
template<class T> T sqr(T a) { return a * a; }

template<int N, int M>
struct Matching {
  int n, m;
  vi E[N];

  void init(int nn, int mm) {
    REP(i, n) vi().swap(E[i]);
    n = nn; m = mm;
  }

  void add(int a, int b) { E[a].pb(b); }

  int p1[N], p2[M];
  int d[N], q[N];

  bool bfs() {
    int qb = 0;
    REP(i, n) {
      if (p1[i] == -1) d[q[qb++] = i] = 1;
      else d[i] = -1;
    }
    for (int qa = 0; qa < qb; ++qa) {
      int v = q[qa], u;
      REP(i, sz(E[v])) {
        if (p2[u = E[v][i]] == -1) return true;
        if (d[p2[u]] == -1) d[q[qb++] = p2[u]] = d[v] + 1;
      }
    }
    return false;
  }

  bool dfs(int v) {
    for (; q[v] < sz(E[v]); ++q[v]) {
      int u = E[v][q[v]];
      if (p2[u] == -1 || (d[p2[u]] == d[v] + 1 && dfs(p2[u]))) {
        p1[v] = u;
        p2[u] = v;
        return true;
      }
    }
    return false;
  }

  int max_matching(bool zero = true) {
    if (zero) {
      fill_n(p1, n, -1);
      fill_n(p2, m, -1);
    }
    while (bfs()) {
      REP(i, n) q[i] = 0;
      REP(i, n) if (p1[i] == -1) dfs(i);
    }
    return n - count(p1, p1 + n, -1);
  }
};


class TestCase {
 public:
  static const int N = 1011, ID = 2002;
  int n;
  bool e[N];
  int a[N];
  typedef pair<int, bool> pib;
  vector<pib> s[ID];

  Matching<N, N> m;
  //int p1[N], p2[N];

  TestCase() {  // input
    scanf("%d", &n);
    char c;
    REP(i, n) {
      do { scanf("%c", &c); } while (!isalpha(c));
      e[i] = c == 'E';
      scanf("%d", a+i);
    }
  }

  void solve() {
    REP(i, n) if (a[i] != 0) s[a[i]].pb(pib(i, e[i]));
    int k0 = 0, k1 = 0;
    m.init(n, n);
    REP(i, ID) if (!s[i].empty()) {
      REP(j, sz(s[i])-1) if (s[i][j].Y == s[i][j+1].Y) {
        if (s[i][j].Y) ++k0;
        else ++k1;
        FOR(u, s[i][j].X+1, s[i][j+1].X)
          if (a[u] == 0 && e[u] != s[i][j].Y) {
            if (s[i][j].Y) m.add(s[i][j].X, u);
            else m.add(u, s[i][j].X+1);
          }
      }
    }
    if (m.max_matching() != k0 + k1) {
      print("CRIME TIME");
    } else {
      int e0 = 0;
      REP(i, ID) if (!s[i].empty()) {
        int j = sz(s[i]) - 1;
        if (s[i][j].Y) {
          ++e0;
          FOR(t, s[i][j].X+1, n) if (a[t] == 0 && !e[t]) m.add(s[i][j].X, t);
        }
        j = 0;
        if (!s[i][j].Y) {
          REP(t, s[i][j].X) if (a[t] == 0 && e[t]) m.add(t, s[i][j].X);
        }
      }
      REP(i, n) if (a[i] == 0 && e[i]) {
        ++e0;
        FOR(j, i+1, n) if (a[j] == 0 && !e[j]) m.add(i, j);
      }
      //int r0 = m.max_matching(false);
      REP(i, ID) if (!s[i].empty()) {
        REP(j, sz(s[i])-1) if (s[i][j].Y && !s[i][j+1].Y) {
          m.add(s[i][j].X, s[i][j+1].X);
          ++e0;
          FOR(u, s[i][j].X+1, s[i][j+1].X) if (a[u] == 0) {
            if (e[u]) m.add(u, s[i][j+1].X);
            if (!e[u]) m.add(s[i][j].X, u);
          }
        }
      }
      //print("\n%d: %d - %d,%d\n", e0, m.max_matching(false), k0, k1);
      int r = m.max_matching(false);
      //if (r0 != r) { print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"); }
      print("%d", e0 - (r - k0));
    }
  }

  string out;
 private:
  static const int __L = 1024;
  char buf[__L+1];

  void print(const char* fmt, ...) {
    va_list args;
    va_start(args, fmt);
    vsnprintf(buf, __L, fmt, args);
    va_end(args);
    out.append(buf);
  }

  template<typename Iterator>
  void printi(const char* fmt, Iterator begin, Iterator end,
      const char* separator = " ") {
    for (Iterator it = begin; it != end; ++it) {
      if (it != begin) print(separator);
      print(fmt, *it);
    }
    print("\n");
  }
};

mutex input_mutex;
int itest, ntest;
vector<string> answer;

void work() {
  while (true) {
    input_mutex.lock();
    if (itest >= ntest) {
      input_mutex.unlock();
      break;
    }
    int wtest = itest++;
    cerr << "Case " << wtest+1 << " started\n";
    TestCase* test = new TestCase();
    input_mutex.unlock();
    test->solve();
    answer[wtest].swap(test->out);
    delete test;
  }
}

void output(int test, const string& ans) {
  printf("Case #%d: %s\n", test + 1, ans.c_str());
}

int main() {
  freopen("c-small-attempt2.in", "r", stdin);  // -small-attempt0
  freopen("c-small-attempt2.txt", "w", stdout);  // -large
  itest = 0;
  scanf("%d", &ntest);
  answer.resize(ntest);
#ifdef MULTITHREADING
  vector<thread> threads;
  REP(i, thread::hardware_concurrency()) threads.pb(thread(work));
  REP(i, sz(threads)) threads[i].join();
  REP(i, ntest) output(i, answer[i]);
#else
  REP(i, ntest) {
    cerr << "Case " << i+1 << " started\n";
    TestCase* test = new TestCase();
    test->solve();
    output(i, test->out);
    delete test;
  }
#endif
  cerr << endl << endl << "TIME: " << clock() << endl;
  return 0;
}
