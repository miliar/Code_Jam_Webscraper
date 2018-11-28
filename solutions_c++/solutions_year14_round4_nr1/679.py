#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;

int T, n, x, cnt[1005];

int main() {
  scanf("%d", &T);
  for (int it = 1; it <= T; it++) {
    scanf("%d %d", &n, &x);
    memset(cnt,0,sizeof(cnt));
    for (int i = 0; i < n; i++) {
      int c;
      scanf("%d", &c);
      cnt[c]++;
    }
    int ret = 0;
    for (int d2 = x; d2 > 0; d2--) while (cnt[d2]) {
      ret++;
      cnt[d2]--;
      for (int d1 = min(x - d2, d2); d1 > 0; d1--) if (cnt[d1]) {
        cnt[d1]--;
	break;
      }
    }
    printf("Case #%d: %d\n", it, ret);
  }
}
