//
//  main.cpp
//  bsuir2016
//
//  Created by Artjom Bastun on 3/28/16.
//  Copyright © 2016 Artjom Bastun. All rights reserved.
//

#include <iostream>
#include <string.h>
#include <algorithm>

using namespace std;

bool number[33];
int n, j;

//long long binpow(int a, int n) {
//  long long res = 1;
//  while (n)
//    if (n & 1) {
//      res *= a;
//      --n;
//    }
//    else {
//      a *= a;
//      n >>= 1;
//    }
//  return res;
//}

long long buildNumber(int base) {
  long long x = 0;
  int mult = 1;
  for (int i = 0; i < n / 2; ++i) {
    x += number[i] * mult;
    mult *= base;
  }
  return x;
}

void nextNumber() {
  int i = 1;
  while (number[i] == 1) {
    number[i++] = 0;
  }
  number[i] = 1;
}

void printNumber() {
  for (int i = n/2 - 1; i >= 0; --i) {
    cout << number[i];
  }
  for (int i = n/2 - 1; i >= 0; --i) {
    cout << number[i];
  }
}

int main(int argc, const char * argv[]) {
  freopen("/Users/stunba/Projects/bsuir2016/bsuir2016/input.txt", "r", stdin);
  freopen("/Users/stunba/Projects/bsuir2016/bsuir2016/output.txt", "w", stdout);
  
  int t;
  cin >> t;
  
//  long long pn = UINT32_MAX;
//  prime = new bool[pn + 1];
//  for (long long i = 0; i <= pn; i++) {
//    prime[i] = true;
//  }
//  prime[0] = prime[1] = false;
//  for (long long i=2; i*i <= pn; ++i) {
//    if (prime[i]) {
//      if (i * 1ll * i <= pn) {
//        for (long long j=i*i; j<=pn; j+=i) {
//          prime[j] = false;
//        }
//      }
//    }
//  }
  
  for (int i = 1; i <= t; ++i) {
    cin >> n >> j;
    cout << "Case #" << i << ": " << endl;
    for (int l = 0; l < n; ++l) {
      number[l] = 0;
    }
    number[0] = 1;
    number[n/2 - 1] = 1;
    for (int count = 0; count < j; count++) {
      printNumber();
      cout << " ";
      for (int base = 2; base <= 10; base++) {
        cout << buildNumber(base) << " ";
      }
      cout << endl;
      nextNumber();
    }
  }
  
  return 0;
}
