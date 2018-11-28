/* Written by Filip Hlasek 2014 */
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

#define MAXN 111111
int X, S[MAXN], N;

int main(int argc, char *argv[]) {
  int T;
  scanf("%d", &T);
  REP(t, T) {
    scanf("%d%d", &N, &X);
    REP(i, N) scanf("%d", S + i);
    sort(S, S + N);
    int ans = 0, left = 0, right = N - 1;
    while (left <= right) {
      ans++;
      if (left < right && S[left] + S[right] <= X) left++;
      right--;
    }
    printf("Case #%d: %d\n", t + 1, ans);
  }
  return 0;
}
