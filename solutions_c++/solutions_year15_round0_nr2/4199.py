/* Written by Filip Hlasek 2015 */
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstring>

#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define REP(i,b) for(int i=0;i<(b);i++)

using namespace std;

#define MAXN 1111
int N, P[MAXN];

int get_cuts(int x, int eating) {
  return (x - 1) / eating;
}

bool possible(int y) {
  FOR(eating, 1, y) {
    long long sum = 0;
    REP(i, N) sum += get_cuts(P[i], eating);
    if (sum <= y - eating) return true;
  }
  return false;
}

int main(int argc, char *argv[]) {
  int T;
  scanf("%d", &T);
  FOR(t, 1, T) {
    scanf("%d", &N);
    REP(i, N) scanf("%d", P + i);
    int l = 1, r = MAXN;
    while (l < r) {
      int m = (l + r) / 2;
      if (possible(m)) r = m;
      else l = m + 1;
    }
    printf("Case #%d: %d\n", t, l);
  }
  return 0;
}
