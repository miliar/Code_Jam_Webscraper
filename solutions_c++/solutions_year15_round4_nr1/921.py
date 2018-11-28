// C++11
#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
  int T; scanf("%d", &T);
  for(int tci = 0; tci < T; ++tci) {
    int R, C; scanf("%d%d", &R, &C);
    static char tbl[110][110];
    for(int y = 0; y < R; ++y) {
      scanf(" %s", tbl[y]);
    }
    static int tblcnt[110][110];
    for(int y = 0; y < R; ++y) {
      for(int x = 0; x < C; ++x) {
        tblcnt[y][x] = 0;
      }
    }
    static bool tbl2[4][110][110];
    for(int y = 0; y < R; ++y) {
      for(int x = 0; x < C; ++x) {
        tbl2[0][y][x] = (y==0 ? false : (tbl2[0][y-1][x] || tbl[y-1][x]!='.'));
        tbl2[1][y][x] = (x==0 ? false : (tbl2[1][y][x-1] || tbl[y][x-1]!='.'));
        tblcnt[y][x] += tbl2[0][y][x];
        tblcnt[y][x] += tbl2[1][y][x];
      }
    }
    for(int y = R-1; y >= 0; --y) {
      for(int x = C-1; x >= 0; --x) {
        tbl2[2][y][x] = (y==R-1 ? false : (tbl2[2][y+1][x] || tbl[y+1][x]!='.'));
        tbl2[3][y][x] = (x==C-1 ? false : (tbl2[3][y][x+1] || tbl[y][x+1]!='.'));
        tblcnt[y][x] += tbl2[2][y][x];
        tblcnt[y][x] += tbl2[3][y][x];
      }
    }
    bool wholeok = true;
    int cnt = 0;
    for(int y = 0; y < R; ++y) {
      for(int x = 0; x < C; ++x) {
        if(tbl[y][x]=='.') continue;
        if(tblcnt[y][x] == 0) wholeok = false;
        bool needcnt = false;
        if(!tbl2[0][y][x] && tbl[y][x]=='^') needcnt = true;
        if(!tbl2[1][y][x] && tbl[y][x]=='<') needcnt = true;
        if(!tbl2[2][y][x] && tbl[y][x]=='v') needcnt = true;
        if(!tbl2[3][y][x] && tbl[y][x]=='>') needcnt = true;
        cnt += needcnt;
      }
    }
    if(wholeok) {
      printf("Case #%d: %d\n", tci+1, cnt);
    } else {
      printf("Case #%d: IMPOSSIBLE\n", tci+1);
    }
  }
  return 0;
}
