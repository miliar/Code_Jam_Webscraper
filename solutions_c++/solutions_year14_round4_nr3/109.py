#include <algorithm>
#include <iostream>
#include <sstream>
#include <cassert>
#include <cstdarg>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstdio>
#include <queue>
#include <ctime>
#include <cmath>
#include <map>
#include <set>

using namespace std;

#define all(c) (c).begin(), (c).end()
#define mp make_pair
#define pb push_back
#define sz(c) (int)(c).size()
#define eprintf(...) fprintf(stderr, __VA_ARGS__)

const int maxn = 1 << 10;
int x[maxn][2];
int y[maxn][2];
int w[maxn][maxn];
int dist[maxn], was[maxn];

void solve(int test) {
  int W, H, B;
  scanf("%d%d%d", &W, &H, &B);
  for (int i = 0; i < B; i++) {
    for (int k = 0; k < 2; k++) {
      scanf("%d%d", &x[i][k], &y[i][k]);
    }
    x[i][1]++;
    y[i][1]++;
  }
  int n = B + 2;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      w[i][j] = W + H;
    }
  }
  w[n - 2][n - 1] = W;
  w[n - 1][n - 2] = W;
  for (int i = 0; i < B; i++) {
    for (int j = 0; j < B; j++) {
      int left = max(y[i][0], y[j][0]);
      int right = min(y[i][1], y[j][1]);
      w[i][j] = H + W;
      if (left <= right) {
        w[i][j] = min(abs(x[i][0] - x[j][1]), abs(x[i][1] - x[j][0]));
      }
      left = max(x[i][0], x[j][0]);
      right = min(x[i][1], x[j][1]);
      if (left <= right) {
        w[i][j] =
            min(w[i][j], min(abs(y[i][0] - y[j][1]), abs(y[i][1] - y[j][0])));
      }
      for (int k1 = 0; k1 < 4; k1++) {
        for (int k2 = 0; k2 < 4; k2++) {
          int xx1 = x[i][k1 & 1];
          int yy1 = y[i][k1 >> 1];
          int xx2 = x[j][k2 & 1];
          int yy2 = y[j][k2 >> 1];
          w[i][j] = min(w[i][j], max(abs(xx1 - xx2), abs(yy1 - yy2)));
        }
      }
    }
    w[i][B] = x[i][0];
    w[B][i] = x[i][0];
    w[B + 1][i] = W - x[i][1];
    w[i][B + 1] = W - x[i][1];
  }
  for (int i = 0; i < n; i++) {
    was[i] = 0;
    dist[i] = W;
  }
  dist[B] = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      assert(w[i][j] == w[j][i]);
     // eprintf("%d%c", w[i][j], " \n"[j + 1 == n]);
    }
  }
  for (;;) {
    int mini = -1;
    for (int i = 0; i < n; i++) {
      if (!was[i] && (mini == -1 || dist[i] < dist[mini])) {
        mini = i;
      }
    }
    if (mini == -1) break;
    was[mini] = 1;
    for (int i = 0; i < n; i++) {
      dist[i] = min(dist[i], dist[mini] + w[mini][i]);
    }
  }
  //eprintf("dist:\n");
  //for (int i = 0; i < n; i++) eprintf("%d%c", dist[i], " \n"[i + 1 == n]);
  printf("Case #%d: %d\n", test, dist[n - 1]);
}

int main() {
  int T;
  scanf("%d", &T);
  for (int test = 1; test <= T; test++) {
    solve(test);
  }
}
