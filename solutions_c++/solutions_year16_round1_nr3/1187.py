#include <bits/stdc++.h>

using namespace std;

#ifdef ACMTUYO
struct RTC{~RTC(){cerr << "Time: " << clock() * 1.0 / CLOCKS_PER_SEC <<" seconds\n";}} runtimecount;
#define DBG(X) cerr << #X << " = " << X << '\n';
#else
struct RTC{};
#define DBG(X)
#endif

#define fast_io() ios_base::sync_with_stdio(false)
#define mp make_pair
#define mt make_tuple
#define pb push_back
#define eb emplace_back
#define sz(x) ((int)(x).size())
#define all(c) (c).begin(),(c).end()
#define forn(i, n) for (int i = 0; i < (n); i++)
typedef long long int number;
const int maxn = 1010;
vector<int> g[maxn];
bool G[maxn][maxn];
int n;
bool vis[maxn];
int ans;
//a siempre tiene a alguien asignado 
//el metodo busca a alguien para que b mire
void solve(int a, int b, int first, int cnt) {
  if (G[b][a] || G[b][first]) {
    ans = max(ans, cnt);
  }
  forn (i, n)
    if (!vis[i]) {
      if (G[b][i] || G[b][a]) {
        vis[i] = true;
        solve(b, i, first, cnt + 1);
        vis[i] = false;
      }
    }
}
int main() {
  int t;
  scanf("%d", &t);
  for (int caso = 1; caso <= t; caso++) {
    scanf("%d", &n);
    forn (i, n)
      g[i].clear();
    memset(G, false, sizeof(G));
    forn (i, n) {
      int j;
      scanf("%d", &j);
      j--;
      G[i][j] = true;
      g[i].pb(j - 1);
    }
    ans = 1;
    memset(vis, false, sizeof(vis));
    forn (i, n) {
      vis[i] = true;
      forn (j, n)
        if (j != i && G[i][j]) {
          vis[j] = true;
          solve(i, j, i, 2);
          vis[j] = false;
        }
      vis[i] = false;
    }
    printf("Case #%d: %d\n", caso, ans);
  }
  
  return 0;
}

