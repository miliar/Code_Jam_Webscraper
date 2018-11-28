#include <cstdio>
#include <algorithm>

using namespace std;
int LEN, NEEDED;

long long toBase(long long val, int base) {
  long long conv = 0;
  long long exp = 1;
  for (int i = 0; i < 64; ++i) {
    if (val & (1LL << i)) conv += exp;
    exp *= base;
  }
  return conv;
}

long long findFactor(long long val) {
  long long ll = min(val - 1, ((long long)(sqrt(val) + 0.5)));
  for (long long i = 2; i <= ll; ++i) {
    if (val % i == 0) return i;
  }
  return -1;
}

int main() {
  int dummy;
  scanf("%d %d %d", &dummy, &LEN, &NEEDED);
  long long lo = (1LL << (LEN - 1)) + 1;
  long long hi = (1LL << LEN) - 1;
  int num = 0;
  printf("Case #1:\n");
  for (long long i = lo; i <= hi; ++i) {
    if (i % 2 == 0) continue;
    long long factors[11] = {};
    bool doable = true;
    for (int b = 2; b <= 10; ++b) {
      long long val = toBase(i, b);
      long long factor = findFactor(val);
      if (factor != -1) factors[b] = factor;
      else {doable = false; break;}
    }
    if (doable) {
      num++;
      long long dec = toBase(i, 10);
      printf("%lld ", dec);
      for (int b = 2; b <= 10; ++b) {
        printf("%lld", factors[b]);
        if (b != 10) printf(" ");
      }
      printf("\n");
      if (num == NEEDED) break;
    }
  }
}
