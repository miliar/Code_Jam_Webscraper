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


const int kMaxM = 1000 + 10;
struct Pos {
  int pos;
  int num;
  friend bool operator <(const Pos& p1, const Pos& p2) {
    return p1.pos < p2.pos;
  }
};
Pos o[kMaxM], e[kMaxM];

int64 remain, cost;
int n, m, p;

int64 getCost(int L) {
  return (n + n + 1 - L) * (int64)L / 2;
}

int main() {
  int T;
  cin>>T;
  REP (ncase, T) {
    cout << "Case #" << ncase + 1 <<": ";
    scanf("%d%d", &n ,&m);
    cost = 0;
    REP (i, m) {
      scanf("%d%d", &o[i].pos, &e[i].pos);
      scanf("%d", &p);
      e[i].num =o[i].num = p;
      addMod(cost, getCost(e[i].pos - o[i].pos) % kMod * p % kMod);
    }
    sort(o, o + m);
    sort(e, e + m);
    int top1 = 0;
    vector<Pos> st;
    remain = 0;
    REP (i, m) {
      remain += e[i].num;
      while (top1 < m && o[top1].pos <= e[i].pos) {
        st.push_back(o[top1]);
        ++top1;
      }
      while (remain > 0) {
        int64 d = min((int64)st.back().num, remain);
        addMod(cost, kMod - ((getCost(e[i].pos - st.back().pos) % kMod) * d % kMod));
        st.back().num -= d;
        remain -=d ;
        if (st.back().num == 0) {
          st.pop_back();
        }
      }
    }
    cout << cost <<endl;
  }
  return 0;
}

