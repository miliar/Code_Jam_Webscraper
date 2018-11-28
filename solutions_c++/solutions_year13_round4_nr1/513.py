#include <iostream>
#include <vector>
#include <queue>
#include <cstring>
using namespace std;

typedef long long ll;

const ll MOD = 1000002013;
const ll INF = 1000000000000000000LL;
typedef pair<ll, int> PLI;

inline ll mod(ll x) {
  return (x < MOD) ? x : x%MOD;
}

#define NN 2005
#define pot(u,v) (pi[u]-pi[v])

int adj[NN][NN], deg[NN], padre[NN]; 
ll w[NN][NN], cap[NN][NN], pi[NN], d[NN], f[NN][NN];

int n;

ll flow, cost;

bool dijkstra(int s, int t) {
  memset(padre, -1, sizeof(padre));
  for (int i = 0; i < n; ++i) d[i] = INF;
  d[s] = 0;
  priority_queue<PLI> Q;
  Q.push(PLI(0,s));
  while (not Q.empty()) {
    int u = Q.top().second;
    ll dist = -Q.top().first;
    Q.pop();
    if (dist != d[u]) continue;
    for (int i = 0; i < deg[u]; ++i) {
      int v = adj[u][i];
      if (f[u][v] >= 0 and cap[u][v] - f[u][v] > 0 and 
      d[v] > d[u] + pot(u,v) + w[u][v]) {
        d[v] = d[u] + pot(u,v) + w[u][v];
        Q.push(PLI(-d[v], v));
        padre[v] = u;
      }
      else if (f[u][v] < 0 and d[v] > d[u] + pot(u,v) - w[v][u]) {
        d[v] = d[u] + pot(u,v) - w[v][u];
        Q.push(PLI(-d[v], v));
        padre[v] = u;
      }
    }
  }
  for (int i = 0; i < n; ++i) if (pi[i] < INF) pi[i] += d[i];
  return padre[t] >= 0;
}

void maxmin(int s, int t) {
  memset(f, 0, sizeof(f));
  memset(pi, 0, sizeof(pi));
  flow = cost = 0;
  while (dijkstra(s, t)) {
    ll bot = INF;
    for (int v = t, u = padre[v]; u != -1; v = u, u = padre[u]) {
      if (f[u][v] >= 0) bot = min(cap[u][v] - f[u][v], bot);
      else bot = min(f[v][u], bot);
    }
    for (int v = t, u = padre[v]; u != -1; v = u, u = padre[u]) {
      if (f[u][v] >= 0) cost += w[u][v]*bot;
      else cost -= w[v][u]*bot;
      f[u][v] += bot;
      f[v][u] -= bot;
    }
    flow += bot;
  }
}

inline ll valor(ll k, ll N) {
  return (k*(2*N + 1 - k))/2;
}

struct Info {
  int o, e, qtt;  
};

int main() {
  int casos;
  cin >> casos;
  for (int cas = 1; cas <= casos; ++cas) {
    int N, m;
    cin >> N >> m;
    vector<Info> v(m);
    ll suma = 0;
    for (int i = 0; i < m; ++i) {
      cin >> v[i].o >> v[i].e >> v[i].qtt;
      suma += v[i].qtt*valor(v[i].e - v[i].o, N);      
    }
    
    n = 2*m + 2;
    memset(cap, 0, sizeof(cap));
    memset(w, 0, sizeof(w));
    memset(deg, 0, sizeof(deg));
    
    
    vector<vector<int> > can(m, vector<int>(m,0));
    for (int i = 0; i < m; ++i) can[i][i] = 1;
    for (int i = 0; i < m; ++i) 
      for (int j = i + 1; j < m; ++j) 
        if (not (v[i].o > v[j].e or v[i].e < v[j].o)) can[i][j] = can[j][i] = 1;

    
    for (int k = 0; k < m; ++k) {
      for (int i = 0; i < m; ++i) {
        for (int j = 0; j < m; ++j) {
          can[i][j] |= (can[i][k] & can[k][j]);          
        }
      }
    }
    
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < m; ++j) {
        if (v[i].o > v[j].e) can[i][j] = false;        
      }
    }
    
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < m; ++j) {
        if (can[i][j]) {
          adj[i][deg[i]++] = m + j;
          adj[m + j][deg[m + j]++] = i;
          cap[i][m + j] = m + INF;
          w[i][m + j] = valor(v[j].e - v[i].o, N);
        }
      }
    }
    
    //Source
    for (int i = 0; i < m; ++i) {
      adj[2*m][deg[2*m]++] = i;
      adj[i][deg[i]++] = 2*m;
      cap[2*m][i] = v[i].qtt;
    }
    
    //Sink
    for (int i = 0; i < m; ++i) {
      adj[2*m + 1][deg[2*m + 1]++] = i + m;
      adj[i + m][deg[i + m]++] = 2*m + 1;
      cap[i + m][2*m + 1] = v[i].qtt;
    }
    
    maxmin(2*m, 2*m + 1);
    cout << "Case #" << cas << ": " << suma - cost << endl;
  }
}