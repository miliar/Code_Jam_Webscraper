#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair<int, int> PII;
const int MAXN = 1000 + 10;
PII pd[MAXN];
int N, B;

LL count(LL t, int id) {
  LL ret = 0;
  for (int i = 0; i < B; ++ i) {
    if (t % pd[i].first != 0) ret += t / pd[i].first + 1;
    else {
      if (pd[i].second <= id) ret += t / pd[i].first + 1;
      else ret += t / pd[i].first;
    }
  }
  return ret;
}

int main() {
  int T; scanf("%d", &T);
  for (int cas = 1; cas <= T; ++ cas) {
    scanf("%d%d", &B, &N);
    for (int i = 0; i < B; ++ i) {
      scanf("%d", &pd[i].first);
      pd[i].second = i + 1;
    }
    sort(pd, pd + B);
    int ret = -1; LL time;
    for (int i = 0; i < B; ++ i) {
      int left = 0, right = N;
      while (left < right) {
        int mid = (left + right - 1) >> 1;
        LL num = count((LL)mid * pd[i].first, pd[i].second);
        if (num >= N) right = mid;
        else left = mid + 1;
      }
      LL tmp = (LL)left * pd[i].first;
      if (ret == -1 || tmp < time || (tmp == time && pd[i].second < ret)) {
        ret = pd[i].second, time = tmp;
      }
    }
    printf("Case #%d: %d\n", cas, ret);
  }
  return 0;
}
