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

#define MAXN 2222
int N;
int A[MAXN], B[MAXN], X[MAXN];

bool solve(int i) {
  if(i == N+1) return true;
  REP(j, N) if(X[j] == -1) {
    int l = 1, r = 1;
    REP(k, N) if(X[k] != -1 && X[k] != i) {
      if (k < j) l = max(l, 1 + A[k]);
      else       r = max(r, 1 + B[k]);
    }
    if(l == A[j] && r == B[j]) {
      X[j] = i;
      if(solve(i+1)) return true;
      X[j] = -1;
    }
  }
  return false;
}

int main(int argc, char *argv[]){
  int T;
  scanf("%d", &T);
  FOR(t, 1, T) {
    printf("Case #%d:", t);
    scanf("%d", &N);
    REP(i, N) scanf("%d", A + i);
    REP(i, N) scanf("%d", B + i);
    REP(i, N) X[i] = -1;
    solve(1);
    REP(i, N) printf(" %d", X[i]); printf("\n");
  }
  return 0;
}
