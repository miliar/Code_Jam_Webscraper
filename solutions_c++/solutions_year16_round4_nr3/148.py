#include <iostream>
#include <vector>
using namespace std;
int R, C, love[60];
int vis[60], g=1;
vector<int> v[60];
int horizontal(int x, int y) { return C*x + y; }
int vertical(int x, int y) { return (R+1)*C + (C+1)*x + y; }
void join(int a, int b) { v[a].push_back(b); v[b].push_back(a); /* cout << "join(" << a << ", " << b << ")\n"; */}
int conv(int a) {
  int x;
  if (a < C) x = horizontal(0, a);
  else if (a-C < R) x = vertical(a-C, C);
  else if (a-C-R < C) x = horizontal(R, C-1-(a-C-R));
  else x = vertical(R-1-(a-2*C-R), 0);
  return x;
}
void dfs(int a) {
  vis[a] = g;
  for (int b: v[a]) 
    if (!vis[b]) dfs(b);
}
int main() {
  ios_base::sync_with_stdio(0);
  int T, a, b;
  cin >> T;
  for (int t=1; t<=T; t++) {
    cout << "Case #" << t << ": ";
    for (int i=0; i<60; i++) love[i];
    cin >> R >> C;
    for (int i=0; i<R+C; i++) {
      cin >> a >> b;
      a--; b--;
      int x = conv(a), y = conv(b);
      love[x] = y;
      love[y] = x;
    }
    bool s[17][17], fail = true;
    for (int i=0; i<(1<<(R*C)); i++) {
      for (int j=0; j<60; j++) vis[j] = 0, v[j].clear();
      g = 1;
      for (int j=0; j<R*C; j++) {
        int x = j/C, y = j%C;
        s[x][y] = (i>>j)&1;
        if (s[x][y]) {
          join(horizontal(x, y), vertical(x, y+1));
          join(horizontal(x+1, y), vertical(x, y));
        } else {
          join(horizontal(x, y), vertical(x, y));
          join(horizontal(x+1, y), vertical(x, y+1));
        }
      }
       /*  cout << "\n";
        for (int x=0; x<R; x++) {
          for (int y=0; y<C; y++)
            if (s[x][y]) cout << "\\"; else cout << "/";
          cout << "\n";
        } cout << "\n"; */

      for (int a=0; a<(R+1)*C + R*(C+1); a++)
        if (!vis[a]) { dfs(a); g++; }
      int used[g];
      fail = false;
      for (int i=0; i<=g; i++) used[i] = 0;
      for (int a=0; a<2*(R+C) && !fail; a++) {
        // cout << "vis[" << conv(a) << "] = " << vis[conv(a)] << "\n";
        // cout << "vis[" << love[conv(a)] << "] = " << vis[love[conv(a)]] << "\n";
        int x = vis[conv(a)];
        if (used[x] > 1 || vis[love[conv(a)]] != x) fail = true;
        used[x]++;
      }
      if (!fail) {
        cout << "\n";
        for (int x=0; x<R; x++) {
          for (int y=0; y<C; y++)
            if (s[x][y]) cout << "\\"; else cout << "/";
          cout << "\n";
        }
        break;
      }
    }
    if (fail) cout << "\nIMPOSSIBLE\n";
  }
  return 0;
}
