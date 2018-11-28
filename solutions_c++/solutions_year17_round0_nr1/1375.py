/* Written by Filip Hlasek 2017 */
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <iostream>

#define FOR(i, a, b)   for (int i = (a); i <= (b); i++)
#define FORD(i, a, b)  for (int i = (a); i >= (b); i--)
#define REP(i, b)      for (int i =  0 ; i <  (b); i++)

using namespace std;

#define MAXN 1111
int K, N;
char input[MAXN];

int main(int argc, char *argv[]) {
  int T;
  scanf("%d", &T);
  FOR(t, 1, T) {
    scanf("%s", input);
    N = strlen(input);
    scanf("%d", &K);
    int ans = 0;
    FORD(i, N - 1, 0) {
      if (input[i] == '-') {
        if (i < K - 1) { ans = -1; break; }
        ans++;
        REP(j, K) input[i - j] = (input[i - j] == '+' ? '-' : '+');
      }
    }
    printf("Case #%d: ", t);
    if (ans == -1) printf("IMPOSSIBLE\n");
    else printf("%d\n", ans);
  }
  return 0;
}
