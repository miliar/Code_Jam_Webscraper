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

#define REP(i, n) for (__typeof(n) i = 0 ; i < (n) ; i ++)
#define REPD(i, n) for (__typeof(n) i = (n) ; i >= 0 ; i --)
#define FOR(i, a, b) for (__typeof(a) i = (a) ; i < (b) ; i ++)
#define FORD(i, a, b) for (__typeof(a) i = (a) ; i >= (b) ; i --)

#define MUL64(x, y) (((int64) (x)) * ((int64) (y)))
#define MULMOD(x, y, modul) (MUL64(x, y) % modul)
#define MUL(x, y) MULMOD(x, y, modul)
#define ADD(reg, val) { reg += val ; if (reg >= modul) reg -= modul ; }

#define SET(v, val) memset(v, val, sizeof(v)) ;

#define BIG
string PROBLEM = "B" ;

#ifdef BIG
ifstream in((PROBLEM + "-large.in").c_str()) ; ofstream out((PROBLEM + "-large.out").c_str()) ;
#endif

#ifndef BIG
ifstream in((PROBLEM + "-small.in").c_str()) ; ofstream out((PROBLEM + "-small.out").c_str()) ;
#endif

int64 n, p ;

int64 f(int64 k) {
  int64 ret = 0LL, under = (1LL << n) - k - 1, pw = (1LL << (n - 1)) ;
  while (under > 0) {
    ret += pw ;
    pw /= 2 ; under = (under - 1) / 2 ;
  }
  //cout << n << "," << p << "->" << k << " " <<ret << endl ;
  return ret ;
}

int main() {
  int numTests ;
  in >> numTests ;
  FOR(test, 1, numTests + 1) {
    in >> n >> p ;
    int64 best = 0, worst = 0 ;
    for (int s = 1 ; s <= n && (1LL << n) - (1LL << (n - s + 1)) + 1 <= p ; s ++) {
      best = (1LL << s) - 2 ;
    }
    if (p == (1LL << n)) best = (1LL << n) - 1 ;
    int64 low = 0, high = (1LL << n) - 1, mid, under = (1LL << n) - p ;
    cout << "TEST " << test << endl ;
    while (low <= high) {
      mid = low + (high - low) / 2 ;
      cout << low << "," << mid << "," << high << endl ;
      if (f(mid) >= under) { worst = MAX(worst, mid) ; low = mid + 1 ; }
      else high = mid - 1 ;
    }
    if (p == (1LL << n)) worst = (1LL << n) - 1 ;
    out << "Case #" << test << ": " << best << " " << worst << endl ;
  }
  in.close() ;
  out.close() ;

  return 0;
}
