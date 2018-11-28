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

#define PI 3.14159265358979323
#define EPS 1e-9
typedef pair<double, int> pinfo;

int n;
vector<string> words, sent [1888];
map<string, int> w2i;
vector<int> s [1888];
int lw [11888];

int main() {
  ios_base::sync_with_stdio(false) ;

  int numTests ;
  in >> numTests ;
  FOR(test, 1, numTests + 1) {
    in >> n;
    string line;
    getline(in, line);
    words.clear();
    REP(i, n) {
      getline(in, line);
      istringstream sin(line);
      s [i].clear(); sent [i].clear();
      while (!sin.eof()) {
        string word;
        sin >> word;
        words.push_back(word);
        sent [i].push_back(word);
      }
    }

    RUNIQUE(words);
    REP(iw, SIZE(words)) { w2i [words [iw]] = iw; }
    REP(i, n) {
      s [i].clear();
      REP(is, SIZE(sent [i])) { s [i].push_back(w2i [sent [i] [is]]) ; }
      RUNIQUE(s [i]);
    }
    int ret = SIZE(words);
    REP(comb, (1 << n)) if (((comb & 1) == 0) && (comb & 2) != 0) {
      REP(iw, SIZE(words)) lw [iw] = -1;
      REP(is, SIZE(s [0])) lw [s [0] [is]] = 0;
      REP(is, SIZE(s [1]))  if (lw [s [1] [is]] == -1) lw [s [1] [is]] = 1; else lw [s [1] [is]] = 2;
      FOR(i, 2, n) {
        if ((comb & (1 << i)) != 0) {
          REP(is, SIZE(s [i])) {
            if (lw [s [i] [is]] == -1) lw [s [i] [is]] = 1;
            else if (lw [s [i] [is]] == 0) lw [s [i] [is]] = 2;
          }
        } else {
          REP(is, SIZE(s [i])) {
            if (lw [s [i] [is]] == -1) lw [s [i] [is]] = 0;
            else if (lw [s [i] [is]] == 1) lw [s [i] [is]] = 2;
          }
        }
      }
      int cur = 0;
      REP(iw, SIZE(words)) if (lw [iw] == 2) cur ++;
      ret = MIN(ret, cur);
    }


    cout << "Case #" << test << ": "  << ret << endl;
    out << "Case #" << test << ": "  << ret << endl;
  }

  in.close() ;
  out.close() ;

  return 0;
}
