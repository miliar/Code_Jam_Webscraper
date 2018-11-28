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

//#define BIG
string PROBLEM = "D" ;

#ifdef BIG
ifstream in((PROBLEM + "-large.in").c_str()) ; ofstream out((PROBLEM + "-large.out").c_str()) ;
#endif

#ifndef BIG
ifstream in((PROBLEM + "-small.in").c_str()) ; ofstream out((PROBLEM + "-small.out").c_str()) ;
#endif

#define MAXM 1888
#define MAXN 1888

int n, m, maxN, cntMax, id [MAXM], cnt [MAXM];
string s [MAXM];
vector<int> w [MAXN];
map<int, int> cache;
vector<string> x;

int h(int idx, int l, int r) {
  if (l > r) return 0;
  if (l == r) return (idx <= SIZE(x [l])) ? SIZE(x [l]) - idx : 0;
  int lastL = l, nextL = l;
  int ret = 0;
  while (lastL <= r) {
    while (lastL <= r && SIZE(x [lastL]) <= idx) lastL ++;
    nextL = lastL ;
    while (nextL <= r && (SIZE(x [nextL]) > idx && x [nextL] [idx] == x [lastL] [idx])) nextL ++;
    if (lastL <= r) {
      int tmp = h(idx + 1, lastL, nextL - 1);
      ret += 1 + tmp;
    }
    lastL = nextL;
  }
  return ret;
}
int g(vector<int> &v) {
  int comb = 0;
  REP(i, SIZE(v)) comb |= (1 << v [i]);
  if (cache.find(comb) != cache.end()) return cache [comb];
  int ret = 0;
  x.clear();
  REP(i, SIZE(v)) x.push_back(s [v [i]]) ;
  SORT(x);
  ret = h(0, 0, SIZE(x) - 1);
  //cout << "g: " ; REP(i, SIZE(x)) cout << x [i] << " " ; cout << ret << endl;
  return (cache [comb] = ret);
}
void f(int idx) {
  if (idx == m) {
    bool ok = true;
    REP(i, n) if (cnt [i] == 0) { ok = false ; break ; }
    if (ok) {
      REP(i, n) w [i].clear();
      REP(i, m) w [id [i]].push_back(i);
      //cout << "CUR: " << endl;
      //REP(i, n) { cout << i << ": " ; REP(j, SIZE(w [i])) cout << w [i] [j] << "," << s [w [i] [j]] << "   " ; cout << endl ;}
      int curCnt = n;
      REP(i, n) {
        int tmp = g(w [i]);
        //cout << "RETURN " << i << " " << tmp << endl ;
        curCnt += tmp;
      }
      if (curCnt > maxN) { maxN = curCnt ; cntMax = 1 ; }
      else if (curCnt == maxN) cntMax ++;
    }
  } else {
    REP(i, n) {
      id [idx] = i; cnt [i] ++ ;
      f(idx + 1);
      cnt [i] --;
    }
  }
}
int main() {
  ios_base::sync_with_stdio(false) ;

  int numTests ;
  in >> numTests ;
  FOR(test, 1, numTests + 1) {
    in >> m >> n ;
    REP(i, m) in >> s [i];
    maxN = 0; cntMax = 0;
    SET(cnt, 0) ; SET(id, 0); cache.clear() ;
    f(0);
    cout << test << ":" << maxN << " " << cntMax << endl;
    out << "Case #" << test << ": " << maxN << " " << cntMax << endl ;
  }

  in.close() ;
  out.close() ;

  return 0;
}
