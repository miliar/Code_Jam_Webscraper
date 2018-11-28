#include <bits/stdc++.h>
using namespace std;

typedef long long lli;

const int INF = 1<<28;
const int MAXR = 101;
const int MAXC = 101;
const int di[] = {0,1,0,-1};
const int dj[] = {1,0,-1,0};
const lli mod = 1000000007LL;

int R, C;
vector<vector<int> > G;
lli ans = 0;
set<vector<vector<int> > > s;

bool check(int i, int j) {
  int res = 0, zero = 0;
  for(int d = 0; d < 4; ++d) {
    int ni = i + di[d];
    int nj = (j + dj[d] + C) % C;
    if(ni < 0 || ni >= R) continue;
    zero += G[ni][nj] == 0;
    res += G[ni][nj] == G[i][j];
  }
  if(zero) return res <= G[i][j] && res + zero >= G[i][j];
  else return res == G[i][j];
}

bool ok(int i, int j) {
  if(!check(i, j)) return false;
  for(int d = 0; d < 4; ++d) {
    int ni = i + di[d];
    int nj = (j + dj[d] + C) % C;
    if(ni < 0 || ni >= R) continue;
    if(G[ni][nj] == 0) continue;
    if(!check(ni, nj)) return false;
  }
  return true;
}

void add() {
  if(s.count(G)) return;
  ++ans;
  for(int k = 0; k < C; ++k) {
    for(int i = 0; i < R; ++i) {
      int tmp = G[i][0];
      for(int j = 0; j < C; ++j) {
        G[i][j] = G[i][j+1];
      }
      G[i][C-1] = tmp;
    }
    s.insert(G);
  }
}

void rec(int i, int j) {
  if(j == C) j = 0, ++i;
  if(i == R) {
    add();
    return;
  }
  for(int k = 1; k <= 4; ++k) {
    if(k == 4 && (i == 0 || i == R-1)) break;
    G[i][j] = k;
    if(ok(i, j)) {
      rec(i, j+1);
    }
  }
  G[i][j] = 0;
}

int main() {
  int T; cin >> T;
  for(int tc = 1; tc <= T; ++tc) {
    cout << "Case #" << tc << ": ";
    cin >> R >> C;
    G = vector<vector<int> >(R, vector<int>(C));
    s.clear();
    ans = 0;
    rec(0, 0);
    cout << ans << endl;
  }
  return 0;
}
