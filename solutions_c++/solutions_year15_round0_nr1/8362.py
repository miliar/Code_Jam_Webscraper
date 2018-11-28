#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

typedef long long llint;

char s[12345];
int solve() {
  int n; scanf("%d", &n);
  scanf("%s", s);
  int cnt = 0;
  int ret = 0;
  for (int i = 0; i <= n; ++i) {
    if (cnt < i) { ret += i - cnt; cnt = i; }
    cnt += s[i] - '0';
  }
  return ret;
}

int main(void) {
  int T; scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    printf("Case #%d: %d\n", t, solve());
  }
  return 0;
}

