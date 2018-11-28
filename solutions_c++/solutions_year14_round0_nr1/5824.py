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

int c[4][4];
  
int main(void) {
  int t; cin >> t; 
  int T = t;
  while(t--) {
    vector<int> fir, sec, res;
    int r; cin >> r;
    REP(i, 4) REP(j, 4) {
      cin >> c[i][j];
    }
    REP(j, 4) fir.pb(c[r - 1][j]);
    cin >> r;
    REP(i, 4) REP(j, 4) {
      cin >> c[i][j];
    }
    REP(j, 4) sec.pb(c[r - 1][j]);
    REP(i, 4) {
      REP(j, 4) {
        if (fir[i] == sec[j]) {
          res.pb(fir[i]);
          break;
        }
      }
    }
    printf("Case #%d: ", T - t);
    if (res.size() >= 2) cout << "Bad magician!" << endl;
    else if (res.size() == 0) cout << "Volunteer cheated!" << endl;
    else cout << res[0] << endl;
  }
  return 0;
}
