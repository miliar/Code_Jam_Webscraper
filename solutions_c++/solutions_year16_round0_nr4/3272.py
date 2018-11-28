#include <cstdio>
#include <cstring>
#include <cstdint>
#include <algorithm>
using namespace std;

uint64_t x;
bool mark[30];

int K, C, S;

int main() {
  int T;
  scanf("%d", &T);
  for (int I = 1; I <= T; ++I) {
    scanf("%d%d%d", &K, &C, &S);
    printf("Case #%d:", I);
    for (int i = 1; i <=S; ++i) {
      printf(" %d", i);
    }
    printf("\n");
  }
}
