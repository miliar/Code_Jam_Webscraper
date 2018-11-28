#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < int(b); ++i)
#define trav(a, v) for(auto& a : v)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
#define D(x) cerr << #x << " = " << x << endl

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vpi;

template<typename T, typename U> static inline void smin(T &x, U y) {if(y < x) x = y; }
template<typename T, typename U> static inline void smax(T &x, U y){ if(y > x) x = y; }
template<typename T> istream& operator>>(istream& in, vector<T> &v) { rep(i,0,v.size()) in >> v[i]; return in; }
template<typename A, typename B> istream& operator>>(istream& in, pair<A, B> &p) { in >> p.first >> p.second; return in; }
template<typename T> ostream& operator<<(ostream& out, vector<T> &v) { if(v.size()) out << v[0]; rep(i,1,v.size()) out << ' ' << v[i]; return out; }
template<typename A, typename B> ostream& operator<<(ostream& out, pair<A, B> &p){ out << p.first << ' ' << p.second; return out; }


vector<int> match;
vector<bool> seen;
template<class G>
bool find(int j, G &g) {
  if (match[j] == -1) return 1;
  seen[j] = 1; int di = match[j];
  trav(e, g[di])
    if (!seen[e] && find(e, g)) {
      match[e] = di;
      match[j] = -1;
      return 1;
    }
  return 0;
}
template<class G>
int dfs_matching(G &g, int n, int m) {
  match.assign(m, -1);
  rep(i,0,n) {
    seen.assign(m, false);
    trav(j,g[i])
      if (find(j, g)) {
        match[j] = i;
        break;
      }
  }
  return m - count(all(match), -1);
}

bool ok(int N, const vector<string>& G) {
  rep(i,0,N) {
    vector<vector<int>> graph(N);
    int has = 0;
    rep(j,0,N) {
      if (G[i][j] == '1') {
        has++;
      }
      rep(k,0,N) {
        if (j != i && G[j][k] == '1' && G[i][k] == '1') {
          graph[j].push_back(k); 
        }
      }
    }
    if (dfs_matching(graph, N, N) == has) {
      return false;
    }
  }
  return true;
}

bool solve(int tc){
  int N;
  cin >> N;
  vector<string> G(N);
  cin >> G;
  int ans = N * N;
  rep(i,0,1<<(N*N)) {
    vector<string> G2 = G;
    rep(j,0,N) {
      rep(k,0,N) {
        if (i & 1 << (j * N + k)) G2[j][k] = '1';
      }
    }
    if (ok(N, G2)) {
      smin(ans, __builtin_popcount(i));
    }
  }
  cout << "Case #" << tc << ": " << ans << endl;
  return true;
}

int main() {
  cin.sync_with_stdio(false); cin.tie(NULL);
  int n = 1<<30;
  cin >> n;
  for(int i = 1; i <= n && solve(i); ++i);
}
