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

int J, N;
string gettwo(LL x) {
  string S(N, '1');
  for (int i = 0; i < N; ++i) {
    if (x % 2 == 0) S[N - i - 1] = '0';
    x /= 2;
  }
  return S;
}

LL getDiv(LL x, LL d) {
  LL value = 0, aux = 1, div = 2, temp = x;
  while (x) {
    value += (x % 2) * aux, x /= 2;
    aux *= d;
  }
  // fprintf(stderr, "%s in %lld: %lld\n", gettwo(temp).c_str(), d, value);
  while (div * div <= value) {
    if (value % div == 0) return div;
    ++div;
  }
  // fprintf(stderr, "%lld not good in %lld, because %lld is prime\n", temp, d,
  //         value);
  return -1;
}

void doStuff() {
  int cnt = 0;
  scanf("%d%d", &N, &J);
  LL start = 1 << (N - 1);
  LL num = start;
  while (cnt < J) {
    if (num % 2 == 0 || ((num & start) == 0)) {
      ++num;
      continue;
    }
    LL divisors[10];
    for (int d = 0; d < 9; ++d) {
      LL temp = getDiv(num, d + 2);
      if (temp < 0) {
        divisors[0] = -1;
        break;
      } else
        divisors[d] = temp;
    }
    if (divisors[0] > 1) {
      printf("%s", gettwo(num).c_str());
      for (int d = 0; d < 9; ++d) printf(" %lld", divisors[d]);
      printf("\n");
      ++cnt;
    }
    ++num;
  }
}

int main() {
  int T;
  scanf("%d", &T);
  REP(t, T) printf("Case #%d:\n", t + 1), doStuff();
  return 0;
}