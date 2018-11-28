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

int nr, nc, dr [4] = {-1, 1, 0, 0}, dc [4] = {0, 0, -1, 1};
char t [888] [888];

int main() {
  ios_base::sync_with_stdio(false) ;
  map<char, int> dir;
  dir ['^'] = 0; dir ['>'] = 3; dir ['<'] = 2; dir ['v'] = 1;

  int numTests ;
  in >> numTests ;
  FOR(test, 1, numTests + 1) {
    in >> nr >> nc;
    REP(r, nr) in >> t [r];
    int ret = 0;
    REP(r, nr) REP(c, nc) if (t [r] [c] != '.') {
      int way = dir [t [r] [c]];
      int cr = r + dr [way], cc = c + dc [way];
      bool out = true;
      while (cr >= 0 && cr < nr && cc >= 0 && cc < nc && out) {
        if (t [cr] [cc] != '.') out = false;
        cr += dr [way]; cc += dc [way];
      }
      if (out) {
        REP(way, 4) {
          int cr = r + dr [way], cc = c + dc [way];
          while (cr >= 0 && cr < nr && cc >= 0 && cc < nc && out) {
            if (t [cr] [cc] != '.') out = false;
            cr += dr [way]; cc += dc [way];
          }
        }
        if (out) ret = -1; else if (ret != -1) ret ++;
      }
    }
    out << "Case #" << test << ": ";
    if (ret != -1) out << ret << endl;
    else out << "IMPOSSIBLE" << endl;
  }
  in.close() ;
  out.close() ;

  return 0;
}
