#include <bits/stdc++.h>
#include <unordered_map>

using namespace std;

typedef long long LL;

#define mset(a, v) memset(a, v, sizeof(a));
#define mset0(a) mset(a, 0);

void read() { }
template<typename... T> void read(int &h, T &... t) {
  scanf("%d", &h); read(t...);
}
template<typename... T> void read(LL &h, T &... t) {
  scanf("%lld", &h); read(t...);
}
template<typename... T> void read(double &h, T &... t) {
  scanf("%lf", &h); read(t...);
}

const int maxint = 0x7f7f7f7f;
const double eps = 1e-10, pi = acos(-1.0);

const int maxN = 8888;

unordered_map<string, int> mp;
int n, tests, curID;
vector<int> words[maxN], has[maxN];
char buf[1111 * 11];

int s, t, ec, d[maxN], vd[maxN];
struct edge_link {
  int v, r;
  edge_link *next, *pair;
} edge[11111111], *header[maxN], *current[maxN];

void add(int u, int v, int r) {
  edge[++ec].v = v, edge[ec].r = r, edge[ec].next = header[u], header[u] = &edge[ec], edge[ec].pair = &edge[ec + 1];
  edge[++ec].v = u, edge[ec].r = 0, edge[ec].next = header[v], header[v] = &edge[ec], edge[ec].pair = &edge[ec - 1];
}

int augment(int u, int flow) {
  if (u == t) return flow;
  int temp, res = 0;
  for (edge_link *&e = current[u]; e != NULL; e = e->next) {
    if (e->r && d[u] == d[e->v] + 1) {
      temp = augment(e->v, min(e->r, flow - res));
      e->r -= temp, e->pair->r += temp, res += temp;
      if (d[s] == t || res == flow) return res;
    }
  }
  if (--vd[d[u]] == 0) d[s] = t;
  else current[u] = header[u], ++vd[++d[u]];
  return res;
}

int sap() {
  int flow = 0;
  memset(d, 0, sizeof(d)), memset(vd, 0, sizeof(vd));
  vd[0] = t;
  for (int i = 1; i <= t; ++i) current[i] = header[i];
  while (d[s] < t) flow += augment(s, maxint);
  return flow;
}

vector<int> readL() {
  gets(buf);
  stringstream ss(buf);
  string s;
  vector<int> v;
  while (ss >> s) {
    if (mp.find(s) == mp.end()) {
      mp[s] = ++curID;
    }
    v.push_back(mp[s]);
  }
  sort(v.begin(), v.end());
  v.erase(unique(v.begin(), v.end()), v.end());
  return v;
}

int main() {
  freopen("C-large.in", "r", stdin);
  freopen("C-large233.out", "w", stdout);
  read(tests);
  for (int tt = 1; tt <= tests; ++tt) { 
    curID = 0;
    mp.clear();
    read(n);
    gets(buf);
    for (int i = 0; i < maxN; ++i) has[i].clear();
    for (int i = 1; i <= n; ++i) {
      sort(words[i].begin(), words[i].end());
      words[i] = readL();
      for (int w : words[i]) has[w].push_back(i);
    }
    for (int i = 1; i <= curID; ++i) {
      sort(has[i].begin(), has[i].end());
      has[i].erase(unique(has[i].begin(), has[i].end()), has[i].end());
    }
    ec = 0;
    mset0(header);
    for (int i = 1; i <= curID; ++i) {
      for (int j = 0; j < has[i].size(); ++j) {
        for (int k = 0; k < has[i].size(); ++k) {
          if (j == k) continue;
          add(has[i][j], i + n, maxint);
          add(i + n + curID, has[i][k], maxint); 
        }
      }
    }
    for (int i = 1; i <= curID; ++i) {
      add(i + n, i + n + curID, 1);
    }
    s = curID + curID + n + 1;
    t = s + 1;
    add(s, 1, maxint);
    add(2, t, maxint);
    printf("Case #%d: %d\n", tt, sap());
  }
  return 0;
}
