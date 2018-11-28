#include <bits/stdc++.h>
#define REP(x, n) for (int x = 0; x < (int)(n); x++)
#define RREP(x, n) for (int x = (int)(n)-1; x >= 0; --x)
#define FOR(x, m, n) for (int x = (int)m; x < (int)(n); x++)
#define EACH(itr, cont) \
  for (typeof((cont).begin()) itr = (cont).begin(); itr != (cont).end(); ++itr)
#define ALL(X) (X).begin(), (X).end()
#define mem0(X) memset((X), 0, sizeof(X))
#define mem1(X) memset((X), 255, sizeof(X))

using namespace std;
typedef long long LL;

void doStuff() {
  int K, C, S;
  scanf("%d%d%d", &K, &C, &S);
  LL value = 1;
  for (int i = 0; i < C - 1; ++i) value *= K;
  for (int i = 0; i < K; ++i) {
    printf(" %lld", (i + 1) * value);
  }
  printf("\n");
}

int main() {
  int T;
  scanf("%d", &T);
  REP(t, T) printf("Case #%d:", t + 1), doStuff();
  return 0;
}