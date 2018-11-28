#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;

int xa[1005], xb[1005], ya[1005], yb[1005];

long long calc(int a, int b, int c, int d) {
  if (b <= c) return c - b;
  if (d <= a) return a - d;
  return 0;
}

long long calc(int a, int b) {
  return max(calc(xa[a], xb[a], xa[b], xb[b]), calc(ya[a], yb[a], ya[b], yb[b]));
}

int T;
int W, H, B;
long long d[1005][1005];
bool V[1005];
long long D[1005];

int main() {
  freopen("C-large.in", "r", stdin);
  freopen("C.out", "w", stdout);
  scanf("%d", &T);
  for (int test = 1; test <= T; ++test) {
    memset(V, 0, sizeof(V));
    scanf("%d%d%d", &W, &H, &B);
    for (int i = 0; i < B; ++i) {
      scanf("%d%d%d%d", &xa[i], &ya[i], &xb[i], &yb[i]);
    }
    for (int i = 0; i < B; ++i) {
      for (int j = 0; j < B; ++j) {
        d[i][j] = max(0ll, calc(i, j) - 1);
      }
      d[B][i] = d[i][B] = xa[i];
      d[B + 1][i] = d[i][B + 1] = W - 1 - xb[i];
    }
    d[B][B + 1] = d[B + 1][B] = W; 
    int S = B;
    int T = B + 1; 
    int N = B + 1;
    memset(V, 0, sizeof(V));
    V[S] = 1;
    for (int i = 0; i <= N; ++i) {
      D[i] = d[S][i];
    }
    for (int i = 0; i <= N; ++i) {
      int w = 0;
      long long tmp = 100000000000000ll;
      for (int j = 0; j <= N; ++j) {
        if (V[j] == 0 && D[j] < tmp) {
          tmp = D[j];
          w = j;
        }
      }
      V[w] = 1;
      for (int j = 0; j <= N; ++j) {
        if (V[j] == 0) {
          D[j] = min(D[j], D[w] + d[w][j]);
        }
      }
    }
    printf("Case #%d: %I64d\n", test, D[T]);
  }
  return 0;
}

