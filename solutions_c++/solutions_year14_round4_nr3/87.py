#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 1010;
const int inf = 1 << 29;

int T;
int W, H, B;

int adj[MAXN][MAXN];
int X0[MAXN];
int Y0[MAXN];
int X1[MAXN];
int Y1[MAXN];

int getdist(int a, int b) {
  if (a == 0 && b == B) {
    return W;
  }
  if (a == 0) {
    return X0[b];
  } else if (b == B) {
    return W - 1 - X1[a];
  } else {
    int dx = max(X0[a] - X1[b] - 1, X0[b] - X1[a] - 1);
    int dy = max(Y0[a] - Y1[b] - 1, Y0[b] - Y1[a] - 1);
    int d = max(dx, dy);
    return d;
  }
}

int dist[MAXN];
bool vis[MAXN];

int dijk() {
  for(int i = 0; i <= B; ++i) {
    dist[i] = inf;
    vis[i] = false;
  }
  dist[0] = 0;
  for(int rep = 0; rep <= B; ++rep) {
    int bst = -1;
    for(int i = 0; i <= B; ++i) {
      if (vis[i]) continue;
      if (bst == -1 || dist[i] < dist[bst]) {
        bst = i;
      }
    }
    vis[bst] = true;
    for(int i = 0; i <= B; ++i) {
      if (vis[i]) continue;
      int ndist = dist[bst] + adj[bst][i];
      if (ndist < dist[i]) {
        dist[i] = ndist;
      }
    }
  }

  return dist[B];
}

int main() {
  scanf("%d", &T);
  for(int t = 1; t <= T; ++t) {
    scanf("%d %d %d", &W, &H, &B);
    for(int i = 1; i <= B; ++i) {
      scanf("%d %d %d %d", X0 + i, Y0 + i, X1 + i, Y1 + i);
    }
    ++B;

    for(int i = 0; i <= B; ++i) {
      for(int j = i + 1; j <= B; ++j) {
        adj[i][j] = adj[j][i] = getdist(i, j);
  //      printf("adj[%d][%d] = %d\n", i, j, adj[i][j]);
      }
    }

    int ans = dijk();
    printf("Case #%d: %d\n", t, ans);
  }

}
