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
  int n, k;

  void input() {
    scanf("%d%d", &n, &k);
  }

  void generate(bool big, int seed) {
    auto rnd = bind(uniform_int_distribution<int>(0, 9),
                    default_random_engine(seed));
  }

  void solveSlow() {
  }

  void solve() {
    vi d(9);
    REP(i, 9) {
      d[i] = 2;
      while ((i + 3) % d[i] != 0) ++d[i];
    }
    REP(u, k) {
      string s = "1";
      REP(i, n/2-1) {
        char c = (u>>i&1) + '0';
        s += c;
        s += c;
      }
      s += "1";
      print("%s ", s.c_str());
      printi("%d", all(d));
//      REP(i, 9) {
//        int r = 0;
//        REP(j, n) {
//          r *= (i + 2);
//          if (s[j] == '1') ++r;
//          r %= d[i];
//        }
//        if (r != 0) print("error for %d\n", i + 2);
//      }
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
  printf("Case #%d:\n%s", test + 1, answer.c_str());
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
  freopen("c-large.in", "r", stdin);  // -small-attempt0
  freopen("output-large.txt", "w", stdout);  // -large
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
