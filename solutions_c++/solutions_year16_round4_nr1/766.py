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

typedef pair<pint, int> pinfo;

string imp = "IMPOSSIBLE";

string ret, cur;

int n, r, p, s;
map<pinfo, string> cache;

string gen(int r, int s, int p) {
    //cout << "gen(" << r << "," << s << "," << p << ")" << endl;
    pinfo info(pint(r, s), p);
    if (cache.find(info) != cache.end()) return cache[info];
    if (r == 0 && s == 1 && p == 1) return "PS";
    else if (s == 0  && r == 1 && p == 1) return "PR";
    else if (p == 0  && s == 1 && r == 1) return "RS";
    else {
        int k = p + r + s;
        string &ret = cache[info];
        ret = imp;
        if (k % 3 == 1) {
            if (p == (k / 3) + 1) {
                string tmp = gen(r / 2, s / 2 + 1, p / 2) + gen(r / 2 + 1, s / 2, p / 2);
                //cout << tmp << (tmp.find(imp) == string::npos && (ret == imp || ret > tmp)) << endl;
                if (tmp.find(imp) == string::npos && (ret == imp || ret > tmp)) ret = tmp;
                tmp = gen(r / 2 + 1, s / 2, p / 2) + gen(r / 2, s / 2 + 1, p / 2);
                //cout << tmp << (tmp.find(imp) == string::npos && (ret == imp || ret > tmp)) << endl;
                if (tmp.find(imp) == string::npos && (ret == imp || ret > tmp)) ret = tmp;
            }
            if (r == (k / 3) + 1) {
                string tmp = gen(r / 2, s / 2 + 1, p / 2) + gen(r / 2, s / 2, p / 2 + 1);
                //cout << tmp << (tmp.find(imp) == string::npos && (ret == imp || ret > tmp)) << endl;
                if (tmp.find(imp) == string::npos && (ret == imp || ret > tmp)) ret = tmp;
                tmp = gen(r / 2, s / 2, p / 2 + 1) + gen(r / 2, s / 2 + 1, p / 2);
                //cout << tmp << (tmp.find(imp) == string::npos && (ret == imp || ret > tmp)) << endl;
                if (tmp.find(imp) == string::npos && (ret == imp || ret > tmp)) ret = tmp;
            }
            if (s == (k / 3) + 1) {
                string tmp = gen(r / 2, s / 2, p / 2 + 1) + gen(r / 2 + 1, s / 2, p / 2);
                //cout << tmp << (tmp.find(imp) == string::npos && (ret == imp || ret > tmp)) << endl;
                if (tmp.find(imp) == string::npos && (ret == imp || ret > tmp)) ret = tmp;
                tmp = gen(r / 2 + 1, s / 2, p / 2) + gen(r / 2, s / 2, p / 2 + 1);
                //cout << tmp << (tmp.find(imp) == string::npos && (ret == imp || ret > tmp)) << endl;
                if (tmp.find(imp) == string::npos && (ret == imp || ret > tmp)) ret = tmp;
            }
        } else {
            k++;
            if (p == (k / 3) - 1) {
                string tmp = gen(r / 2, s / 2 + 1, p / 2) + gen(r / 2 + 1, s / 2, p / 2);
                //cout << tmp << (tmp.find(imp) == string::npos && (ret == imp || ret > tmp)) << endl;
                if (tmp.find(imp) == string::npos && (ret == imp || ret > tmp)) ret = tmp;
                tmp = gen(r / 2 + 1, s / 2, p / 2) + gen(r / 2, s / 2 + 1, p / 2);
                //cout << tmp << (tmp.find(imp) == string::npos && (ret == imp || ret > tmp)) << endl;
                if (tmp.find(imp) == string::npos && (ret == imp || ret > tmp)) ret = tmp;
            }
            if (r == (k / 3) - 1) {
                string tmp = gen(r / 2, s / 2 + 1, p / 2) + gen(r / 2, s / 2, p / 2 + 1);
                //cout << tmp << (tmp.find(imp) == string::npos && (ret == imp || ret > tmp)) << endl;
                if (tmp.find(imp) == string::npos && (ret == imp || ret > tmp)) ret = tmp;
                tmp = gen(r / 2, s / 2, p / 2 + 1) + gen(r / 2, s / 2 + 1, p / 2);
                //cout << tmp << (tmp.find(imp) == string::npos && (ret == imp || ret > tmp)) << endl;
                if (tmp.find(imp) == string::npos && (ret == imp || ret > tmp)) ret = tmp;
            }
            if (s == (k / 3) - 1) {
                string tmp = gen(r / 2, s / 2, p / 2 + 1) + gen(r / 2 + 1, s / 2, p / 2);
                //cout << tmp << (tmp.find(imp) == string::npos && (ret == imp || ret > tmp)) << endl;
                if (tmp.find(imp) == string::npos && (ret == imp || ret > tmp)) ret = tmp;
                tmp = gen(r / 2 + 1, s / 2, p / 2) + gen(r / 2, s / 2, p / 2 + 1);
                //cout << tmp << (tmp.find(imp) == string::npos && (ret == imp || ret > tmp)) << endl;
                if (tmp.find(imp) == string::npos && (ret == imp || ret > tmp)) ret = tmp;
            }
        }
        return ret;
    }
}

void solve(int n, int r, int p, int s) {
    int k = (1 << n);
    if (n > 1) {
        if (k % 3 == 1) {
            if ((p == (k / 3) + 1 && r == (k / 3) && s == (k / 3))
                || (p == (k / 3) && r == (k / 3) + 1 && s == (k / 3))
                || (p == (k / 3) && r == (k / 3) && s == (k / 3) + 1)) ret = gen(r, s, p);
        } else {
            k++;
            if ((p == (k / 3) - 1 && r == (k / 3) && s == (k / 3))
                || (p == (k / 3) && r == (k / 3) - 1 && s == (k / 3))
                || (p == (k / 3) && r == (k / 3) && s == (k / 3) - 1)) ret = gen(r, s, p);
        }
    } else {
        if ((p == 1 && r == 1) || (p == 1 && s == 1) || (s == 1 && r == 1)) ret = gen(r, s, p);
    }
}


int main() {
  int numTests ;
  cin >> numTests ;
  FOR(test, 1, numTests + 1) {
    cin >> n >> r >> p >> s;
    ret = imp;
    solve(n, r, p, s);

    cout << "Case #" << test << ": " << ret << endl;
  }

  return 0;
}
