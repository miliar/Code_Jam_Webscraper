//CONTEST SOURCE
#include <iostream>
#include <cstring>
#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <queue>
using namespace std;
#define ll long long
#define pii pair<int, int>
#define mp make_pair
#define x first
#define y second
#define pb push_back
#define VI vector<int>
#define all(s) (s).begin(),(s).end()
#define L(s) (int)(s).size()
#define inf 1000000000
#define pdd pair<double, double>
int n, t, m;
char a[16][16];
int u[64][16][16][4];
int dx[]  = {
  -1, 0, 1, 0};
int dy[] = {
  0, 1, 0, -1};
int seq[64];
queue<pair<pair<int, int> , pair<int, int>  > > q;
void get(int guy, int &pi, int &pj, int &pw) {
  if (guy < m) {
    pi = 0; pj = guy; pw = 0;
  }
  if (guy >= m && guy < n + m) {
    pi = guy - m; pj = m - 1; pw = 1;
  }
  if (guy >= n + m && guy < n + m + m) {
    pi = n - 1; pj = m - 1 - (guy - n - m); pw = 2;
  }
  if (guy >= n + m + m && guy < n + n + m + m) {
    pi = n - 1 - (guy - n - m - m); pj = 0; pw = 3;
  }
}
int main() {
  freopen("C-small-attempt0.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  cin >> t;
  for(int tc = 1; tc <= t; ++tc) {
    cerr << tc << endl;
    cin >> n >> m;
    for(int i = 0; i < 2 * n + 2 * m; ++i) {
      cin >> seq[i]; --seq[i];
    }
    cout << "Case #" << tc << ":\n";
    bool found = 0;
    for(int mask = 0; mask < (1 << (n * m)); ++mask) {
      int bit = 0;
      for(int i = 0; i < n; ++i) {
        for(int j = 0; j < m; ++j) {
          a[i][j] = '\\';
          if (mask & (1 << bit)) {
            a[i][j] = '/';
          }
          ++bit;
        }
      }

      memset(u, 0, sizeof(u));
      while(!q.empty()) q.pop();

      for(int guy = 0; guy < (2 * n + 2 * m); ++guy) {
        int pi, pj, pw;
        get(guy, pi, pj, pw);
        u[guy][pi][pj][pw] = 1;
        q.push(mp(mp(pi, pj), mp(guy, pw)));
      }

      while(!q.empty()) {
        int pi = q.front().x.x;
        int pj = q.front().x.y;
        int guy = q.front().y.x;
        int pw = q.front().y.y;
        q.pop();

        int ni, nj, nw;
        ni = pi + dx[pw];
        nj = pj + dy[pw];
        nw = (pw + 2) % 4;
        if (ni >= 0 && ni < n && nj >= 0 && nj < m &&
            !u[guy][ni][nj][nw]) {
          u[guy][ni][nj][nw] = 1;
          q.push(mp(mp(ni, nj), mp(guy, nw)));
        }

        ni = pi;
        nj = pj;
        if (a[pi][pj] == '/') {
          if (pw == 0) nw = 3; else
            if (pw == 3) nw = 0; else
              if (pw == 1) nw = 2; else
                if (pw == 2) nw = 1;
        }
        if (a[pi][pj] == '\\') {
          if (pw == 0) nw = 1; else
            if (pw == 1) nw = 0; else
              if (pw == 2) nw = 3; else
                if (pw == 3) nw = 2;
        }

        if (!u[guy][ni][nj][nw]) {
          u[guy][ni][nj][nw] = 1;
          q.push(mp(mp(ni, nj), mp(guy, nw)));
        }
      }

      bool ok = 1;
      for(int guy = 0; guy < (2 * n + 2 * m); guy += 2) {
        int pi, pj, pw;
        int qi, qj, qw;
        int pguy = seq[guy];
        int qguy = seq[guy + 1];
        for(int i = 0; i < n; ++i) {
          for(int j = 0; j < m; ++j) {
            for(int w = 0; w < 4; ++w) {
              if (u[pguy][i][j][w] && !u[qguy][i][j][w]) ok = 0;
              if (u[qguy][i][j][w] && !u[pguy][i][j][w]) ok = 0;
              for(int oguy = 0; oguy < (2 * n + 2 * m); ++oguy) {
                if (u[pguy][i][j][w] && u[oguy][i][j][w] &&
                    oguy != pguy && oguy != qguy) {
                  ok = 0;
                  break;
                }
              }
              if (!ok) break;
            }
            if (!ok) break;
          }
          if (!ok) break;
        }
        if (!ok) break;
      }

      if (ok) {
        for(int i = 0; i < n; ++i) {
          for(int j = 0; j < m; ++j) {
            cout << a[i][j];
          }
          cout << endl;
        }
        found = 1;
        break;
      }
    }
    if (!found) cout << "IMPOSSIBLE\n";
  }
}
