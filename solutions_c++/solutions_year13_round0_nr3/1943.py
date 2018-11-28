#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

typedef long long lint;

int is_pal(lint v) {
  char k[16];
  int p = 0;
  while (v) {
    k[p++] = v%10 + '0';
    v/=10;
  }
  int a = 0, b = p-1;
  while (a < b) {
    if (k[a] != k[b]) return 0;
    a++, b--;
  }
  return 1;
}
int main() {
  vector<lint> pos;
  for (int i = 1; i <= 10000000; i++) {
    if (is_pal(i)) pos.push_back(i);
  }

  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    int ans = 0;
    lint a, b;
    scanf("%lld %lld", &a, &b);
    lint bot = 1, top = a;
    lint v = 1;
    while (bot <= top) {
      lint mid = (bot+top)/2;
      if (mid >= a/mid) v = mid;
      if (mid >= a/mid) {
	top = mid-1;
      } else bot = mid+1;
    }
    if (v*v < a) v++;
    assert(v*v >= a);
    while (v*v <= b) {
      if (is_pal(v) && is_pal(v*v)) {
	ans++;
      }
      v += 1;
    }

    printf("Case #%d: %d\n", t, ans);
  }
}
