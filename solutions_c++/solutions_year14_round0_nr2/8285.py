#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <sstream>
#include <vector>
#include <complex>
#include <ctime>
#include <stack>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> VI;
typedef vector< VI > VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
  
#define REP(i, n) for(int i = 0; i < (n); ++i)
#define RREP(i, n) for(int i = (n) - 1; i >= 0; --i)
#define FOR(i, x, y) for(int i = (x); i <= (y); ++i)
#define RFOR(i, x, y) for(int i = (x); i >= (y); --i)
#define SZ(a) (ll)(a).size()
#define ALL(a) (a).begin(),(a).end()
#define SORT(a) sort(ALL(a)) 
#define CLEAR(x) memset(x, 0, sizeof x);
#define COPY(FROM, TO) memcpy(TO, FROM, sizeof TO);
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define pb push_back
#define mk make_pair
#define sqr(x) ((x)*(x))
#define X first
#define Y second
const long double pi=acos(-1.0);
const double EPS = 1E-9;
const int INF = 2 * (1e+9) + 1;
const int NMAX = 1000000;
const int MOD = (1e+9) + 7;

int tests;
int main () {
  freopen ("B-large.in", "r", stdin);
  freopen ("B-large.out", "w", stdout);
  scanf ("%d", &tests);
  REP (test, tests) {
    double c, f, x;
    scanf ("%lf%lf%lf", &c, &f, &x);
    int cur = 0;
    double per_sec = 2, time = 0;
    while (1) {
      time += c / per_sec;
      double t1 = (x - c) / per_sec;
      double t2 = x / (per_sec + f);
      if (t1 < t2) {
        time += t1;
        break;
      } else {
        //time += c / per_sec;
        per_sec += f;
      }
    }
    printf("Case #%d: %.7lf\n", test + 1, time);
  }
}
/*
1
500.0 4.0 2000.0

4
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0
*/