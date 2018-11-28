#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long llint;

const int MAX = 1111;
const int inf = 1e9;

int sum[MAX];
int L[MAX], R[MAX];

int main(void) {
  int TC;
  scanf("%d", &TC);
  for (int tp = 1; tp <= TC; ++tp, fflush(stdout)) {
    int N, K;
    scanf("%d %d", &N, &K);
    REP(i, N-K+1) scanf("%d", sum+i);

    REP(i, K) {
      L[i] = R[i] = 0;
      int d = 0;
      for (int x = i; x + 1 + K <= N; x += K) {
        d += sum[x + 1] - sum[x];
        L[i] = min(L[i], d);
        R[i] = max(R[i], d);
      }
    }
    
    auto check = [&] (int lo, int hi) {
      int slo = 0, shi = 0;
      REP(i, K) {
        if (lo-L[i] > hi-R[i]) return false;
        slo += lo - L[i];
        shi += hi - R[i];
      }
      return slo <= sum[0] && sum[0] <= shi;
    };
    
    int M = (N/K)*10000*10;
    int lo = M, ans = inf;
    for (int hi = M; hi >= -M; --hi) {
      while (lo > -M && !check(lo, hi)) lo--;
      if (check(lo, hi)) ans = min(ans, hi - lo);
    }
    

    printf("Case #%d: ", tp);
    printf("%d\n", ans);
  }
  return 0;
}
