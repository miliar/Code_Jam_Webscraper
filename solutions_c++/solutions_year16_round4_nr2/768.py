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
string PROBLEM = "C" ;

#ifdef BIG
//ifstream in((PROBLEM + "-large.in").c_str()) ; ofstream out((PROBLEM + "-large.out").c_str()) ;
#endif

#ifndef BIG
ifstream in((PROBLEM + "-small.in").c_str()) ; ofstream out((PROBLEM + "-small.out").c_str()) ;
#endif


#define MAXN 222

int n, k;
double p[MAXN];
double dp[MAXN][MAXN][MAXN];
vector<double> v;

double solve(int k, int yes, int no) {
    if (k < 0 || yes < 0 || no < 0) return 0.0;
    double &ret = dp[k][yes][no];
    //cout << "in" << k << "," << yes << "," << no << ": " << ret << "   " << v[k] << endl;
    if (ret > -0.5) return ret;
    ret = 0.0;
    if (k == 0) {
        if (yes + no != 1) return 0.0;
        if (yes == 1) return (ret = v[0]);
        else return (ret = 1.0 - v[0]);
    } else {
        double tmp = 0.0;
        if (yes > 0) {
            ret += v[k] * solve(k - 1, yes - 1, no);
            //if (tmp > ret) ret = tmp;
        }
        if (no > 0) {
            ret += (1.0 - v[k]) * solve(k - 1, yes, no - 1);
            //if (tmp > ret) ret = tmp;
        }
    }
    //cout << k << "," << yes << "," << no << ": " << ret << "   " << v[k] << endl;
    return ret;
}

int main() {
  int numTests ;
  cin >> numTests ;
  FOR(test, 1, numTests + 1) {
    cin >> n >> k;
    REP(i, n) cin >> p[i];
    sort(p, p + n);
    double ret = 0.0;
    int bl = -1;
    REP(l, k + 1) {
        v.clear();
        REP(i, l) v.push_back(p[i]);
        REP(i, k - l) v.push_back(p[n - i - 1]);
        //cout << "l = " << l << endl;
        //REP(i, v.size()) cout << v[i] << " " ; cout << endl;
        sort(v.begin(), v.end());
        REP(a, k + 1) REP(b, k + 1) REP(c, k + 1) dp[a][b][c] = -1.0;
        double tmp = solve(v.size() - 1, k / 2, k / 2);
        if (tmp > ret) { ret = tmp; bl = l; }
    }
    cout << "Case #" << test << ": " << ret << endl;
  }

  return 0;
}
