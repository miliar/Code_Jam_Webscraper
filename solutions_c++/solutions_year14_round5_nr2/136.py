#include <cstdio>
#include <cstring>

const int MAXN = 110;
const int MAXH = 2111;

int DP[MAXN][MAXH]; // DP[cur monster][shots banked]
int H[MAXN];
int G[MAXN];

int T, N, P, Q;

int ceil(int a, int b) {
  return (a + b - 1) / b;
}

int getdp(int cur, int s) {
  int &ret = DP[cur][s];
  if (cur >= N) return 0;
  if (ret) return ret - 1;

  int h = H[cur];
  int ns = -1;
  for(int i = 1; i <= 10; ++i) {
    for(int j = 0; j <= 10; ++j) {
      int hurt = i * P + j * Q;
      if (hurt >= h && hurt - P < h) {
        int next = s + j - i;
        if (next > ns) ns = next;
      }
    }
  }

  if (ns >= 0) {
    int choice1 = getdp(cur + 1, ns) + G[cur];
    if (choice1 > ret) ret = choice1;
  }
  int k = ceil(h, Q);
  int choice2 = getdp(cur + 1, s + k);
  if (choice2 > ret) ret = choice2;
  return ret++;
}

int main() {
  scanf("%d", &T);
  for(int t = 1; t <= T; ++t) {
    scanf("%d %d %d", &P, &Q, &N);
//    if (t == 4) printf("%d %d %d\n", P, Q, N);
    for(int i = 0; i < N; ++i) {
      scanf("%d %d", H + i, G + i);
//      if (t == 4) printf("%d %d\n", H[i], G[i]);
    }
    memset(DP, 0, sizeof(DP));
    int ans = getdp(0, 1);
    printf("Case #%d: %d\n", t, ans);
  }

  return 0;
}
