#include <cmath>
#include <cstring>
#include <iostream>
#include <map>

using namespace std;

#define MAXN 65536

map<long long, long long> divs;
int s[33];

long long getDiv(long long N) {
  // if (divs.find(N) == divs.end()) {
    for (long long i = 2; i <= sqrt(N); i++)
      if (N % i == 0) {
        return i;
        // divs[N] = i;
        // break;
      }
    return -1;
    // if (divs.find(N) == divs.end())
    //   divs[N] = -1;
  // }
  // return divs[N];
}

long long inBase(long long V, int b) {
  long long res = 0;
  long long m = 1;
  while (V) {
    res = res + (V % 2) * m;
    V /= 2;
    m *= b;
  }
  return res;
}

int main() {
  for (int i = 32768; i < 65536; i++) {
    if (i % 2 == 0)
      continue;
    bool found = true;
    long long res[10];
    for (int j = 2; j <= 10; j++) {
      res[j] = getDiv(inBase(i, j));
      if (res[j] == -1) {
        found = false;
        break;
      }
    }
    if (found) {
      int n = i;
      int t = 0;
      while (n) {
        s[t++] = n % 2;
        n /= 2;
      }
      while (--t >= 0)
        printf("%d", s[t]);
      for (int j = 2; j <= 10; j++)
        printf(" %lld", res[j]);
      printf("\n");
    }
  }
  return 0;
}
