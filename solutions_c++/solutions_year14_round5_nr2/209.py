#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;

int f[105][3005][205];
int P, Q, N, T;
int H[105], G[105];
int dp(int now, int p, int h) {
  if (now == N) return 0;
  int& ret = f[now][p][h];
  if (ret == -1) {
    ret = 0;
    if (h <= Q) {
      ret = max(ret, dp(now + 1, p + 1, H[now + 1]));
      int t = p + 1;
      t -= ((h - 1) / P + 1);
      if (t >= 1) {
        ret = max(ret, dp(now + 1, t - 1, H[now + 1]) + G[now]);
      } else if (t == 0) {
        if (now + 1 < N && H[now + 1] <= Q) {
          ret = max(ret, dp(now + 2, 0, H[now + 2]) + G[now]);
        } else {
          ret = max(ret, dp(now + 1, 0, H[now + 1] - Q) + G[now]);
        }
      }
    } else {
      ret = max(ret, dp(now, p + 1, h - Q));
    }
  }
  return ret;
}

int main() {
  freopen("B-large.in", "r", stdin);
  freopen("B.out", "w", stdout);
  scanf("%d", &T);
  for (int test = 1; test <= T; ++test) {
    memset(f, -1, sizeof(f));
    scanf("%d%d%d", &P, &Q, &N);
    for (int i = 0; i < N; ++i) {
      scanf("%d%d", &H[i], &G[i]);
    }
    printf("Case #%d: %d\n", test, dp(0, 0, H[0]));
  }
  return 0;
}

