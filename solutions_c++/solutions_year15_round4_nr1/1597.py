#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cassert>
#include <cstdlib>

using namespace std;

#define ri(X) scanf("%d", &(X))
#define pi(X) printf("%d", (X))
#define mp(X,Y) make_pair(X,Y)
#define pb(X) push_back(X)
#define lint long long
#define pii pair<int,int>
#define inf 1e9
#define linf 1e18
#define X first
#define Y second
#define all(X) (X).begin(),(X).end()
#define uni(X) X.erase(unique(X.begin(), X.end()), X.end());

int t, r, c;
string tod[200];

int m[][4] = {
  {-1, 0, 1, 0},
  { 0, 1, 0,-1}
};

int getNewOri(char a) {
  if (a == '^') return 0;
  else if (a == '>') return 1;
  else if (a == 'v') return 2;
  return 3; //<
}

bool valid(int x, int y) {
  return (0 <= x && x < r && 0 <= y && y < c);
}

bool easyFix(int la, int pla) {
  int xl, xpl, yl, ypl;
  xl = la / c;
  yl = la % c;
  xpl = pla / c;
  ypl = pla % c;
  
  if (xl == xpl) {
    if (yl - ypl > 0) tod[xl][yl] = '<';
    else tod[xl][yl] = '>';
  } else { //yl == ypl
    if (xl - xpl > 0) tod[xl][yl] = '^';
    else tod[xl][yl] = 'v';
  }
  
  return 1;
}

bool trickyFix(int la) {
  int xl, yl, cx, cy, nx, ny;
  xl = la / c;
  yl = la % c;
  for (int o = 0; o < 4; o++) {
    cx = xl;
    cy = yl;
    for (int i = 0; i < r+c; i++) {
      nx = cx + m[0][o];
      ny = cy + m[1][o];
      if (valid(nx, ny)) {
        cx = nx; cy = ny;
        if (tod[nx][ny] != '.') return easyFix(la, cx * c + cy);
      } else break;
    }
  }
  
  return 0;
}

int tryFix(int sx, int sy) {
  if (tod[sx][sy] == '.') return 0;
  int ori = getNewOri(tod[sx][sy]), step = r*c, cx, cy, nx, ny;
  int plt, lt;
  plt = -1;
  lt  = sx * c + sy;
  cx = sx; cy = sy;
  for (int k = 0; k < step; k++) {
    nx = cx + m[0][ori];
    ny = cy + m[1][ori];
    if (valid(nx, ny)) {
      cx = nx;
      cy = ny;
      if (tod[cx][cy] != '.') {
        ori = getNewOri(tod[cx][cy]);
        swap(lt, plt);
        lt = cx * c + cy;
      }
    } else if (plt != -1) {
      if (easyFix(lt, plt)) return 1;
      return -1;
    } else {
      if (trickyFix(lt)) return 1;
      return -1;
    }
  }
  
  return 0;
}

int main(){
  cin >> t;
  
  for (int T = 1; T <= t; T++) {
    ri(r); ri(c);
    for (int i = 0; i < r; i++) cin >> tod[i];
    
    bool go = 1;
    int res = 0;
    for (int i = 0; i < r && go; i++)
      for (int j = 0; j < c && go; j++) {
        int cur = tryFix(i, j);
        
        //for (int k = 0; k < r; k++) cout << tod[k] << endl;
        //cout << endl;
        
        if (cur == -1) go = 0;
        else res += cur;
      }
    
    if (go) printf("Case #%d: %d\n", T, res);
    else printf("Case #%d: IMPOSSIBLE\n", T);
  }
  return 0;
}
