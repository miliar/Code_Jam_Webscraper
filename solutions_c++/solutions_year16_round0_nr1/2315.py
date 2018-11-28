#ifndef INCLUDED
#include <bits/stdc++.h>
#define INCLUDED
#define F first
#define S second
#define MP make_pair
#define PB push_back

using namespace std;
typedef long long L;
typedef long double LD;
#endif
/*
 * Author: raghumdani
 * Date Created: 09/04/2016
*/

#define TESTCASE

const int N = 1234567;
const int mod = 1000000007;
L xx = 2000000000000000000LL;

int JAM16_A(int testNumber) {
  L n;
  scanf("%lld", &n);
  if(n == 0) {
    printf("Case #%d: INSOMNIA\n", testNumber);
    return(0);
  }
  int cnt[10] = {0};
  for(L i = 1; ; ++i) {
    L cur = n * i;
    if(cur >= xx) break;
    while(cur != 0) {
      cnt[cur % 10] = 1;
      cur /= 10;
    }
    bool bad = false;
    for(int j = 0; j < 10; ++j) {
      if(!cnt[j]) {
        bad = true;
        break;
      }
    }
    if(!bad) {
      printf("Case #%d: %lld\n", testNumber, i * n);
      return(0);
    }
  }
  printf("Case #%d: INSOMNIA\n", testNumber);
  return(0);
}

void allClear() {
  
}

int main() {
  int t = 1;
  #ifdef TESTCASE
    scanf("%d", &t);
  #endif
  for(int _ = 1; _ <= t; ++_) {
    int ret = JAM16_A( _ );
    allClear();
  }
  return(0);
}

