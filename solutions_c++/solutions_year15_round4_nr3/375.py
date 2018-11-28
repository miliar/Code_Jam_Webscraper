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
  static const int N = 202;
  int n;
  char t[1111111];
  vi s[N];

  map<string, int> m;
  int ind(const string& s) {
//    print("%s\n", s.c_str());
    if (m.count(s)) return m[s];
    int k = sz(m);
    return m[s] = k;
  }

  void inp(vi& s) {
    s.clear();
    gets(t);
    int i = 0;
    REP(j, strlen(t)) if (t[j] == ' ') {
      t[j] = 0;
      s.pb(ind(string(t + i)));
      i = j + 1;
    }
    s.pb(ind(string(t + i)));
  }

  TestCase() {  // input
    scanf("%d", &n);
    gets(t);
    REP(i, n) inp(s[i]);
  }

  vi unite(const vi& a, const vi& b) {
    vi t(sz(a) + sz(b));
    t.resize(set_union(all(a), all(b), t.begin()) - t.begin());
    return t;
  }

  void solve() {
//    REP(i, n) { print("%d: ", sz(s[i]));
//      REP(j, sz(s[i])) print("%d ", s[i][j]); print("\n"); }
    REP(i, n) sort(all(s[i]));
    int ans = INF;
    REP(u, 1<<(n-2)) {
      vi e, f;
      REP(i, n-2) {
        if (u>>i&1) f = unite(f, s[i+2]);
        else e = unite(e, s[i+2]);
      }
      e = unite(e, s[0]);
      f = unite(f, s[1]);
      vi t(max(sz(e), sz(f)));
      smin(ans, int(set_intersection(all(e), all(f), t.begin()) - t.begin()));
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
  freopen("c-small-attempt0.in", "r", stdin);  // -small-attempt0
  freopen("c-small-attempt0.txt", "w", stdout);  // -large
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
