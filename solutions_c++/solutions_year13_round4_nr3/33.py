#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <algorithm>
#include <vector>

using namespace std;
const int kMaxn = 2010;

int a[kMaxn], b[kMaxn];
int deg[kMaxn];
int x[kMaxn];
vector<int> e[kMaxn];
int q[kMaxn];
int n;
void add_edge(int x, int y) {
  deg[y]++;
  e[x].push_back(y);
}
int main() {
  int T, cas = 0;
  for (scanf("%d", &T), cas = 1; cas <= T; cas++) {
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) scanf("%d", a + i);
    for (int i = 1; i <= n; i++) scanf("%d", b + i);
    memset(deg, 0, sizeof deg);
    for (int i = 1; i <= n; i++) e[i].clear();
    for (int i = 1; i <= n; i++) {
      int flag = 0;
      for (int j = i - 1; j > 0; j--) {
        if (a[j] >= a[i]) {
          add_edge(i, j);
        }
        if (a[j] + 1 == a[i] && !flag) {
          add_edge(j, i);
          flag = 1;
        }
      }
      flag = 0;
      for (int j = i + 1; j <= n; j++) {
        if (b[j] >= b[i]) {
          add_edge(i, j);
        }
        if (b[j] + 1 == b[i] && !flag) {
          add_edge(j, i);
          flag = 1;
        }
      }
    }
    int qn = 0;
    for (int i = 1; i <= n; i++)
      if (deg[i] == 0) q[qn++] = i;
    sort(q, q + qn);
    for (int p = 0; p < qn; p++) {
      int u = q[p];
      x[u] = p + 1;
      for (int i = 0; i < int(e[u].size()); i++) {
        int v = e[u][i];
        --deg[v];
        if (deg[v] == 0) {
          q[qn++] = v;
        }
      }
      sort(q + p + 1, q + qn);
    }
    printf("Case #%d:", cas);
    for (int i = 1; i <= n; i++) printf(" %d", x[i]);
    puts("");
  }
  return 0;
}
