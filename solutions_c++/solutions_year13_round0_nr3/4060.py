#include <cstdio>
#include <cassert>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

typedef unsigned long long ll;

#define MAX 10000040LL

vector<ll> nfairsquares(MAX);

bool isfair(ll x) {
  static char num[100];
  sprintf(&num[0], "%llu", x);
  size_t l = strlen(num);

  for (size_t i = 0; i < l/2; ++i)
    if (num[i] != num[l-i-1])
      return false;

  return true;
}

int isfairsquare(ll x) {
  if (isfair(x) && isfair(x*x)) {
//    fprintf(stderr, "%llu^2 = %llu is fair square\n", x, x*x);
    return 1;
  }
  return 0;
}

void generate() {
  nfairsquares[0] = 0;
  for (ll i = 1; i < nfairsquares.size(); ++i)
    nfairsquares[i] = nfairsquares[i-1] + isfairsquare(i);
}

int solve() {
  ll A, B;
  ll aq, bq;

  scanf("%llu %llu", &A, &B);
  aq = sqrt(A);
  bq = sqrt(B);
  if (aq*aq < A) aq++;

  return nfairsquares[bq] - nfairsquares[aq-1];
}

int main() {
  int T;
  scanf("%d\n", &T);

  generate();

  for (int i = 0; i < T; ++i)
    printf("Case #%d: %d\n", i+1, solve());
  return 0;
}
