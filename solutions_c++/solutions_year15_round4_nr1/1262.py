#include <bits/stdc++.h>
#include <cassert>
using namespace std;
using ll=long long; using ld=long double;
#define rep(i,s,e) for (int i=(s),__ee=(e);i<__ee;++i)
#define all(x) begin(x),end(x)
#define clr(x,y) memset(x,y,sizeof x)
#define contains(x,y) ((x).find(y)!=end(x))
#define pb push_back
#define mk make_pair
#define mkt make_tuple
#define fst first
#define snd second
#define sz(x) ((int)(x).size())
int dx[]={0,0,1,-1,1,-1,1,-1}, dy[]={-1,1,0,0,1,-1,-1,1};
void run();
int main() {
#ifdef LOCAL
#  define dbg(s, ...) printf(s "\n", __VA_ARGS__)
#else
#  define endl "\n"
#  define dbg(s,...)
#  define FILE "x"
  //freopen(FILE ".in", "r", stdin), freopen(FILE ".out", "w", stdout);
  ios::sync_with_stdio(0);
#endif
  cout << fixed << setprecision(16);
  run();
}

int T, R, C;
char grid[101][101];
set<char> possible[101][101];
void run() {
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    cin >> R >> C;
    for (int i = 0; i < R; ++i)
      for (int j = 0; j < C; ++j) {
        cin >> grid[i][j];
        possible[i][j].insert('<');
        possible[i][j].insert('>');
        possible[i][j].insert('^');
        possible[i][j].insert('v');
      }
    for (int i = 0; i < R; ++i) {
      set<int> pos;
      for (int j = 0; j < C; ++j)
        if (grid[i][j] != '.')
          pos.insert(j);
      if (pos.empty()) continue;
      int a = *begin(pos);
      int b = *prev(end(pos));
      possible[i][a].erase('<');
      possible[i][b].erase('>');
    }
    for (int j = 0; j < C; ++j) {
      set<int> pos;
      for (int i = 0; i < R; ++i)
        if (grid[i][j] != '.')
          pos.insert(i);
      if (pos.empty()) continue;
      int a = *begin(pos);
      int b = *prev(end(pos));
      possible[a][j].erase('^');
      possible[b][j].erase('v');
    }
    bool impossible = 0;
    int ans = 0;
    for (int i = 0; i < R; ++i)
      for (int j = 0; j < C; ++j) {
        if (grid[i][j] == '.') continue;
        if(possible[i][j].empty())
          impossible = 1;
        if (possible[i][j].count(grid[i][j]) == 0)
          ans++;
      }
    if (impossible)
      cout << "IMPOSSIBLE" << endl;
    else
      cout << ans << endl;
  }
}
