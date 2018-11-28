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

bool isprime[100000000];
std::vector<long> primes;

void init() {
  for(int i = 0; i < 100000000; ++i) {
    isprime[i] = true;
  }
  isprime[0] = isprime[1] = false;
  for(int i = 2; i < 10000; ++i) {
    if( isprime[i] ) {
      for(int j = i * i; j < 100000000; j+=i) {
        isprime[j] = false;
      }
    }
  }
  for(int i = 0; i < 100000000; ++i) {
    if( not isprime[i] ) continue;
    primes.push_back(i);
  }
}

long check(long n) {
  long limit = sqrt(n) + 10;
  for(int i = 0; i < (int)primes.size(); ++i) {
    if( limit <= primes[i] ) break;
    if( n % primes[i] == 0 ) {
      return primes[i];
    }
  }
  return -1;
}

long convert(int B, std::string str) {
  long res = 0;
  for(int i = 0; i < (int)str.size(); ++i) {
    res *= B;
    res += (str[i] - '0');
  }
  return res;
}

int main() {
  init();

  printf("Case #1:\n");
  std::string str = "1000000000000001";
  long ans[11];
  int count = 0;
  long bitter = 0;
  for(;;) {
    for(int i = 0; i < 14; ++i) {
      if( (bitter & (1 << i)) == 0 ) {
        str[i+1] = '0';
      }
      else {
        str[i+1] = '1';
      }
    }
    bitter += 1;
    if( bitter >= 0x3fff ) break;
    bool flag = true;
    for(int j = 2; j <= 10; ++j) {
      long t = convert(j, str);
      long s = check(t);
      ans[j] = s;
      if( s < 0 ) {
        flag = false;
        break;
      }
    }
    if( flag == true ) {
      std::cout << str;
      for(int j = 2; j <= 10; ++j) {
        std::cout << ' ' << ans[j];
      }
      std::cout << std::endl;
      count += 1;
      if( count >= 50 ) break;
    }
  }
  
  return 0;
}
