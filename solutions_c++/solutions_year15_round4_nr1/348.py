#include <iostream>
#include <string>
#include <vector>
using namespace std;

/*
bool check(vector<string> &bd)
{

}

int rec(int x, int y, vector<string> &bd)
{
  int h = bd.size(), w = bd[0].size();

  if (y == h) {
    if (check(bd)) return 0;
    return 99999;
  }

  if (x == w) {
    return rec(0, y+1, bd);
  }

  if (bd[y][x] == '.') {
    return rec(x+1, y, bd);
  }

  static const char dir[]="^>v<";
  for (int i=0;i<4;i++){
    if (bd[y][x]==dir[i]) continue;
    char bkup = bd[y][x];
    bd[y][x] = dir[i];

  }
}
*/

void solve()
{
  int h, w; cin>>h>>w;
  vector<string> bd(h);
  for (auto &line: bd) cin>>line;

  int ans = 0;
  for (int y = 0; y < h; y++) {
    for (int x = 0; x < w; x++) {
      if (bd[y][x] == '.') continue;

      bool has[4]={};
      static const int vect[4][2] = {
        {0, -1}, {1, 0}, {0, 1}, {-1, 0}
      };
      for (int d = 0; d < 4; d++) {
        int dx = vect[d][0];
        int dy = vect[d][1];
        int cx = x + dx;
        int cy = y + dy;
        while (cx >= 0 && cx < w && cy >= 0 && cy < h) {
          if (bd[cy][cx]!='.') {
            has[d]=true;
          }
          cx += dx;
          cy += dy;
        }
      }

      int cd = 0;
      if (bd[y][x] == '^') cd = 0;
      if (bd[y][x] == '>') cd = 1;
      if (bd[y][x] == 'v') cd = 2;
      if (bd[y][x] == '<') cd = 3;

      if (has[cd])
        continue;

      if (has[0]|has[1]|has[2]|has[3]) {
        ans++;
        continue;
      }

      cout << "IMPOSSIBLE" << endl;
      return;
    }
  }
  cout << ans << endl;
}

int main()
{
  int cases; cin>>cases;
  for (int cn=1;cn<=cases;cn++){
    cout << "Case #" << cn << ": ";
    solve();
  }
  return 0;
}
