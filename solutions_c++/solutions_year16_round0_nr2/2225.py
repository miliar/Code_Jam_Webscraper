/* Written by Filip Hlasek 2016 */
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

char p[1111];
int N;

int main(int argc, char *argv[]) {
  int T;
  scanf("%d", &T);
  FOR(t, 1, T) {
    printf("Case #%d: ", t);
    scanf("%s", p);
    N = strlen(p);
    p[N] = '+';
    int ans = 0;
    REP(i, N) ans += p[i] != p[i + 1];
    printf("%d\n", ans);
  }
  return 0;
}
