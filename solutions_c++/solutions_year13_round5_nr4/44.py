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

long double dp[1 << 20];

int main(int argc, char *argv[]){
  int T; 
  scanf("%d", &T);
  REP(t, T) {
    printf("Case #%d: ", t + 1);
    char start[25];
    scanf("%s", start);
    int N = strlen(start);
    REP(i, 1 << N) if(i) {
      dp[i] = 0;
      REP(j, N) REP(k, N) if (i & (1 << ((j + k) % N))) {
        dp[i] += (N - k) + dp[i ^ (1 << ((j + k) % N))];
        break;
      }
      dp[i] /= N;
    }
    int mask = 0;
    REP(i, N) if(start[i] == '.') mask |= 1 << i;
    printf("%.15Lf\n", dp[mask]);
  }
  return 0;
}
