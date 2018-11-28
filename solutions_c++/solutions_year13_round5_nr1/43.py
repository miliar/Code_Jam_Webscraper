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

#define MAXN 55
long long B, X[MAXN];
int N;

long long sum(long long middle, int n) {
  long long ans = 0;
  REP(i, N) {
    if(i < n) ans += max(0LL, middle - X[i]);
    else      ans += max(0LL, middle + 1 - X[i]);
  }
  return ans;
}

long double solve(int n) {
  long long left = 0, right = 1000000000000000LL;
  while(left < right) {
    long long middle = (left + right + 1) / 2;
    if(sum(middle, n) > B) right = middle - 1;
    else left = middle;
  }

  long long spent = 0;
  REP(i, n) spent += max(0LL, left - X[i]);
  return (long double)36/n * spent - sum(left, n);
}

int main(int argc, char *argv[]){
  int T;
  scanf("%d", &T);
  REP(t, T) {
    printf("Case #%d: ", t + 1);
    scanf("%lld%d", &B, &N);

    REP(i, N) scanf("%lld", X + i);
    while(N < 37) X[N++] = 0;
    sort(X, X + N);

    long double best = 0;
    FOR(n, 1, N-1) best = max(best, solve(n));
    printf("%.10Lf\n", best);
  }
   
  return 0;
}
