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
  LL N;
  scanf("%lld", &N);
  set<LL> S;
  for (LL i = 1; i < 1e+6; ++i) {
    LL aux = N * i;
    while (aux) S.insert(aux % 10), aux /= 10;
    if (S.size() == 10) {
      printf("%lld\n", i * N);
      return;
    }
  }
  printf("INSOMNIA\n");
}

int main() {
  int T;
  scanf("%d", &T);
  REP(t, T) printf("Case #%d: ", t + 1), doStuff();
  return 0;
}