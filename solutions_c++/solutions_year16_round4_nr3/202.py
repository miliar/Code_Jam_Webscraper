#include <stdexcept>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <cassert>
#include <cstring>
#include <cstdarg>
#include <cstdio>
#include <memory>
#include <random>
#include <cmath>
#include <ctime>
#include <functional>
#include <algorithm>
#include <complex>
#include <numeric>
#include <limits>
#include <bitset>
#include <vector>
#include <string>
#include <queue>
#include <deque>
#include <array>
#include <list>
#include <map>
#include <set>
#include <thread>
#include <mutex>

using namespace std;

#define all(a) (a).begin(), (a).end()
#define sz(a) static_cast<int>((a).size())
#define FOR(i, a, b) for (int i(a), b_(b); i < b_; ++i)
#define REP(i, n) FOR (i, 0, n)
#define FORD(i, a, b) for (int i(a), b_(b); i >= b_; --i)
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
template <class T> using min_queue = priority_queue<T, vector<T>, greater<T>>;

const int INF = static_cast<int>(1e9);
const long long INF_LL = static_cast<long long>(4e18);
const double pi = acos(-1.0);

template <class T> T& smin(T& x, const T& y) { if (x > y) x = y; return x; }
template <class T> T& smax(T& x, const T& y) { if (x < y) x = y; return x; }
template <class T> T sqr(const T& x) { return x * x; }

template <class T> T gcd(T a, T b) {
  for (a = abs(a), b = abs(b); a && b; a >= b ? a %= b : b %= a);
  return a + b;
}

class TestCase {
public:
  // data
  static const int N = 111;
  int r, c, n;
  int p[N];

  void input() {
    scanf("%d%d", &r, &c);
    n = 2 * (r + c);
    REP(i, r + c) {
      int a, b;
      scanf("%d%d", &a, &b);
      --a;
      --b;
      p[a] = b;
      p[b] = a;
    }
  }

  void generate(bool big, int seed) {
    auto rnd = bind(uniform_int_distribution<int>(0, 9),
                    default_random_engine(seed));
  }

  void solveSlow() {
  }

  char f[N][N];
  struct P {
    int x, y, dir;
    P(int x = 0, int y = 0, int dir = 0) : x(x), y(y), dir(dir) {}
  };

  P calc(int i) {
    if (i < c) return P(0, i, 0);
    i -= c;
    if (i < r) return P(i, c-1, 3);
    i -= r;
    if (i < c) return P(r-1, c-i-1, 1);
    i -= c;
    return P(r-i-1, 0, 2);
  }

  bool findPath(P a, P b) {
    switch (b.dir) {
      case 0: --b.x; break;
      case 1: ++b.x; break;
      case 2: --b.y; break;
      case 3: ++b.y; break;
    }
    while (true) {
      int i = a.x, j = a.y;
      switch (a.dir) {
        case 0:
          if (f[i][j] == '/') a.dir = 3, --a.y;
          else f[i][j] = '\\', a.dir = 2, ++a.y;
          break;
        case 1:
          if (f[i][j] == '/') a.dir = 2, ++a.y;
          else f[i][j] = '\\', a.dir = 3, --a.y;
          break;
        case 2:
          if (f[i][j] == '\\') a.dir = 0, ++a.x;
          else f[i][j] = '/', a.dir = 1, --a.x;
          break;
        case 3:
          if (f[i][j] == '\\') a.dir = 1, --a.x;
          else f[i][j] = '/', a.dir = 0, ++a.x;
          break;
      }
      if (a.x == b.x && a.y == b.y) return true;
      if (a.x < 0 || a.x >= r) return false;
      if (a.y < 0 || a.y >= c) return false;
//      if (d == 0 && a.x == r) return false;
//      if (d == 1 && a.x == -1) return false;
//      if (d == 2 && a.y == c) return false;
//      if (d == 3 && a.y == -1) return false;
    }
  }

  void solve() {
    vi l;
    REP(i, n) l.pb(i);
    REP(i, r) REP(j, c) f[i][j] = '.';
    while (true) {
      l.pb(l[0]);
      bool ok = false;
      REP(i, sz(l)-1) if (l[i+1] == p[l[i]]) {
        if (findPath(calc(l[i]), calc(l[i+1]))) {
//          REP(ii, r) printf("%s\n", f[ii]); printf("\n");
          l.erase(l.begin() + i);
          if (i+1 == sz(l)) l.erase(l.begin());
          else l.erase(l.begin() + i);
          ok = true;
        }
        break;
      }
      l.pop_back();
      if (!ok) break;
    }
    if (l.empty()) {
      REP(i, r) {
        REP(j, c) if (f[i][j] == '.') f[i][j] = '/';
        print("\n%s", f[i]);
      }
    } else {
      print("\nIMPOSSIBLE");
    }
  }

  string output;
private:
  static const int __L = 1 << 9;
  char buffer[__L+1];

  void print(const char* format, ...) {
    va_list args;
    va_start(args, format);
    vsnprintf(buffer, __L, format, args);
    va_end(args);
    output.append(buffer);
  }

  template <typename Iterator>
  void printi(const char* format, Iterator first, Iterator last,
              const char* delimiter = " ", const char* closing = "\n") {
    for (; first != last; ++first != last ? print("%s", delimiter) : void())
      print(format, *first);
    print("%s", closing);
  }
};

mutex inputMutex;
int testIndex, testCount;
vector<string> answer;

void work() {
  while (true) {
    inputMutex.lock();
    if (testIndex >= testCount) {
      inputMutex.unlock();
      break;
    }
    int current = testIndex++;
    cerr << "Case " << current + 1 << " started\n";
    unique_ptr<TestCase> test(new TestCase());
    test->input();
    inputMutex.unlock();
    test->solve();
    answer[current].swap(test->output);
  }
}

void output(int test, const string& answer) {
  printf("Case #%d: %s\n", test + 1, answer.c_str());
}

void randomTest() {
  for (int i = 0; i < 100; ++i) {
    unique_ptr<TestCase> test(new TestCase());
    test->generate(false, i);
    test->solve();
    string output;
    output.swap(test->output);
    test->solveSlow();
    if (test->output != output) {
      cerr << "Error on test #" << i + 1 << endl;
      cerr << "Expected:\n" << test->output << endl;
      cerr << "Received:\n" << output << endl;
    }
    //cerr << output << endl;
  }
  cerr << endl << endl << "Test time: ";
  cerr << static_cast<double>(clock()) / CLOCKS_PER_SEC << endl;
  exit(0);
}

void maxTest() {
  for (int i = 0; i < 100; ++i) {
    unique_ptr<TestCase> test(new TestCase());
    test->generate(true, i);
    test->solve();
    output(i, test->output);
  }
  cerr << endl << endl << "Max test time: ";
  cerr << static_cast<double>(clock()) / CLOCKS_PER_SEC << endl;
  exit(0);
}

int main() {
  //randomTest();
  //maxTest();
  freopen("c-small-attempt0.in", "r", stdin);  // -small-attempt0.in
  freopen("c-small-attempt0.txt", "w", stdout);  // -large
  testIndex = 0;
  scanf("%d", &testCount);
  answer.resize(testCount);
#ifndef SINGLE_THREAD
  vector<thread> threads;
  for (int i = 0; i < thread::hardware_concurrency(); ++i)
    threads.emplace_back(work);
  for (auto& thread : threads) thread.join();
  for (int i = 0; i < testCount; ++i) output(i, answer[i]);
#else
  for (int i = 0; i < testCount; ++i) {
    cerr << "Case " << i + 1 << " started\n";
    unique_ptr<TestCase> test(new TestCase());
    test->input();
    test->solve();
    output(i, test->output);
  }
#endif
  cerr << endl << endl << "Total time: ";
  cerr << static_cast<double>(clock()) / CLOCKS_PER_SEC << endl;
  return 0;
}
