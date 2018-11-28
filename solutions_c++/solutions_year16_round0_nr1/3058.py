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

long T, N;

uint32_t CalcMask(long N) {
  bool t[10] = {};
  while( N != 0 ) {
    t[N % 10] = true;
    N /= 10;
  }
  uint32_t res = 0;
  for(int i = 0; i < 10; ++i) {
    if( t[i] ) {
      res |= (1 << i);
    }
  }
  return res;
}

int main() {
  scanf("%ld", &T);
  for(long i = 0; i < T; ++i) {
    scanf("%ld", &N);
    if( N == 0 ) {
      printf("Case #%ld: INSOMNIA\n", i + 1);
      continue;
    }
    uint32_t mask = 0;
    for(long j = 1; j < 10000; ++j) {
      mask |= CalcMask(j * N);
      if( mask == 0x3ff ) {
        printf("Case #%ld: %ld\n", i + 1, j * N);
        break;
      }
    }    
  }
  
  return 0;
}
