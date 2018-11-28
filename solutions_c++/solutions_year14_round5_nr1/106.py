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

class TestCase {
 public:
  static const int h = 1000011;
  int n, p, q, r, s;
  int a[h];
  ll sum[h];

  TestCase() {  // input
    scanf("%d%d%d%d%d", &n, &p, &q, &r, &s);
  }

  void solve() {
    REP(i, n) a[i] = (ll(i) * p + q) % r + s;
    //printi("%d", a, a+n);
    sum[0] = 0;
    REP(i, n) sum[i+1] = sum[i] + a[i];
    ll ans = INF_LL;
    int r = 0;
//    while (sum[r] * 2 < sum[n]) ++r;
    REP(l, n) {
      while (r <= l) ++r;
      smin(ans, max(max(sum[l], sum[r] - sum[l]), sum[n] - sum[r]));
      while (r < n && (sum[r] - sum[l]) < sum[n] - sum[r]) {
        ++r;
//        if (n < 100) print("%d %d: %I64d %I64d %I64d\n",
//            l, r, sum[l], sum[r] - sum[l], sum[n] - sum[r]);
        smin(ans, max(max(sum[l], sum[r] - sum[l]), sum[n] - sum[r]));
      }
      --r;
    }
    ll d = sum[n];
//    print("%I64d %I64d\n", ans, d);
    ans = d - ans;
    print("%I64d.", ans / d);
    REP(i, 15) {
      ans %= d;
      ans *= 10;
      print("%I64d", ans / d);
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
  freopen("a-large.in", "r", stdin);  // -small-attempt0
  freopen("a-large.txt", "w", stdout);  // -large
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
