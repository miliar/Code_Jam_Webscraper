#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

int R, C, W;
int cache[21][21][1 << 21];

int max(int a, int b) {
  if (a > 1000000000) return b;
  if (b > 1000000000) return a;
  return std::max(a, b);
}

int dp(int st, int en, int taken) {
  if (en - st == W) return 0;
  if (taken == ((1 << C) - 1)) return 1000000000;
  if (cache[st][en][taken] != -1) return cache[st][en][taken];

  int best = 1000000000;
  for (int i = 0; i < C; ++i) {
    if (taken & (1 << i)) continue;
  
    int subbest = dp(st, en, taken | (1 << i)) + 1;
    if (en - st == 0) {
      subbest = max(dp(i, i + 1, taken | (1 << i)) + 1, subbest);
    } else if (i == st - 1) {
      subbest = max(dp(st - 1, en, taken | (1 << i)) + 1, subbest);
    } else if (i == en) {
      subbest = max(dp(st, en + 1, taken | (1 << i)) + 1, subbest);
    }

    best = min(best, subbest);
  }
  return cache[st][en][taken] = best;
}


int main() {
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    scanf("%d %d %d", &R, &C, &W);
    memset(cache, -1, sizeof(cache));

    int rowAns = dp(0, 0, 0);

    printf("Case #%d: %d\n", t, R * rowAns - (R - 1) * (W - 1));
  }
}
