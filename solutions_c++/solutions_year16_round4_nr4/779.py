// {{{ Includes

#pragma clang diagnostic ignored "-Wc++98-compat-pedantic"
#pragma clang diagnostic ignored "-Wunused-macros"
#pragma clang diagnostic ignored "-Wmissing-prototypes"
#pragma clang diagnostic ignored "-Wsign-conversion"
#pragma clang diagnostic ignored "-Wsign-compare"

#include <random>
#include <climits>
#include <array>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <queue>
#include <cstring>
#include <limits>
#include <chrono>

#include <unistd.h>
using namespace std;

#ifdef ONLINE_JUDGE // UVa defines this flag
static bool debug = false;
#else
static bool debug = true;
#endif

// }}}
// {{{ Utilities

#define Loop(i, n) for (int i = 0; i < int(n); ++i)
#define Loopa(i, a, b) for (int i = (a); i <= (b); ++i)
#define Loopd(i, a, b) for (int i = (a); i >= (b); --i)

template <typename T, typename Q, typename S>
bool Bounded(const T &x, const Q &a, const S &b) {
  return a <= x && x <= b;
}

#define db(x) #x << "=" << x << " "
#define pdb(x) printf("#x = %d\n", x);
#define All(x) x.begin(), x.end()
template <typename T> int sz(const T &x) { return x.size(); }
template <typename T, typename Q> bool mem(const T &s, const Q &x) {
  return s.find(x) != s.end();
}
typedef long double ld;
typedef long long int ll;
typedef vector<int> Vi;
typedef vector<ll> Vll;
typedef pair<int, int> Pii;
typedef pair<ll, ll> Pll;
typedef vector<Vi> Adj;
typedef vector<bool> Vb;
#define CI(x) x::const_iterator
#define II(x) x::iterator

template <typename T> int sign(const T &x) {
  return x == 0 ? 0 : x > 0 ? 1 : -1;
}
template <typename T> T square(const T &x) { return x * x; }

template <typename T> struct leq_by {
  const vector<T> *v;
  leq_by(const vector<T> &v_) : v(&v_) {}
  bool operator()(int i, int j) { return v->at(i) < v->at(j); }
};

template <typename S, typename T>
istream& operator>>(istream& in, pair<S, T>& p) {
  return in >> p.first >> p.second;
}
template <typename S, typename T>
ostream& operator<<(ostream& out, const pair<S, T>& p) {
  return out << "{" << p.first << ", " << p.second << "}";
}

template <typename ...Args, typename T, typename S>
S& read(Args... args, T& x, S& y) { read(&args..., x); cin >> y; return y; }
template <typename T, typename I = typename T::iterator>
void read(T &cnt) { for (auto& x : cnt) cin >> x; }
template <typename S, typename T> T& read(S& y, T& x) { cin >> y >> x; return x; }

template <typename T> void umin(T &x, const T &y) { x = min(x, y); }
template <typename T> void umax(T &x, const T &y) { x = max(x, y); }
template <typename T, typename F, typename... Types>
T &Update(T &x, F fun, Types... args) {
  return x = fun(x, args...);
}

// }}}
// {{{ Output

template <typename T> struct show_container {
  const T &container;
  show_container(const T &container_) : container(container_) {}
};
template <typename T>
ostream &operator<<(ostream &o, const show_container<T> &thing) {
  bool first = true;
  o << "{";
  for (const auto &x : thing.container) {
    if (!first)
      o << ", ";
    first = false;
    o << x;
  }
  o << "}";
  return o;
}

template <typename T> show_container<T> show(const T &container) {
  return show_container<T>(container);
}

#define dprintf debug && printf
struct dout_ { } dout;
template <typename T> dout_ &operator<<(dout_ &out, const T &thing) { if (debug) cout << thing; return out; }
dout_ &operator<<(dout_ &out, ostream &(*thing)(ostream &)) { if (debug) cout << thing; return out; }

struct outboth {
  ostream &a;
  ostream &b;
  outboth(ostream &a_, ostream &b_) : a(a_), b(b_) {}
};
template <typename T> outboth &operator<<(outboth &both, const T &thing) {
  both.a << thing;
  both.b << thing;
  return both;
}
outboth &operator<<(outboth &both, ostream &(*thing)(ostream &)) {
  both.a << thing;
  both.b << thing;
  return both;
}

// }}}
// {{{ Timing

struct ScopeTiming_impl {
  string filename, function;
  int lineno;
  string label;
  int *counter;
  chrono::time_point<std::chrono::high_resolution_clock> startTime, endTime;
  ScopeTiming_impl(string filename_ = "<no file>",
    string function_ = "<>",
    int lineno_ = -1, string label = "", int* counter_ = nullptr)
    : filename(filename_), function(function_),
      lineno(lineno_), label(label), counter(counter_)
  {
    startTime = std::chrono::high_resolution_clock::now();
  }
  ~ScopeTiming_impl() {
    if (!debug) return;
    endTime = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = endTime - startTime;
    cout << filename << ":" << lineno << ":" << function;
    if (!label.empty()) cout << ":" << label;
    if (counter) cout << "[" << ++*counter << "]";
    cout << ": Time taken: ";
    int oldprec = cout.precision(3);
    auto oldflags = cout.setf(std::ios::fixed);
    cout << (1e3 * elapsed.count()) << "ms." << endl;
    cout.flags(oldflags);
    cout.precision(oldprec);
  }
};
#ifndef ONLINE_JUDGE
#define TIMING__(label, c1, c2) static int counter##c1 = 0; ScopeTiming_impl timing##c2(__FILE__, __FUNCTION__, __LINE__, label, &counter##c1)
#define TIMING_(label, c1, c2) TIMING__(label, c1, c2)
#define TIMING(label) TIMING_(label, __COUNTER__, __COUNTER__)
#define TIMING0() TIMING("")
#else
#define TIMING(label)
#define TIMING0()
#endif

// }}}
// {{{ Common algorithms

template <typename T, typename F>
T isearch(T low, T high, F pred) {
  assert(low < high);
  assert(!pred(low));
  assert(pred(high));
  while (high >= low + 2) {
    T m = sign(low) == sign(high)
      ? low + (high - low) / 2
      : (high + low) / 2;
    if (pred(m)) high = m;
    else low = m;
  }
  return low;
}

// }}}
// {{{ Solver known to be correct

void solve_correct(int casenum, outboth rout) {
  printf("==================================================% 3d\n", casenum);

  rout << "Case #" << casenum << ": "
       << "not implemented." << endl;
}

// }}}
// {{{ Solver

int N;

uint32_t nextBitPermutation(uint32_t v) {
  uint32_t t = v | (v - 1);
  return (t + 1) | (((~t & -~t) - 1) >> (__builtin_ctz(v) + 1));
}

uint32_t nextSubset(uint32_t universe, uint32_t subset) {
  assert((subset & ~universe) == 0 && subset != universe);
  // Returns the lexicographically next subset after `subset' of the
  // set universe. Returns zero when subset == universe.
  return (subset - universe) & universe;
}

bool check(const vector<Vi>& A) {
  Vi workerOrder(N); iota(All(workerOrder), 0);

  do {

    Vb taken(N);
    // dout << "check: " << show(workerOrder) << endl;;
    // Loop(i,N) dout << "    " << show(A[i]) << endl;
    function<bool(int)> search = [&](int i) -> bool {
      // dout << "search(" << i << "): " << show(taken) << endl;
      if (i == N) return true;
      bool allTrue = true, hasJob = false;
      for (int j = 0; j < N && allTrue; ++j) {
        if (A[workerOrder[i]][j] && !taken[j]) {
          hasJob = true;
          taken[j] = true;
          allTrue = allTrue && search(i+1);
          taken[j] = false;
        }
      }
      // dout << "search(" << i << ") => " << allTrue << " " << hasJob << endl;
      return allTrue && hasJob;
    };
    if (!search(0)) return false;

  } while (next_permutation(All(workerOrder)));

  return true;
}

void solve(int casenum, outboth rout) {
  printf("==================================================% 3d\n", casenum);
  TIMING0();

  cin >> N;
  vector<string> As(N); read(As);
  vector<Vi> A(N, Vi(N));
  Loop(i, N) Loop(j, N) A[i][j] = (As[i][j] == '1');

  dout << db(N) << endl;
  Loop(i,N) dout << show(A[i]) << endl;

  bool done = false;
  int ans = -1;
  for (int weight = 0; weight <= N*N && !done; ++weight) {
    for (int subset = (1<<weight)-1; subset < (1<<(N*N)); subset = nextBitPermutation(subset)) {
      assert(__builtin_popcount(subset) == weight);
      vector<Vi> A2 = A;
      bool valid = true;
      for (int i = 0; i < N*N && valid; ++i)
        if (subset&(1<<i)) {
          int k = i/N, j = i%N;
          if (A2[k][j]) valid = false;
          else A2[k][j] = 1;
        }
      // dout << db(subset) << endl;
      if (!valid) continue;
      if (check(A2)) {
        done = true;
        ans = weight;
        break;
      }
    }
  }

  rout << "Case #" << casenum << ": " << ans << endl;
}

// }}}
// {{{ Main

int main(int argc, char **argv) {
  debug = getenv("NODEBUG") == NULL;

  string fnIn, fnOut, fnTest;
  if (argc > 1) {
    fnIn = string(argv[1]);
    if (fnIn.substr(fnIn.size() - 3) == ".in") {
      fnOut = fnIn.substr(0, fnIn.size() - 3) + ".last";
      fnTest = fnIn.substr(0, fnIn.size() - 3) + ".out";
    } else {
      fnOut = fnIn + ".last";
      fnTest = fnIn + ".out";
    }
  } else {
    fnIn = "D.test.in";
    fnOut = "D.test.last";
    fnTest = "D.test.out";
  }
  cout << "Input file: " << fnIn << endl
       << "Output file: " << fnOut << endl
       << "Testing file: " << fnTest << endl;
  freopen(fnIn.c_str(), "r", stdin);
  ofstream outfile(fnOut);

  auto startTime = std::chrono::steady_clock::now();

  int T = 0;
  cin >> T;
  assert(!!cin);
  if (getenv("CORRECT") != NULL) {
    Loop(i, T) solve_correct(i + 1, outboth(cout, outfile));
  } else {
    Loop(i, T) solve(i + 1, outboth(cout, outfile));
  }

  std::chrono::duration<double> elapsed = std::chrono::steady_clock::now() - startTime;
  cout << "Time taken: [1m" << elapsed.count() << "[0m" << endl;

  int exitcode = 0;
  string cmd = "diff \"" + fnOut + "\" \"" + fnTest + "\"";
  if (access(fnTest.c_str(), F_OK) != -1) {
    cout << "Diff command: " << cmd << endl;
    int ret = system(cmd.c_str());
    cout << "Diff result: " << ret << endl;
    if (WEXITSTATUS(ret))
      cout << "[41;4mOUTPUT FILE DIFFERS FROM TEST FILE.[0m" << endl;
    else
      cout << "[44;4mdiff succeeded.[0m" << endl;
    exitcode = WEXITSTATUS(ret);
  } else {
    cout << "Diff file missing: " << fnTest << endl;
  }

  return exitcode;
}

// }}}

// clang-format off
// Local variables:
// compile-command: "/opt/clang/bin/clang++ -fsanitize={address,undefined} -fmodules -std=c++11 -Wall -Wextra -g -I/opt/brew/include -L/opt/brew/lib -o D D.cc -lgmp && ./D D.test.in"
// irony-additional-clang-options: ("-std=c++11" "-Wall" "-Wextra" "-I/opt/brew/include" "-I/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1")
// End:
