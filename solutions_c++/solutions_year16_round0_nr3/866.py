#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <numeric>
#include <utility>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

long long getDiv(long long n) {
  if (n <= 1) return 1;
  if (n < 4) return 1;
  if ((n & 1) == 0) return 2;
  for (long long i = 3; i * i <= n; i += 2) {
    if (n % i == 0) return i;
  }
  return 1;
}

int digits[60];
long long divs[11];

void setDigits(int n, long long x, int *digits) {
  digits[0] = digits[n] = 1;
  for (int i = 1; i < n; ++i) {
    digits[i] = x & 1;
    x /= 2;
  }
}

long long getNumber(int base, int n, int *digits) {
  long long t = 1;
  long long ret = 0;
  for (int i = 0; i <= n; ++i) {
    ret += digits[i] * t;
    t *= base;
  }
  return ret;
}

bool setDivs(int n, long long x) {
  setDigits(n, x, digits); 
  for (int base = 2; base <= 10; ++base) {
    long long m = getNumber(base, n, digits);
    divs[base] = getDiv(m);
    if (divs[base] == 1) return false;
  }
  return true;
}

void printResult(int n) {
  for (; n >= 0; --n) {
    printf("%d", digits[n]);
  }
  for (int base = 2; base <= 10; ++base) {
    printf(" %lld", divs[base]);
  }
  printf("\n");
}

void solve() {
  int n, j;
  scanf("%d%d", &n, &j);
  --n;
  printf("\n");
  long long m = 0;
  while (j--) {
    while (!setDivs(n, m)) ++m;
    printResult(n);
    ++m;
  }
}

int main() {
  int t;
  scanf("%d", &t);
  for (int tc = 1; tc <= t; ++tc) {
    printf("Case #%d: ", tc);
    solve();
  }
  return 0;
}
