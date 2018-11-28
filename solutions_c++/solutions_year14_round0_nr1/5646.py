#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <algorithm>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define SZ(a) (int)(a).size()
#define FOR(i,a,b) for (int i=(a); i<=(b); ++i)
#define REP(i,n) for (int i=0; i<(n); ++i)
#define ALL(c) c.begin(), c.end()
typedef vector<int> VI;
typedef pair<int, int> PII;
#define CLR(c,n) memset(c,n,sizeof(c))
template <class T> void checkmin(T &a, T b) { if (b<a) a=b; }
template <class T> void checkmax(T &a, T b) { if (b>a) a=b; }
#define TR(it, container) for(typeof(container.begin()) it = container.begin();\
it != container.end(); it++)
#define CONTAIN(it, container) (container.find(it)!=container.end())

int main(int argc, char *argv[]) {
  int tc, r1, r2, g1[4][4], g2[4][4];
  cin >> tc;
  FOR(ic, 1, tc) {
    cin >> r1; --r1; REP(i, 4) REP(j, 4) cin >> g1[i][j];
    cin >> r2; --r2; REP(i, 4) REP(j, 4) cin >> g2[i][j];
    int m1 = 0, m2 = 0;
    REP(i, 4) m1 |= 1 << g1[r1][i], m2 |= 1 << g2[r2][i];
    int m = m1 & m2;
    printf("Case #%d: ", ic);
    if (m == 0) printf("Volunteer cheated!\n");
    else if (m & (m-1)) printf("Bad magician!\n");
    else FOR(i, 1, 16) if (m & (1 << i)) printf("%d\n", i);
  }
}
