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

template<int N>
struct DSU {
  int n;
  int p[N], rank[N];

  int add() { p[n] = n; rank[n] = 0; return n++; }
  void init(int nn) { n = 0; REP(i, nn) add(); }

  int find(int v) {
    return v == p[v] ? v : p[v] = find(p[v]);
  }

  void join(int a, int b) {
    a = find(a);
    b = find(b);
    if (a == b) return;
    if (rank[a] < rank[b]) swap(a, b);
    p[b] = a;
    if (rank[a] == rank[b]) ++rank[a];
  }
};


class TestCase {
 public:
  static const int h = 55;
  int n, m;
  bool r[h][h];
  string z[h];
  DSU<h> d;

  void input() {
    scanf("%d%d", &n, &m);
    char t[11];
    REP(i, n) {
      scanf("%s", t);
      z[i] = string(t);
    }
    CL(r, 0);
    int a, b;
    REP(j, m) {
      scanf("%d%d", &a, &b);
      --a; --b;
      r[a][b] = r[b][a] = true;
    }
  }

  bool operator ()(int i, int j) {
    return z[i] < z[j];
  }

  void solve() {
    vi st;
    vi p;
    REP(i, n) p.pb(i);
    sort(all(p), *this);
    st.pb(p[0]);
    outp("%s", z[p[0]].c_str());
    p[0] = -1;
    REP(step, n-1) {
      bool ist[h];
      CL(ist, false);
      REP(i, sz(st)) ist[st[i]] = true;
      REP(u, n) if (p[u] != -1) {
        bool ok = false;
        d.init(n);
        REP(i, n) if (p[i] != -1) FOR(j, i+1, n) if (p[j] != -1)
          if (r[p[i]][p[j]]) d.join(p[i], p[j]);
        REP(c, sz(st)) {
          int v = st[c];
          REP(i, n) if (r[v][i]) d.join(v, i);
          bool conn = true;
          REP(i, n) if (p[i] != -1 && d.find(p[i]) != d.find(st[0])) {
            conn = false;
            break;
          }
          if (conn && r[v][p[u]]) {
            ok = true;
            break;
          }
        }
        if (ok) {
          while (!r[p[u]][st.back()]) st.pop_back();
          st.pb(p[u]);
          outp("%s", z[p[u]].c_str());
          p[u] = -1;
          break;
        }
      }
    }
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
