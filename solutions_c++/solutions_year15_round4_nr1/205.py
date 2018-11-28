#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define ull unsigned long long
#define ld long double
#define pb push_back
#define popb pop_back

#define pii pair<int,int>
#define mp make_pair
#define X first
#define Y second

#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)

#define maxN 105

int T;
int R, C;
char arr[maxN][maxN];
int dir[300];
int dirs[4][2] = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};

int main() {
  dir['>'] = 0;
  dir['v'] = 1;
  dir['^'] = 2;
  dir['<'] = 3;
  dir['.'] = -1;
  scanf("%d", &T);
  FOR(t, 1, T) {
    scanf("%d%d", &R, &C);
    REP(i, R) scanf("%s", arr[i]);
    int cnt = 0;
    bool imp = false;
    REP(i, R) REP(j, C) {
      int d = dir[arr[i][j]];
      if (d != -1) {
        bool ok[4] = {false, false, false, false};
        REP(dd, 4) {
          int x = i, y = j;
          REP(k, maxN) {
            x += dirs[dd][0];
            y += dirs[dd][1];
            if (x < 0 || y < 0 || x >= R || y >= C) break;
            if (arr[x][y] != '.') { ok[dd] = true; break; }
          }
        }
        if (ok[d]) continue;
        if (!ok[0] && !ok[1] && !ok[2] && !ok[3]) {
          imp = true;
        }
        ++cnt;
      }
    }
    printf("Case #%d: ", t);
    if (imp) {
      printf("IMPOSSIBLE\n");
    } else {
      printf("%d\n", cnt);
    }
  }

  return 0;
}
