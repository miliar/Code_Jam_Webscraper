#include <cstdio>
#include <cmath>
#include <cstring>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <map>

int T;

int main() {
  scanf("%d", &T);
  for(int i = 1; i <= T; ++i) {
    int K, C, S;
    scanf("%d %d %d", &K, &C, &S);
    long w[128];
    for(int j = 0; j < K; ++j) {
      w[j] = j;
    }
    for(int j = 1; j < C; ++j) {
      for(int k = 0; k < K; ++k) {
        w[k] = w[k] * K + k;
      }
    }
    printf("Case #%d:", i);
    for(int j = 0; j < K; ++j) {
      printf(" %ld", w[j] + 1);
    }
    printf("\n");
  }
  
  return 0;
}
