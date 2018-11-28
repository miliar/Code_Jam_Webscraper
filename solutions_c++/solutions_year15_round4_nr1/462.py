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

template<class T> T& smin(T& a, const T& b) { if (a > b) a = b; return a; }
template<class T> T& smax(T& a, const T& b) { if (a < b) a = b; return a; }
template<class T> T sqr(const T& a) { return a * a; }

class TestCase {
 public:
  // data
  static const int N = 111;
  int r, c;
  char g[N][N];

  TestCase() {  // input
    scanf("%d%d", &r, &c);
    REP(i, r) scanf("%s", g[i]);
  }

  void solve() {
    int ans = 0;
    REP(i, r) REP(j, c) if (g[i][j] != '.') {
      bool a[4];
      REP(u, 4) a[u] = false;
      REP(x, i) if (g[x][j] != '.') { a[0] = true; break; }
      FOR(x, i+1, r) if (g[x][j] != '.') { a[1] = true; break; }
      REP(y, j) if (g[i][y] != '.') { a[2] = true; break; }
      FOR(y, j+1, c) if (g[i][y] != '.') { a[3] = true; break; }
      bool one = false;
      REP(u, 4) if (a[u]) one = true;
      if (!one) {
        print("IMPOSSIBLE");
        return;
      }
      if (g[i][j] == '^' && !a[0]) ++ans;
      if (g[i][j] == 'v' && !a[1]) ++ans;
      if (g[i][j] == '<' && !a[2]) ++ans;
      if (g[i][j] == '>' && !a[3]) ++ans;
    }
    print("%d", ans);
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
