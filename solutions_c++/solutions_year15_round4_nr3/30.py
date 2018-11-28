/**
 * Author: Sergey Kopeliovich (Burunduk30@gmail.com)
 */

#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define fill(a, x) memset(a, x, sizeof(a))

typedef long long ll;

const int N = 200;

int n;
set<int> t[N];
map<ll, int> m;
int cc;

int getHash( const string &s ) {
  ll x = 0;
  for (int i = 0; i < (int)s.size(); i++)
    x = x * 239 + s[i];
  if (!m.count(x))
    return m[x] = cc++;
  return m[x];
}

template <const int maxV, const int _maxE>
struct Graph {
  static const int maxE = 2 * _maxE;
  int s, t, e, head[maxV], next[maxE], to[maxE], f[maxE], c[maxE];
  int cc, u[maxV];

  void init() {
    e = 0, cc = 1;
    fill(u, 0), fill(head, -1);
  }

  int add( int a, int b, int x1, int x2 = 0 ) {
    //printf("%d %d %d %d\n", a, b, x1, x2);
    assert(e + 2 <= maxE && a < maxV && b < maxV);
    next[e] = head[a], to[e] = b, f[e] = 0, c[e] = x1, head[a] = e++;
    next[e] = head[b], to[e] = a, f[e] = 0, c[e] = x2, head[b] = e++;
    return e - 2;
  }

  int gval;
  int dfs( int v, int val ) {
    if (v == t) {
      gval = val;
      return 1;
    }
    u[v] = cc;
    for (int e = head[v]; e != -1; e = next[e])
      if (f[e] < c[e] && u[to[e]] != cc && dfs(to[e], min(val, c[e] - f[e]))) {
        f[e] += gval, f[e ^ 1] -= gval;
        return 1;
      }
    return 0;
  }

  int getFlow() {
    int sum = 0;
    for (cc++; dfs(s, INT_MAX); cc++)
      sum += gval;
    return sum;
  }
};

const int INF = 1e9;
const int E = 1e6;
Graph<E, E> g;

void solve() {
  static char s[999999];
  scanf("%d ", &n);

  cc = 0, m.clear();
  forn(i, n) {
    gets(s);
 	stringstream ss(s);
 	string x;
 	t[i].clear();
 	while (ss >> x)
 	  t[i].insert(getHash(x));
  }

  vector<int> erase;
  for (int x : t[0])
    if (t[1].count(x)) {
      //printf("erase %d\n", x);
      erase.push_back(x);
    }
  for (int x : erase)
    forn(i, n)
      if (t[i].count(x)){
        //printf("%d: erase %d\n", i, x);
        t[i].erase(x);
      }

  int A = t[0].size(), B = t[1].size();
  //printf("A = %d, B = %d\n", A, B);
  g.init();
  g.s = 2 * cc, g.t = g.s + 1;
  for (int i : t[0]) g.add(g.s, 2 * i, 1, 0);
  for (int i : t[1]) g.add(2 * i + 1, g.t, 1, 0);
  for (int i = 2; i < n; i++)
    for (int x : t[i])
      for (int y : t[i])
        if (x != y)
          g.add(2 * x + 1, 2 * y, INF, 0);
  forn(x, cc)
    g.add(2 * x, 2 * x + 1, (t[0].count(cc) || t[1].count(cc)) ? INF : 1, 0);

  printf("%d\n", erase.size() + g.getFlow());
}

int main() {
  int tn;
  scanf("%d", &tn);
  forn(t, tn) {
    printf("Case #%d: ", t + 1);
    fprintf(stderr, "Case #%d:\n", t + 1);
    solve();
  }
  return 0;
}
