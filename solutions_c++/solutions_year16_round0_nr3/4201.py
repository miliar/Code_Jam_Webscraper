#include <cstdio>
#include <cstdlib>

typedef long long ll;

const ll MAX_P = 100*1000*1000;

short divi[MAX_P + 1];
int wit[11];
int primes[102000000];
int nbPrimes = 0;

void initErat() {
  divi[1] = 0;
  for (ll x = 2; x <= MAX_P; x++) {
    if (x % ((int)(MAX_P / 200)) == 0) {
      fprintf(stderr, "Erat %lld\n", x);
      fflush(stderr);
    }
    if (!divi[x]) {
      primes[nbPrimes++] = x;
      for (ll y = x * x; y <= MAX_P; y += x)
        divi[y] = x;
    }
  }
}

void printBin(int N, int n) {
  while (N--)
    putchar('0' + !!(n & (1 << N)));
}

int getDiv(ll x) {
 if (x <= MAX_P)
   return divi[x];

  for(int i = 0;i<nbPrimes;i++) {
    const ll p = primes[i];
    if (p * p > x)
      return 0;
    if (x % p == 0)
      return p;
  }
  fprintf(stderr, "Not enough prime numbers for %lld\n", x);
  exit(1);
}

ll interp(ll n, int b) {

  // printf("interp(");
  // printBin(6, n);

  if (b == 2) {
    // printf(", 2) = %d, div -> %d\n", n, divi[n]);
    return n;
  }

  // printf(", %d) = ", b);

  ll res = 0;
  ll B = 1;
  while (n) {
    res += B * (n & 1);
    n >>= 1;
    B *= b;
  }

  // printf("%lld, div -> %d\n", res, divi[res]);

  // if (res > MAX_P) {
  //   fprintf(stderr, "Too big: %lld\n", res);
  //   exit(1);
  // }

  return res;
}

bool isJC(ll n) {
  for (int b = 2; b <= 10; b++)
    if (!(wit[b] = getDiv(interp(n, b))))
      return false;

  return true;
}

int main() {

  initErat();

  int T;
  scanf("%d", &T);

  for (int t = 1; t <= T; t++) {
    printf("Case #%d:\n", t);

    int N, J;
    scanf("%d%d", &N, &J);
    ll bN = 1 << (N-1);

    for (int n0 = 1; J > 0; n0+=2) {

      const ll n = bN + n0;
      if (isJC(n)) {
        J--;
        printBin(N, n);
        putchar(' ');
        for (int b = 2; b <= 10; b++)
          printf("%d ", wit[b]);
        putchar('\n');
        fflush(stdout);
      }
    }
         
  }
  return 0;
}
