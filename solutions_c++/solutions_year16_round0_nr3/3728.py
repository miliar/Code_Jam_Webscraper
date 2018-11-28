#include <cstdio>
#include <cmath>
#include <cstdint>
#include <vector>
#include <algorithm>

using namespace std;

void p(int n, int w) {
  putchar('1');
  for (int i=0; i<w-2; ++i) putchar(((1<<i)&n) ? '1' : '0');
  putchar('1');
}

void p2(int n, int w) { p(n, w); p(n, w); }

uint64_t p64(uint64_t x, int p) {
  uint64_t r = 1;
  for (int i=0; i<p; ++i) r *= x;
  return r;
}

void f(int w, int k) {
  printf("Case #1:\n");
  for (int i=0; i<k; ++i) {
    p2(i, w);
    for (uint64_t j=2; j<=10; ++j) printf(" %llu", p64(j, w) + 1);
    printf("\n");
  }
}

int main() {
  int n, k;
  scanf("%d", &n); // 1
  scanf("%d %d", &n, &k);
  f(n/2, k);
}
