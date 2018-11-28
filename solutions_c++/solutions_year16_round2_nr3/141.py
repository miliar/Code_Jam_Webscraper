#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

vector<int> g[2005];
int cap[2005][2005], t, n;
bool vis[2005]; int p[2005];

map<string, int> m1, m2;

bool bfs() {
  queue<int> q;
  for (int i = 0; i < 2005; ++i)
    p[i] = -1, vis[i] = 0;
  q.push(0); vis[0] = true;

  while (!q.empty()) {
    int t = q.front(); q.pop();
    for (int u : g[t]) {
      if (cap[t][u] == 0 || vis[u])
	continue;
      p[u] = t;
      vis[u] = true;
      q.push(u);
    }
  }
  
  if (!vis[2*n+1])
    return false;
  int x = 2*n+1;
  while (x != 0) {
    cap[p[x]][x]--; cap[x][p[x]]++;
    x = p[x];
  }
  return true;
}

int maxflow() {
  int ans = 0;
  while (bfs() == true)
    ans++;
  return ans;
}

int main() {
  ifstream cin("input.in");
  cin >> t;
  
  for (int i = 0; i < t; ++i) {
    m1.clear(), m2.clear();
    for (int i = 0; i < 2005; ++i)
      g[i].clear();
    memset(cap, 0, sizeof(cap));
    memset(vis, 0, sizeof(vis));
    
    for (int i = 0; i < 2005; ++i)
      p[i] = -1;
    cin >> n;
    for (int j = 0; j < n; ++j) {
      string a, b; cin >> a >> b;
      if (m1.count(a) == 0)
	m1[a] = m1.size();
      if (m2.count(b) == 0)
	  m2[b] = m2.size();
      
      int u = m1[a], v = m2[b]+n;
      g[u].push_back(v);
      g[v].push_back(u);
      cap[u][v] = 1;
    }

    for (int i = 1; i <= m1.size(); ++i) {
      g[0].push_back(i);
      g[i].push_back(0);
      cap[0][i] = 1;
    } for (int i = 1; i <= m2.size(); ++i) {
      g[i+n].push_back(2*n+1);
      g[2*n+1].push_back(i+n);
      cap[i+n][2*n+1] = 1;
    }
    
    cout << "Case #" << i+1 << ": " << n-(m1.size() + m2.size() - maxflow()) << "\n";
  }
}
