#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstring>
#include <map>

using namespace std;

#define MAXN (1 << 20)

long long D;
long long S[MAXN];
long long M[MAXN];
vector<int> E[MAXN];

int V[2 * MAXN];
int L[2 * MAXN];

void add(int x, int a, int b, int A, int B, int v) {
  if (b <= A || B <= a) {
    return;
  }
  if (a <= A && B <= b) {
    L[x] += v;
    V[x] += v;
    return;
  }
  V[2 * x + 0] += L[x];
  L[2 * x + 0] += L[x];
  V[2 * x + 1] += L[x];
  L[2 * x + 1] += L[x];
  L[x] = 0;

  int M = (A + B) / 2;
  add(2 * x + 0, a, b, A, M, v);
  add(2 * x + 1, a, b, M, B, v);
  V[x] = max(V[2 * x + 0], V[2 * x + 1]);
}

void dfs(int u, long long lo, long long hi) {
  lo = min(lo, S[u]);
  hi = max(hi, S[u]);

  int rlo = max(0ll, hi - D);
  int rhi = lo;
  if (rhi < rlo) {
    return;
  }
//cout << " add " << rlo << ", " << rhi << endl;
  add(1, rlo, rhi + 1, 0, MAXN, 1);
  for (int i = 0; i < E[u].size(); i++) {
    dfs(E[u][i], lo, hi);
  }
}

int main() {
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    cout << "Case #" << t << ": ";

    int N;
    cin >> N >> D;
    long long As, Cs, Rs;
    long long Am, Cm, Rm;
    cin >> S[0] >> As >> Cs >> Rs;
    cin >> M[0] >> Am >> Cm >> Rm;

    for (int i = 0; i < N; i++) {
      E[i].clear();
    }
    for (int i = 1; i < N; i++) {
      S[i] = (S[i - 1] * As + Cs) % Rs;
      M[i] = (M[i - 1] * Am + Cm) % Rm;
      E[M[i] % i].push_back(i);
    }

    memset(V, 0, sizeof(V));
    memset(L, 0, sizeof(L));
    dfs(0, S[0], S[0]);
    cout << V[1] << endl;
  }
  return 0;
}
