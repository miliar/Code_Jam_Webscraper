#include <bits/stdc++.h>

using namespace std;

#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define FOR(i, a, b) for (int i(a), _b(b); i < _b; ++i)
#define REP(i, n) FOR (i, 0, n)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define UNIQUE(a) sort(all(a)), (a).erase(unique(all(a)), (a).end())
#define CL(a, v) memset(a, v, sizeof a)
#define eb emplace_back
#define pb push_back
#define X first
#define Y second

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pii;

const int INF = 1e9;
const ll INF_LL = 4e18;
const double pi = acos(-1.0);
const double eps = 1e-9;

template<class T> T& smin(T& a, const T& b) { if (a > b) a = b; return a; }
template<class T> T& smax(T& a, const T& b) { if (a < b) a = b; return a; }
template<class T> T sqr(const T& a) { return a * a; }


class TestCase {
 public:
  // data
  static const int N = 111;
  int n;
  double v, x;
  double r[N], c[N];


  TestCase() {  // input
    scanf("%d%lf%lf", &n, &v, &x);
    REP(i, n) scanf("%lf%lf", r+i, c+i);
  }

  void solve() {
    if (n > 2) {
      print("N TOO BIG");
      return;
    }
    if (n == 2 && fabs(c[0] - c[1]) < eps) {
      r[0] += r[1];
      n = 1;
    }
    if (n == 1) {
      if (fabs(c[0] - x) > eps) print("IMPOSSIBLE");
      else print("%.9lf", v / r[0]);
      return;
    }
    REP(i, 2) if (fabs(c[i] - x) < eps) {
      print("%.9lf", v / r[i]);
      return;
    }
    if (c[0] > c[1]) {
      swap(c[0], c[1]);
      swap(r[0], r[1]);
    }
    double v0 = v * (c[1] - x) / (c[1] - c[0]);
    double v1 = v * (x - c[0]) / (c[1] - c[0]);
    if (v0 < 0 || v1 < 0) print("IMPOSSIBLE");
    else print("%.9lf", max(v0 / r[0], v1 / r[1]));
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
      const char* separator = " ", const char* closing = "\n") {
    for (Iterator it = begin; it != end; printf(fmt, *it),
	  printf("%s", ++it == end ? closing : separator));
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
  freopen("b-small-attempt2.in", "r", stdin);  // -small-attempt0
  freopen("b-small-attempt2.txt", "w", stdout);  // -large
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
