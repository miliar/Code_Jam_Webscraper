// Headers {{{
#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;
#define REP(i,n) for(int i=0; i<(n); ++i)
#define FOR(i,j,k) for(int i=(j); i<=(k); ++i)
#define FORD(i,j,k) for(int i=(j); i>=(k); --i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define ST first
#define ND second
#define MP make_pair
#define ALL(a) (a).begin(),(a).end()
#define SQR(a) ((a)*(a))
#define debug(x) cerr << #x << " = " << x << '\n'
#define size(x) ((int)(x).size())
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<pair<int,int> > VPII;
typedef unsigned long long ULL;
typedef long long LL;
typedef long double LD;
typedef pair<int,int> PII;
const int INF=1000000000;
// }}}

const int MX = 105;

int n, m;
int a[MX][MX];
int mxrow[MX], mxcol[MX];

void tc(int num) {
  printf("Case #%d: ", num);
  scanf("%d%d", &n, &m);
  REP (i, n) REP (j, m) scanf("%d", &a[i][j]);
  REP (i, n) mxrow[i] = -1;
  REP (j, m) mxcol[j] = -1;
  REP (i, n) REP (j, m) {
    mxrow[i] = max(mxrow[i], a[i][j]);
    mxcol[j] = max(mxcol[j], a[i][j]);
  }
  REP (i, n) REP (j, m) if (a[i][j] < mxrow[i] && a[i][j] < mxcol[j]) {
    printf("NO\n");
    return;
  }
  printf("YES\n");
}

int main() {
  int ntc;
  scanf("%d", &ntc);
  FOR (i, 1, ntc) tc(i);
  return 0;
}
