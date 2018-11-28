#include <stdio.h>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>
#include <map>
#include <tuple>
#include <string>
#include <iostream>

using namespace std;

int marcar_digitos(vector<bool> * digitos, long long n) {
  int k = 0;
  do {
    int digito = n%10;
    if((*digitos)[digito] == false) {
      k++;
      (*digitos)[digito] = true;
    }
    n /= 10;
  } while(n != 0);
  return k;
}

int main() {
  /*for (int i = 1; i < 2000000; i++) {
    vector<bool> digitos(10, false);
    int found = 0;
    int iterations = 0;
    int n = i;
    while(found < 10) {
    found += marcar_digitos(&digitos, n);
    n += i;
    iterations++;
    }
    ans[i] = n - i;
    }*/
  int n;
  scanf(" %d ", &n);
  for (int i = 0; i < n; i++) {
    vector<bool> digitos(10, false);
    long long m;
    scanf(" %lld ", &m);
    if(m == 0) {
      printf("Case #%d: INSOMNIA\n", i+1);
      continue;
    }
    long long k = m;
    int found = 0;
    while(found < 10) {
      found += marcar_digitos(&digitos, k);
      k += m;
    }
    printf("Case #%d: %lld\n", i+1, k - m);
  }
}
