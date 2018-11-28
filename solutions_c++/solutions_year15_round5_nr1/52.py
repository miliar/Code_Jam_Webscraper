#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <vector>

using namespace std;

#define FOR(prom, a, b) for(int prom = (a); prom < (b); prom++)
#define FORD(prom, a, b) for(int prom = (a); prom > (b); prom--)
#define FORDE(prom, a, b) for(int prom = (a); prom >= (b); prom--)

#define DRI(a) int a; scanf("%d ", &a);
#define DRII(a, b) int a, b; scanf("%d %d ", &a, &b);
#define DRIII(a, b, c) int a, b, c; scanf("%d %d %d ", &a, &b, &c);
#define DRIIII(a, b, c, d) int a, b, c, d; scanf("%d %d %d %d ", &a, &b, &c, &d);
#define RI(a) scanf("%d ", &a);
#define RII(a, b) scanf("%d %d ", &a, &b);
#define RIII(a, b, c) scanf("%d %d %d ", &a, &b, &c);
#define RIIII(a, b, c, d) scanf("%d %d %d %d ", &a, &b, &c, &d);

#define PB push_back
#define MP make_pair

#define ll long long
#define ull unsigned long long

#define MM(co, cim) memset((co), (cim), sizeof((co)))

#define DEB(x) cerr << ">>> " << #x << " : " << x << endl;

int S[1000007];
int M[1000007];
int dyn[1000007];
int N,D;
int MN[1000007];
int MX[1000007];

vector<int> g[1000007];

void DFS(int v, int mn, int mx) {
  mn = min(mn,S[v]);
  mx = max(mx,S[v]);
  if(mx-mn > D) return;
  dyn[max(0,mx-D)]++;
  dyn[mn+1]--;
  FOR(i,0,g[v].size()) {
    DFS(g[v][i],mn,mx);
  }
}

int main ()
{
  DRI(T);
  FOR(t,0,T) {
    RII(N,D);
    FOR(i,0,N) g[i].clear();
    MM(dyn,0);
    DRIIII(S0, As, Cs, Rs);
    DRIIII(M0, Am, Cm, Rm);
    S[0] = S0;
    M[0] = M0;
    FOR(i,1,N) {
      S[i] = (S[i-1]*As+Cs) % Rs;
      M[i] = (M[i-1]*Am+Cm) % Rm;
    }
    FOR(i,1,N) M[i] %= i;
    FOR(i,1,N) {
      g[M[i]].PB(i);
    }
    //DFS(0,S[0],S[0]);
    queue<int> q;
    MN[0] = S[0];
    MX[0] = S[0];
    q.push(0);
    while(!q.empty()) {
      int v = q.front();
      q.pop();
      MN[v] = min(MN[v],S[v]);
      MX[v] = max(MX[v],S[v]);
      if(MX[v]-MN[v] > D) continue;
      dyn[max(0,MX[v]-D)]++;
      dyn[MN[v]+1]--;
      FOR(i,0,g[v].size()) {
        int u = g[v][i];
        q.push(u);
        MN[u] = MN[v];
        MX[u] = MX[v];
      }
    }
    int best = 0;
    int cnt = 0;
    FOR(i,0,1000007) {
      cnt += dyn[i];
      best = max(best,cnt);
    }
    printf("Case #%d: %d\n", t+1, best);
  }
  return 0;
}
