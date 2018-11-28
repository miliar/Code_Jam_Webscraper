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
#include <list>
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
#define UNIQUE(a) sort(all(a)), (a).erase(unique(all(a)), (a).end())
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

template<class T> void smin(T& a, const T& b) { if (a > b) a = b; }
template<class T> void smax(T& a, const T& b) { if (a < b) a = b; }
template<class T> T gcd(T a, T b) {
  if (a < 0) a = -a; if (b < 0) b = -b;
  while (a && b) { if (a >= b) a %= b; else b %= a; } return a + b; }
template<class T> T sqr(const T& a) { return a * a; }


class TestCase {
 public:
  // data
  static const int L = 10011;
  int l, n, m;
  ll x;
  char s[L];
  int r[L], p[10];

  static const int g[4][4];
  int gr[4][4];

  int f(int a, int b) {
    int s = 1;
    if (a < 0) a = -a, s = -s;
    if (b < 0) b = -b, s = -s;
    return s * g[a-1][b-1];
  }

  int fr(int a, int b) {
    int s = 1;
    if (a < 0) a = -a, s = -s;
    if (b < 0) b = -b, s = -s;
    return s * gr[a-1][b-1];
  }

  TestCase() {  // input
    scanf("%d%I64d%s", &l, &x, s);
  }

  bool ok() {
    REP(ii, n) REP(ui, l) if (f(p[ii], r[ui]) == 2) {  // i
//      print("i: %d %d\n", ii, ui);
      REP(ik, min(n, m-ii)) REP(uk, l) if (f(fr(r[uk], r[l]), p[ik]) == 4) {
//        print("k: %d %d\n", ik, uk);
        int mm = m - ii - ik;
        if (ui < uk && mm % n == 1) {
          if (fr(r[ui], r[uk]) == 3) return true;
        } else if (mm >= 2) {
          int ij = (mm - 2) % n;
          if (f(fr(r[ui], r[l]), f(p[ij], r[uk])) == 3) return true;
        }
      }
    }
    return false;
  }

  void solve() {
    REP(i, 4) REP(j, 4) {
      int k = g[i][j];
      if (k > 0) gr[i][k-1] = j+1;
      else gr[i][-k-1] = -j-1;
    }

    r[0] = 1;
    REP(i, l) {
      int c = 1;
      switch (s[i]) {
      case 'i': c = 2; break;
      case 'j': c = 3; break;
      case 'k': c = 4; break;
      }
      r[i+1] = f(r[i], c);
    }
//    printi("%d", r, r+l+1);

    p[0] = 1;
    n = 0;
    do {
      p[n+1] = f(p[n], r[l]);
      ++n;
    } while (p[n] != p[0]);
//    print("n = %d\n", n);

    m = x % n;
    REP(i, 3) if (m + n <= x) m += n;
//    print("m = %d\n", m);

    print("%s", ok() ? "YES" : "NO");
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

const int TestCase::g[4][4] = {
  {1,  2,  3,  4},
  {2, -1,  4, -3},
  {3, -4, -1,  2},
  {4,  3, -2, -1}
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
    cerr << "Case " << wtest + 1 << " started\n";
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
  freopen("c-large.in", "r", stdin);  // -small-attempt0
  freopen("c-large.txt", "w", stdout);  // -large
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
    cerr << "Case " << i + 1 << " started\n";
    TestCase* test = new TestCase();
    test->solve();
    output(i, test->out);
    delete test;
  }
#endif
  cerr << endl << endl << "TIME: " << clock() << endl;
  return 0;
}
