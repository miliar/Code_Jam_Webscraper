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
  freopen ("A-small-attempt0(1).in", "r", stdin);
  freopen ("A-small-attempt0(1).out", "w", stdout);
  cin >> tests;
  REP (test, tests) {
    int cards[4][4];
    int answer1 , answer2;
    VI candidates1, candidates2;
    cin >> answer1;
    REP (i, 4) REP (j, 4) cin >> cards[i][j];
    REP (i, 4) candidates1.pb(cards[answer1 - 1][i]);
    cin >> answer2;
    REP (i, 4) REP (j, 4) cin >> cards[i][j];
    REP (i, 4) candidates2.pb(cards[answer2 - 1][i]);
    int cnt = 0;
    REP (i, 4) {
      REP (j, 4) {
        if (candidates1[i] == candidates2[j]) cnt++;
      }
    }
    if (cnt == 1) {
      int card;
      REP (i, 4) {
        REP (j, 4) {
          if (candidates1[i] == candidates2[j]) card = candidates1[i];
        }
      }
      cout << "Case #" << test + 1<< ": " << card << endl;
    } else if (cnt > 1) {
      cout << "Case #" << test + 1<< ": Bad magician!" << endl;
    } else if (cnt == 0) {
      cout << "Case #" << test + 1<< ": Volunteer cheated!" << endl;
    }
  }
}
/*
6
4 8 4 7 9 9
*/