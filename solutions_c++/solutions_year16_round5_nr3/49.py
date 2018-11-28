#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

const int MAXN = 1111;

int T;
int N, S;

int X[MAXN], Y[MAXN], Z[MAXN];
int VX[MAXN], VY[MAXN], VZ[MAXN];
double D[MAXN][MAXN];

typedef pair<int, int> pii;
typedef pair<double, pii> pdii;

int par[MAXN];
int find(int x) {
  if (par[x] == x) return x;
  return par[x] = find(par[x]);
}

void join(int a, int b) {
  a = find(a);
  b = find(b);
  par[a] = b;
}

int main() {
  scanf("%d", &T);
  for(int t = 1; t <= T; ++t) {
    scanf("%d %d", &N, &S);
    for(int i = 0; i < N; ++i) {
      scanf("%d %d %d", X + i, Y + i, Z + i);
      scanf("%d %d %d", VX + i, VY + i, VZ + i);
    }

    vector<pdii> v;
    for(int i = 0; i < N; ++i) {
      for(int j = 0; j < N; ++j) {
        int dx = X[i] - X[j], dy = Y[i] - Y[j], dz = Z[i] - Z[j];
        D[i][j] = sqrt(dx * dx + dy * dy + dz * dz);
        v.push_back(pdii(D[i][j], pii(i, j)));
      }
    }
    sort(v.begin(), v.end());

    for(int i = 0; i < N; ++i) {
      par[i] = i;
    }

    double ans = 0;
    for(int i = 0; i < v.size(); ++i) {
      if (find(0) == find(1)) break;
      ans = v[i].first;
      join(v[i].second.first, v[i].second.second);
    }

    printf("Case #%d: %.6lf\n", t, ans);
  }
}
