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
#include <ctime>

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
string PROBLEM = "C" ;

#ifdef BIG
ifstream in((PROBLEM + "-large.in").c_str()) ; ofstream out((PROBLEM + "-large.out").c_str()) ;
#endif

#ifndef BIG
ifstream in((PROBLEM + "-small.in").c_str()) ; ofstream out((PROBLEM + "-small.out").c_str()) ;
#endif

/**** MIN COST MAX FLOW ****/
#define MAX_N 1888 * 1888 * 2 * 2
#define MAX_E 6 * MAX_N
#define INF 100000000

int numNodes, numEdges, source, target ;
int head [MAX_N], node [MAX_E], next [MAX_E], flow [MAX_E], cap [MAX_E], cost [MAX_E] ;

void INIT(int _numNodes, int _source, int _target) { numNodes = _numNodes ; source = _source ; target = _target ; numEdges = 0 ; REP(u, numNodes) head [u] = -1 ; }
void ADD_EDGE(int u, int v, int _cap, int _cost) { node [numEdges] = v, cap [numEdges] = _cap, cost [numEdges] = _cost, flow [numEdges] = 0, next [numEdges] = head [u], head [u] = numEdges ++ ; node [numEdges] = u, cap [numEdges] = 0, cost [numEdges] = -_cost, flow [numEdges] = 0, next [numEdges] = head [v], head [v] = numEdges ++ ; }
pint MCMF() { int maxFlow = 0, minCost = 0 ; int d [numNodes], f [numNodes], p [numNodes], edge [numNodes] ; bool changed [numNodes] ; while (true) { REP(u, numNodes) d [u] = INF, p [u] = -1, changed [u] = false, f [u] = INF ; d [source] = 0 ; changed [source] = true ; bool ok = true ; while (ok) { ok = false ; REP(u, numNodes) if (changed [u]) { changed [u] = false ; for (int v, k = head [u] ; k >= 0 ; k = next [k]) { v = node [k] ; if (flow [k] < cap [k] && d [u] + cost [k] < d [v]) { d [v] = d [u] + cost [k] ; p [v] = u ; f [v] = min(f [u], cap [k] - flow [k]) ; changed [v] = true ; edge [v] = k ; ok = true ; } } } } if (d [target] >= INF) break ; maxFlow += f [target] ; minCost += f [target] * d [target] ; for (int v = target ; v != source ; v = p [v]) { flow [edge [v]] += f [target] ; flow [edge [v] ^ 1] -= f [target] ; } } return pint(maxFlow, minCost) ; }
/****************************/

#define MAXB 1888
#define MAXW 1888
#define MAXH 1888

int dx [4] = {0, 1, 0, -1}, dy [4] = {1, 0, -1, 0};
int W, H, B, xx0 [MAXB], xx1 [MAXB], yy0 [MAXB], yy1 [MAXB], pxl [MAXB], pyl [MAXB], pxr [MAXB], pyr [MAXB], DELTA;
vector<int> vx, vy;
int t [MAXB] [MAXB];
bool used [MAXW] [MAXH];

#define IN(x, y) ((y) * W + (x))
#define OUT(x, y) (DELTA + IN(x, y))
int can(int way, int x, int y, int &nx, int &ny) {
  nx = x + dx [way] ; ny = y + dy [way];
  return (nx >= 0 && nx < W && ny >= 0 && ny < H);
}
int main() {
  ios_base::sync_with_stdio(false) ;

  int numTests ;
  in >> numTests ;
  FOR(test, 1, numTests + 1) {
    in >> W >> H >> B;
    vx.clear(); vy.clear();
    vx.push_back(0); vx.push_back(2 * W - 1);
    vy.push_back(0); vy.push_back(2 * H - 1);
    REP(ix, W) REP(iy, H) used [iy] [ix] = false;
    REP(i, B) {
      in >> xx0 [i] >> yy0 [i] >> xx1 [i] >> yy1 [i] ;
      FOR(ix, xx0 [i], xx1 [i] + 1) FOR(iy, yy0 [i], yy1 [i] + 1) used [iy] [ix] = true;
      pxl [i] = 2 * xx0 [i] ; pyl [i] = 2 * yy0 [i] ; pxr [i] = 2 * xx1 [i] - 1; pyr [i] = 2 * yy1 [i] - 1;
      vx.push_back(2 * xx0 [i]) ; vx.push_back(2 * xx1 [i] - 1);
      vy.push_back(2 * yy0 [i]) ; vy.push_back(2 * yy1 [i] - 1);
    }
    RUNIQUE(vx) ; RUNIQUE(vy);
    INIT(W * H * 2 + 2, W * H * 2, W * H * 2 + 1);
    int DELTA = W * H;
    REP(ix, W) if (!used [0] [ix]) {
      int u = IN(ix, 0), v = OUT(ix, 0);
      ADD_EDGE(source, u, 1, 0);
      u = IN(ix, H - 1), v = OUT(ix, H - 1);
      ADD_EDGE(u, target, 1, 0);
    }
    REP(ix, W) REP(iy, H) if (!used [iy] [ix]) ADD_EDGE(IN(ix, iy), OUT(ix, iy), 1, 0);
    REP(ix, W) REP(iy, H) if (!used [iy] [ix]) {
      int nx, ny;
      REP(way, 4) if (can(way, ix, iy, nx, ny)) {
        if (!used [ny] [nx]) { ADD_EDGE(OUT(ix, iy), IN(nx, ny), 1, 0) ; }
      }
    }
    /*
    int sizeTable = SIZE(vx) * SIZE(vy);
    REP(ix, SIZE(vx)) {
      REP(iy, SIZE(vy)) {
        t [ix] [iy] = 0;
      }
    }
    */
    cout<<"A" << endl;
    pint ret = MCMF();
    out << "Case #" << test << ": " << ret.first << endl ;
  }

  in.close() ;
  out.close() ;

  return 0;
}
