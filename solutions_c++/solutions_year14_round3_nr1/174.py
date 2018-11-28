#include <cstdio>

using namespace std;

long long gcd(long long a, long long b) {
  while (true) {
    if (a == 0) return b;
    b %= a;
    if (b == 0) return a;
    a %= b;
  }

  return 0;
}

int main() {
  int nCase;
  scanf("%d", &nCase);

  for (int iCase = 0; iCase < nCase; ++iCase) {
    long long p, q;
    
    scanf("%lld/%lld", &p, &q);

    long long g = gcd(p, q);
    p /= g;
    q /= g;

    bool possible = true;
    int gens = 0;
    long long tq = q;
    while (tq > 1) {
      if (tq % 2 != 0) {
        possible = false;
        break;
      }
      else {
        ++gens;
        tq /= 2;
      }
    }

    printf("Case #%d: ", iCase + 1);

    if (!possible || gens > 40) {
      printf("impossible\n");
    }
    else {
      int sol = 0;
      while (p < q) {
        ++sol;
        p *= 2;
      }

      printf("%d\n", sol);
    }
  }
}
