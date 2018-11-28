#include <bits/stdc++.h>

using namespace std;

int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  puts("Case #1:");
  int cnt = 0;
  for (int mask = 0; mask < (1 << 16); ++mask) {
    if ((mask & 1) == 0 || ((mask >> 15) & 1) == 0) {
      continue;
    }
    vector <long long> w;
    for (int base = 2; base <= 10; ++base) {
      long long pot = 1, v = 0;
      for (int i = 0; i < 16; ++i) {
        if (((mask >> i) & 1) == 1) {
          v += pot;
        }
        pot *= base;
      }
      long long d = -1;
      for (long long i = 2; i * i <= v; ++i) {
        if (v % i == 0) {
          d = i;
          break;
        }
      }
      if (d == -1) {
        break;
      }
      w.push_back(d);
    }
    if (w.size() != 9) {
      continue;
    }
    for (int i = 15; i >= 0; --i) {
      putchar('0' + ((mask >> i) & 1));
    }
    for (int i = 0; i < 9; ++i) {
      printf(" %lld", w[i]);
    }
    printf("\n");
    ++cnt;
    if (cnt == 50) {
      break;
    }
  }
  return 0;
}