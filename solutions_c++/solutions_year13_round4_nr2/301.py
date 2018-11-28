#include <iostream>
#include <cstdio>
#include <algorithm>
#include <functional>
#include <numeric>
#include <vector>
#include <set>
#include <map>
#include <queue>
using namespace std;
//{{{Commonly used macro
//-----------------------By cylixstar-----------------------//
#define REP(i, n) for (int n_##__LINE__= (n), i = 0; i < n_##__LINE__; ++i)
#define FOR(i, f, t) for (__typeof__(f) f_##__LINE__=(f), t_##__LINE__=(t), i = f_##__LINE__; i <= t_##__LINE__; ++i)
#define TR(c, it) for (__typeof__((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define ALL(c) (c).begin(), (c).end()
#define SZ(a) ((int)(a).size())
#define CLR(a, v) do { memset(a, v, sizeof(a)); } while(0)
#define DBG(a) do { std::cout << "[" << __FUNCTION__ << "]" << #a << ": " << a << endl; } while(0)

template<typename T>
inline void checkMax(T& a, const T& b) {
  if (a < b) a = b;
}

template<typename T>
inline void checkMin(T& a, const T& b) {
  if (a > b) a = b;
}

//}}}
//{{{Macros about counting problems
//-----------------------By cylixstar-----------------------//
//please customize this values
typedef long long int64;
const int kMod = 1000002013;

template <typename U, typename V>
inline void addMod(U& x, const V y) {
  x += y;
  if (x >= kMod) {
    x -= kMod;
  }
}

template <int N, int MOD>
struct CombinationTable {
  CombinationTable() { init(); }
  static int table[N + 1][N + 1];
  static void init() {
    table[0][0] = 1;
    for (int i = 1; i <= N; ++i) {
      table[i][0] = table[i][i] = 1;
      for(int j = 1; j < i; ++j) {
        table[i][j] = table[i - 1][j] + table[i - 1][j - 1];
        if (table[i][j] >= MOD) {
          table[i][j] -= MOD;
        }
      }
    }
  }
};

template <int N, int MOD>
int CombinationTable<N, MOD>::table[N + 1][N + 1];
//}}}


int n;
int64 p;
int64 tot;

int64 higest(int64 v) {
  while ((v & -v) != v) {
    v -= v & -v;
  }
  return v;
}


struct bestRank {
  int64 operator ()(int64 n, int64 K) {
    if (K == 0) return 0;
    int64 tot = 1LL << n;
    if (K >= (tot >> 1)) {
      return ((*this)(n - 1, K - higest(K)) << 1) + 1;
    } else return 1;
  }
};

struct worstRank {
  int64 operator ()(int64 n, int64 K) {
    if (K == 0) return 0;
    int64 tot = 1LL << n;
    return tot - bestRank()(n, tot - 1 - K) - 1;
  }
};

template <class T>
int64 getAnswer(T ranker) {
  int64 L = 0, R = tot - 1;
  while (L < R) {
    int64 mid = (L + R + 1) >> 1;
    if (ranker(n, mid) < p) {
      L = mid;
    } else {
      R = mid - 1;
    }
  }
  return L;
}

int main() {
  int T;
  cin>>T;
  REP (ncase, T) {
    cout << "Case #" << ncase + 1 <<": ";
    cin>>n>>p;
    tot = 1LL << n;
    bestRank r1;
    worstRank r2;
    cout << getAnswer(r2) <<' '<<getAnswer(r1) <<endl;
  }
  return 0;
}

