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
typedef pair<int, int> pint ;
typedef pair<int64, int64> pint64 ;
typedef vector<int> vint ;

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

#define SUB(x, y) ((((x) % modul) + modul - ((y) % modul)) % modul)
//#define BIG
string PROBLEM = "A" ;

#ifdef BIG
ifstream in((PROBLEM + "-large.in").c_str()) ; ofstream out((PROBLEM + "-large.out").c_str()) ;
#endif

#ifndef BIG
ifstream in((PROBLEM + "-small.in").c_str()) ; ofstream out((PROBLEM + "-small.out").c_str()) ;
#endif

#define MAXM 3888

typedef pair<int64, pint64> pinfo ;

int n, m ;
int64 s [MAXM], e [MAXM], p [MAXM], r [MAXM], modul = 1000002013 ;
vector<pinfo> v ;

int main() {
  int numTests ;
  in >> numTests ;
  FOR(test, 1, numTests + 1) {
    in >> n >> m ;
    v.clear() ;
    int64 cost = 0LL ;
    REP(i, m) {
      in >> s [i] >> e [i] >> p [i] ; r [i] = p [i] ;
      int64 d = e [i] - s [i] ;
      d = ((d * (d + 1)) / 2) % modul ;
      d = MUL(d, p [i]) ;
      ADD(cost, d) ;
      v.push_back(pinfo(s [i], pint(-1, i))) ;
      v.push_back(pinfo(e [i], pint(1, i))) ;
    }
    sort(v.begin(), v.end()) ;
    int64 best = 0LL, cur = 0LL, cnt = 0LL, lastX = v [0].first, tmp ;
    priority_queue<pinfo> q ;
    int iv = 0 ;
    cout << "TEST #" << test << "   " << cost << endl ;
    while (iv < v.size()) {
      int64 x = v [iv].first ;
      tmp = MUL(x - lastX, cur) ;
      ADD(best, tmp) ;
      tmp = (((x - lastX) * (x - lastX + 1)) / 2) % modul ;
      tmp = MUL(tmp, cnt) ;
      ADD(best, tmp) ;
      tmp = MUL(x - lastX, cnt) ;
      ADD(cur, tmp) ;
      cout << x << " " << cur << " " << cnt << "  " << best << endl ;
      while (iv < v.size() && v [iv].first == x) {
        int op = v [iv].second.first, idx = v [iv].second.second ;
        if (op == -1) {
          cnt += p [idx] ;
          q.push(pinfo(s [idx], pint(p [idx], idx))) ;
        } else {
          int64 rem = p [idx], curE = e [idx] ;
          cnt -= rem ;
          int64 sum = 0LL ;
          cout << "   rem = " << rem << ", idx = " << idx << ", " << s [idx] << "," << e [idx] ;
          while (rem > 0) {
            //cout << q.size() << endl ;
            while (r [q.top().second.second] == 0) q.pop() ;
            int nid = q.top().second.second ;
            int64 curS = s [nid], curP = r [nid] ;
            int64 next = MIN(rem, curP) ;
            tmp = ((curE - curS) * next) % modul ;
            ADD(sum, tmp) ;
            r [nid] -= next ; rem -= next ;
            cout << "  nid = " << nid << " " ;
          }
          cout << "  sum = " << sum << endl ;
          cur = SUB(cur, sum) ;
        }
        iv ++ ;
      }
      lastX = x ;
    }
    cout << "best = " << best << endl ;
    cost = (best + modul - cost) % modul ;
    out << "Case #" << test << ": " << cost << endl ;
  }
  in.close() ;
  out.close() ;

  return 0;
}
