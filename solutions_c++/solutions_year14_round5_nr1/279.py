#include <iomanip>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <queue>
#include <fstream>
#include <sstream>
#include <set>
#include <cmath>
#include <map>
#include <iomanip>

using namespace std;

typedef long long int64 ;
typedef unsigned long long uint64 ;
typedef pair<int, int> pint ;
typedef pair<int64, int64> pint64 ;
typedef vector<int> vint ;

#define px first
#define py second

#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define ABS(x) ((x) > 0 ? (x) : -(x))

#define REP(i, n) for (int i = 0 ; i < (n) ; i ++)
#define REPD(i, n) for (int i = (n) ; i >= 0 ; i --)
#define FOR(i, a, b) for (int i = (a) ; i < (b) ; i ++)
#define FORD(i, a, b) for (int i = (a) ; i >= (b) ; i --)

#define MUL64(x, y) (((int64) (x)) * ((int64) (y)))
#define MULMOD(x, y, modul) (MUL64(x, y) % modul)
#define MUL(x, y) MULMOD(x, y, modul)
#define ADD(reg, val) { reg += val ; if (reg >= modul) reg -= modul ; }

#define SET(v, val) memset(v, val, sizeof(v)) ;
#define SIZE(v) ((int) (v).size())
#define ALL(v) (v).begin(), (v).end()
#define SORT(v) { sort(ALL(v)) ; }
#define RSORT(v) { SORT(v) ; REVERSE(v) ; }
#define REVERSE(v) { reverse(ALL(v)) ; }
#define UNIQUE(v) unique((v).begin(), (v).end())
#define RUNIQUE(v) { SORT(v) ; (v).resize(UNIQUE(v) - (v).begin()) ; }

#define BIG
string PROBLEM = "A" ;

#ifdef BIG
ifstream in((PROBLEM + "-large.in").c_str()) ; ofstream out((PROBLEM + "-large.out").c_str()) ;
#endif

#ifndef BIG
ifstream in((PROBLEM + "-small.in").c_str()) ; ofstream out((PROBLEM + "-small.out").c_str()) ;
#endif

#define MAXN 1333888

int64 n, p, q, r, s, t [MAXN], st [MAXN];

#define _sum(x) ((x) < 0 ? 0LL : st [x])
#define sum(l, r) ((l) > (r) ? 0LL : (_sum(r) - _sum((l) - 1)))
int main() {
  ios_base::sync_with_stdio(false) ;

  int numTests ;
  in >> numTests ;
  FOR(test, 1, numTests + 1) {
    in >> n >> p >> q >> r >> s ;
    REP(i, n) { t [i] = (((int64) i * p + q) % r) + s; st [i] = (i > 0 ? st [i - 1] : 0LL) + t [i] ; }
    int64 total = st [n - 1], ret = 0LL;
    REP(i, n) {
      int64 right = sum(i + 1, n - 1), left = sum(0, i);
      int64 cur = max(left, right);
      int64 best = total - cur;
      int idx = lower_bound(st, st + (i + 1), left / 2) - st;
      for (int j = idx - 4 ; j < idx + 5 ; j ++) if (j >= 0 && j <= i) {
        int64 leftleft = sum(0, j - 1), leftright = sum(j, i);
        int64 midcur = max(max(leftleft, leftright), right);
        int64 midbest = total - midcur;
        best = max(best, midbest);
      }
      ret = max(ret, best);
    }
    cout << test << ":" << ret << endl;
    out << "Case #" << test << fixed << setprecision(12) << ": " << 1.0 * ret / total << endl;
  }

  in.close() ;
  out.close() ;

  return 0;
}
