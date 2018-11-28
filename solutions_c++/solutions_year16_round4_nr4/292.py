#include <bits/stdc++.h>

#define FOR(i,b,e) for(int i=(b); i <= (e); ++i)
#define FORD(i,b,e) for(int i=(b); i >= (e); --i)
#define REP(i,n) for(int i=0; i < (n); ++i)
#define SIZE(c) (int) (c).size()
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair
#define ST first
#define ND second
#define FWD(i,a,b) for (int i=(a); i<(b); ++i)
#define BCK(i,a,b) for (int i=(a); i>(b); --i)
#define PI acos(-1.0)
#define pb push_back
#define mp make_pair
#define st first
#define nd second

using namespace std;

typedef long long int LLI;
typedef pair < int , int > PII;
typedef pair < LLI , LLI > PLL;

typedef vector < int > VI;
typedef vector < bool > VB;
typedef vector < PII > VP;
typedef vector < LLI > VL;
typedef vector < PLL > VPL;

typedef vector < VI > VVI;
typedef vector < VL > VVL;
typedef vector < VB > VVB;
typedef vector < VP > VVP;

const int MAXN = 5;

int before[MAXN][MAXN];
int ed[MAXN][MAXN];

const int N = 100;
int n1,n2;          // INPUT
vector<int> g[N];   // INPUT
int m1[N], m2[N];   // OUTPUT
bool vis[N];

bool dfs(int u) {
  if (u<0) return true;
  if (vis[u]) return false; else vis[u]=true;
  for(int v : g[u])
    if (dfs(m2[v])) { m1[u] = v; m2[v] = u; return true; }
  return false;
}

int matching() {
  REP(i,n1) m1[i] = -1;
  REP(i,n2) m2[i] = -1;
  bool changed;
  do {
    changed = 0;
    REP(i,n1) vis[i] = false;
    REP(i,n1) if (m1[i] < 0) changed |= dfs(i);
  } while(changed);
  int siz = 0;
  REP(i,n1) siz += (m1[i] != -1);
  return siz;
}


bool canFuckUp(int w, int n) {
  REP(i, 2*n) g[i].clear();

  n1 = n2 = n;

  REP(wrk, n) if (wrk != w) REP(job, n) {
    if (ed[wrk][job] > 0 && ed[w][job] > 0) {
      g[wrk].pb(job);
    }
  }

  int wSiz = 0;
  REP(job, n) wSiz += ed[w][job] > 0;

  int match = matching();

  return match == wSiz;
}

int main() {
  ios_base::sync_with_stdio(false);

  int t;
  cin >> t;
  FOR(TC, 1, t) {
    cout << "Case #" << TC << ": ";

    int n;
    cin >> n;
    vector<string> in(n);
    REP(i, n) cin >> in[i];

    int res = 100;

    REP(i, n) REP(j, n) before[i][j] = in[i][j] == '1';

    REP(mask, (1 << (n * n))) {
      REP(i, n) REP(j, n) {
        ed[i][j] = before[i][j] + ((1 << (n * i + j)) & mask);
      }

      bool ok = true;
      REP(i, n) if (canFuckUp(i, n)) ok = false;
      if (ok && __builtin_popcount(mask) < res) {
        res = __builtin_popcount(mask);
      }
    }

    cout << res << endl;


  }
}
