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
string PROBLEM = "B" ;

#ifdef BIG
ifstream in((PROBLEM + "-large.in").c_str()) ; ofstream out((PROBLEM + "-large.out").c_str()) ;
#endif

#ifndef BIG
ifstream in((PROBLEM + "-small.in").c_str()) ; ofstream out((PROBLEM + "-small.out").c_str()) ;
#endif

#define MAXN 1888
#define MAXD 12

int n, a [MAXN], b [MAXN], p [MAXN], used [MAXN];
map<int, int> id;

int main() {
  ios_base::sync_with_stdio(false) ;

  int numTests ;
  in >> numTests ;
  FOR(test, 1, numTests + 1) {
    id.clear();

    in >> n;
    REP(i, n) { in >> a [i] ;b [i] = a [i] ; used [i] = 0;}
    sort(b, b + n);
    REP(i, n) id [b [i]] = i;
    REP(i, n) p [i] = id [a [i]];
    int ret = 0;
    REP(i, n) {
      int lft = 0, lsk = 0, rgt = 0, rsk = 0, ip = 0;
      while (p [ip] != i) { lft ++ ; lsk += used [ip] ; ip ++ ; }
      used [ip] = 1;
      ip ++;
      while (ip < n) { rgt ++ ; rsk += used [ip] ; ip ++ ; }
      ret += min(lft - lsk, rgt - rsk) ;
    }
    cout << test << ":" << ret << endl;
    out << "Case #" << test << ": " << ret << endl ;
  }

  in.close() ;
  out.close() ;

  return 0;
}
