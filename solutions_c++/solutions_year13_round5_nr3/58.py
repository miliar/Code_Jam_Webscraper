#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

const int kMaxn = 1010;
const int kMaxm = 4010;
const int kInf = 1500000000;

int debug;
int head[kMaxm], aim[kMaxm], nxt[kMaxm], ln;
int best[kMaxm], worse[kMaxm];
int path[kMaxm], from[kMaxn], from_e[kMaxn];
int eflag[kMaxm];
int pt[kMaxn];
int n, m, pn;
void add_edge(int x, int y, int a, int b) {
  aim[ln] = y;
  nxt[ln] = head[x];
  best[ln] = a;
  worse[ln] = b;
  head[x] = ln++;
}
int f[kMaxn];
int tf[kMaxn];
int ban[kMaxn];
set<pair<int, int> > heap;
int Find(int *dis, int sp, int tp) {
  if (ban[sp]) return kInf;
  heap.clear();
  memset(f, -1, sizeof f);
  f[sp] = 0;
  heap.insert(make_pair(f[sp], sp));
  while (!heap.empty()) {
    set<pair<int, int> >::iterator it = heap.begin();
    int p = it->second;
    heap.erase(it);
    for (int i = head[p]; i != -1; i = nxt[i]) {
      if (eflag[i] == 2) continue;
      int value = (eflag[i] ? best[i] : dis[i]);
      value += f[p];
      int v = aim[i];
      if (ban[v]) continue;
      if (f[v] == -1 || value < f[v]) {
        if (f[v] != -1) heap.erase(heap.find(make_pair(f[v], v)));
        f[v] = value;
        from[v] = p;
        from_e[v] = i;
        heap.insert(make_pair(f[v], v));
      }
    }
  }
  if (f[tp] > -1) return f[tp];
  return kInf;
}
int main() {
  debug = 0;
  int tn, cp;
  for (scanf("%d", &tn), cp = 1; cp <= tn; cp++) {
    scanf("%d%d%d", &n, &m, &pn);
    memset(head, -1, sizeof head);
    ln = 0;
    for (int i = 0; i < m; i++) {
      int u, v, a, b;
      scanf("%d%d%d%d", &u, &v, &a, &b);
      add_edge(u, v, a, b);
    }
    for (int t = 0; t < pn; t++) {
      scanf("%d", pt + t);
      pt[t]--;
    }
    memset(eflag, 0, sizeof eflag);
    int flag = -1;
    for (int i = 0; i < pn; i++) {
      memset(ban, 0, sizeof ban);
      int e = pt[i];
      int len = Find(best, aim[e], 2);
      if (len >= kInf) {
        flag = i;
        break;
      }
      int ans = 0;
      for (int j = 0; j <= i; j++) ans += best[pt[j]];
      for (int j = 1; j <= n; j++) tf[j] = f[j] + ans;
      eflag[pt[i]] = 2;
      if (i == 1) debug = 1;
      int tmp = Find(worse, 1, 2);
      memset(ban, 0, sizeof ban);
      for (int j = 1; j <= n; j++)
        if (f[j] > -1 && f[j] < tf[j]) ban[j] = 1;
//      if (i == 0) {
//        for (int j = 1; j <= n; j++) printf("%d ", tf[j]);puts("");
//        for (int j = 1; j <= n; j++) printf("%d ", f[j]);puts("");
//        for (int j = 1; j <= n; j++) printf("%d ", ban[j]);puts("");
//      }
      int rr = Find(best, aim[e], 2);
//      if (i == 0) printf("%d\n", rr);
      if (Find(best, aim[e], 2) >= kInf) {
        flag = i;
        break;
      }
      eflag[pt[i]] = 1;
    }
    printf("Case #%d: ", cp);
    if (flag == -1) puts("Looks Good To Me"); else printf("%d\n", pt[flag] + 1);
  }
  return 0;
}
