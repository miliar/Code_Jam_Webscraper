#include <deque>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <complex>
#include <vector>
#include <queue>
#include <map>
#include <set>
#define FOR(i,k,n) for (int i=(k); i<(int)(n); ++i)
#define REP(i,n) for (int i=0; i<(int)(n); ++i)
#define pb push_back
#define ALL(c) c.begin(), c.end()
using namespace std;

inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}
typedef pair<int, int> P;
typedef long long ll;
typedef long double ld;
// const int INF = 1000000100;
// const double eps = 1e-8;

int main(void) {
  int t; cin >> t; int T = t;
  while(t--) {
    ld c, f, x, s, res = 0;
    cin >> c >> f >> x;
    s = 2;
    while(true) {
      // cout << s << endl;
      ld nashi = x / s;
      ld ari = c / s + x / (s + f);
      // cout << c /s << " " << nashi << endl;
      if (ari < nashi) {
        res += c / s;
        s += f;
      } else {
        res += nashi;
        break;
      }
    }
    printf("Case #%d: ", T - t);
    printf("%.7lf\n", (double)res);
  }
  return 0;
}
