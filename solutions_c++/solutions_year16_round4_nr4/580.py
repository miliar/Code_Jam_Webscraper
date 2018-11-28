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


int n, pw[8], pm[8];
string w[8], op[8];
bool used[8];

bool go(int i) {
    //cout << "go(" << i << ")" << endl;
    if (i == n) return true;
    int iw = pw[i];
    bool have = false;
    REP(k, n) if (op[iw][k] == '1' && !used[k]) {
        have = true;
        used[k] = true;
        if (!go(i + 1)) return false;
        used[k] = false;
    }
    return have;
}

bool check() {
    bool ret = true;
    REP(iw, n) pw[iw] = iw;
    do {
        SET(used, false);
        if (!go(0)) return false;
    } while (next_permutation(pw, pw + n));
    return ret;
}

int main() {
  int numTests ;
  cin >> numTests ;
  FOR(test, 1, numTests + 1) {
    cin >> n;
    REP(i, n) { cin >> w[i]; op[i] = w[i];}
    int ret = n * n;
    REP(comb, (1 << (n * n))) {
        //cout << comb << endl;
        int ib = 0, iw = 0, im = 0, cost = 0;
        bool ok = true;
        while ((ib < (n*n)) && ok) {
            //cout << iw << "," << im << "," << ib << endl;
            if (comb & (1 << ib)) {
                op[iw][im] = '1';
            } else {
                op[iw][im] = '0';
            }
            if (w[iw][im] == '1') {
                if (op[iw][im] == '0') ok = false;
            } else {
                if (op[iw][im] == '1') cost++;
            }
            ib++;
            im++;
            if (im == n) {
                im = 0;
                iw++;
            }
        }
        //cout << comb << "," << ok << endl;
        if (ok) {
            if (check() && cost < ret) ret = cost;
        }
    }
    cout << "Case #" << test << ": " << ret << endl;
  }

  return 0;
}
