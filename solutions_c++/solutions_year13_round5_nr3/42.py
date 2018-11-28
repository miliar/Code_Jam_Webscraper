/* Written by Filip Hlasek 2013 */
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

int N, M, P;
#define MAXN 2222
int u[MAXN], v[MAXN], a[MAXN], b[MAXN];
int id[MAXN];
int dist[MAXN][MAXN];
bool ok[MAXN];

int main(int argc, char *argv[]){
  int T; 
  scanf("%d", &T);
  REP(t, T) {
    printf("Case #%d: ", t + 1);
    scanf("%d%d%d", &N, &M, &P);
    REP(i, M) {
      scanf("%d%d%d%d", u + i, v + i, a + i, b + i);
      u[i]--; v[i]--;
    }
    REP(i, P) { scanf("%d", id + i); id[i]--; }
    REP(i, P) ok[i] = false;

    if(t + 1 != 5) { printf("X\n"); continue; }

    REP(mask, 1 << M) {
      REP(i, N) REP(j, N) dist[i][j] = 1000000000;
      REP(i, N) dist[i][i] = 0;
      REP(i, M) dist[u[i]][v[i]] = min(dist[u[i]][v[i]], (mask & (1 << i)) ? a[i] : b[i]);
      REP(k, N) REP(i, N) REP(j, N) dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);

      int sum = 0;
      REP(i, P) {
        sum += (mask & (1 << id[i])) ? a[id[i]] : b[id[i]];
        if (sum + dist[v[id[i]]][1] == dist[0][1]) ok[i] = true;
      }
    }

    bool valid = true;
    REP(i, P) if (!ok[i]) { printf("%d\n", id[i] + 1); valid = false; break; }
    if(valid) printf("Looks Good To Me\n");
  }
  return 0;
}
