// Authored by dolphinigle
// GCJ 2013 3

#include <vector>
#include <list>
#include <map>
#include <set>

#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <assert.h>

#define FORN(X,Y) for (int (X) = 0;(X) < (Y);++(X))
#define REP(X,Y,Z) for (int (X) = (Y);(X) < (Z);++(X))

#define RE(X,Y) for (int (X) = 0;(X) < (Y);++(X))
#define FOR(X,Y,Z) for (int (X) = (Y);(X) <= (Z);++(X))

#define SZ(Z) ((int)(Z).size())
#define ALL(W) (W).begin(), (W).end()
#define PB push_back

#define MP make_pair
#define A first
#define B second

#define INF 1023123123
#define EPS 1e-11

#define MX(Z,Y) Z = max((Z),(Y))
#define MN(X,Y) X = min((X),(Y))

#define FORIT(X,Y) for(typeof((Y).begin()) X = (Y).begin();X!=(Y).end();X++)

using namespace std;

typedef long long ll;
typedef double db;
typedef vector<int> vint;

map<string, db> res;

db Solve(string x) {
  if (res.count(x)) return res[x];
  int n = SZ(x);
  int remain = 0;
  FORN(i, n) if (x[i] == '.') ++remain;
  if (!remain) {
    return res[x] = 0.0;
  }
  db ret = 0.0;
  FORN(i, n) {
    // comes here
    int pos = i;
    db pay = n;
    while (x[pos] == 'X') {
      pos = (pos+1)%n;
      pay -= 1.0;
    }
    x[pos] = 'X';
    ret += pay + Solve(x);
    x[pos] = '.';
  }
  ret /= (db)n;
  res[x] = ret;
  return ret;
}

int main() {
  int ntc;
  cin >> ntc;
  FORN(itc, ntc) {
    cout << "Case #" << (itc+1) << ": ";
    string str;
    cin >> str;
    printf("%.10lf\n", Solve(str));
  }
}
