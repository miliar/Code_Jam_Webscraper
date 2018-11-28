#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <complex>
#include <ctime>
#include <cassert>
#include <functional>

using namespace std;

typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define REP(i,s,t) for(int i=(s);i<(t);i++)
#define FILL(x,v) memset(x,v,sizeof(x))

const int INF = (int)1E9;
#define MAXN 100005

int R, C, N;
int g[20][20];
bool v[20][20][2];
set<int> CC;
void initG() {
  FILL(g, -1);
  REP(j,1,C+1) g[0][j] = j;
  int B = C;
  REP(i,1,R+1) g[i][C+1] = B + i;
  B = C+R;
  for(int j=C;j>=1;j--) g[R+1][j] = B + (C-j+1);
  B = 2*C+R;
  for(int i=R;i>=1;i--) g[i][0] = B + (R-i+1);
}
void dfs(int x, int y, int t) {
  v[x][y][t] = 1;
  if (x == 0 || x == R+1 || y == 0 || y == C+1) CC.insert(g[x][y]);
  if (x == 0) {
    if (!v[x+1][y][0]) dfs(x+1,y,0);
  }
  if (x == R+1) {
    if (!v[x-1][y][1]) dfs(x-1,y,1);
  }
  if (y == 0) {
    int lt = g[x][y+1] == 0 ? 0 : 1;
    if (!v[x][y+1][lt]) dfs(x,y+1,lt);
  }
  if (y == C+1) {
    int lt = g[x][y-1] == 0 ? 1 : 0;
    if (!v[x][y-1][lt]) dfs(x,y-1,lt);
  }
  if (x == 0 || x == R+1 || y == 0 || y == C+1) return;

  if (t == 0) {
    if (g[x][y] == 0) {
      if (!v[x-1][y][1]) dfs(x-1, y, 1);
      int lt = g[x][y-1] == 0 ? 1 : 0;
      if (!v[x][y-1][lt]) dfs(x,y-1,lt);
    } else if (g[x][y] == 1) {
      if (!v[x-1][y][1]) dfs(x-1, y, 1);
      int lt = g[x][y+1] == 0 || y+1 == C+1? 0 : 1;
      if (!v[x][y+1][lt]) dfs(x,y+1,lt);
    }
  } else if (t==1){
    if (g[x][y] == 0) {
      if (!v[x+1][y][0]) dfs(x+1, y, 0);
      int lt = g[x][y+1] == 0 || y+1 == C+1? 0 : 1;
      if (!v[x][y+1][lt]) dfs(x,y+1,lt);
    } else if (g[x][y] == 1) {
      if (!v[x+1][y][0]) dfs(x+1, y, 0);
      int lt = g[x][y-1] == 0 ? 1 : 0;
      if (!v[x][y-1][lt]) dfs(x,y-1,lt);
    }
  }
}
set<PII> expect;
bool hasPair() {
  int a = *CC.begin(), b = *CC.rbegin();
  //cerr << "(" << a << "," << b << ")" << endl;
  if (a>b) swap(a,b);
  return expect.find(PII(a,b)) != expect.end();
}
int main() {
  freopen("input", "r", stdin);
  //freopen("output", "w", stdout);
  int cs;
  cin >> cs;
  REP(csn, 1, cs + 1) {
    printf("Case #%d:\n", csn);
    //cerr << csn << endl;
    cin >> R >> C;
    N = 2 * (R+C);
    expect.clear();
    REP(i,0,N/2) {
      int a, b;
      cin >> a >> b;
      if (a>b) swap(a,b);
      expect.insert(PII(a,b));
    }

    bool ok = 0;
    REP(m,0,1<<(R*C)) {
      initG();
      REP(i,1,R+1) {
        REP(j,1,C+1) {
          g[i][j] = (m & (1<<((i-1)*C+(j-1)))) > 0;
        }
      }

      /*
      REP(i,0,R+2) {
        REP(j,0,C+2) {
          fprintf(stderr, "%d ", g[i][j]);
        }
        cerr << endl;
      }
      cerr << endl;
       */

      bool fail = 0;
      FILL(v,0);
      REP(j,1,C+1) {
        if (!v[0][j][1]) {
          CC.clear();
          dfs(0,j,1);
          if (CC.size() != 2 || !hasPair()) {
            fail = 1;
            break;
          }
        }
        if (!v[R+1][j][0]) {
          CC.clear(); dfs(R+1,j,0);
          if (CC.size() != 2 || !hasPair()) {
            fail = 1;
            break;
          }
        }
      }
      if (fail) continue;
      REP(i,1,R+1) {
        if (!v[i][0][0]) {
          CC.clear(); dfs(i,0,0);
          if (CC.size() != 2 || !hasPair()) {
            fail = 1;
            break;
          }
        }
        if (!v[i][C+1][0]) {
          CC.clear(); dfs(i,C+1,0);
          if (CC.size() != 2 || !hasPair()) {
            fail = 1;
            break;
          }
        }
      }
      if (!fail) {
        ok = 1;
        break;
      }
    }
    if (!ok) puts("IMPOSSIBLE");
    else {
      REP(i,1,R+1) {
        REP(j,1,C+1) {
          if (g[i][j] == 0) printf("/");
          else printf("\\");
        }
        puts("");
      }
    }

  }
  return 0;
}
