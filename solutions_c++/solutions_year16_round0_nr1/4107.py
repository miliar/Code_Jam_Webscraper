#include <cstdio>
#include <cstring>
#include <cstdint>
#include <algorithm>
using namespace std;

uint64_t x;
bool mark[30];

int main() {
  int T;
  scanf("%d", &T);
  for (int I = 1; I <= T; ++I) {
    scanf("%llu", &x);
    if (x == 0) {
      printf("Case #%d: INSOMNIA\n", I);
      continue;
    }
    int left = 10;
    fill(mark, mark + 10, false);
    uint64_t i = 1;
    for (; ; ++i) {
      for (uint64_t tmp = x * i; tmp; tmp /= 10) {
        int t = tmp % 10;
        if (mark[t] == 0) {
          --left;
          mark[t] = 1;
        }
      }
      if (left == 0) break;
    }
    printf("Case #%d: %llu\n", I, i * x);
  }
}
