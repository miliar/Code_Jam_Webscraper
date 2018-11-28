#include <iostream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <complex>
#include <string>
#include <stdint.h>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>

using namespace std;

#define REP(i,n) for(int i = 0; i < (int)(n); i++)
#define rep(i,m,n) for(int i = m; i < (int)(n); i++)
#define FOR(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define ALLOF(c) (c).begin(), (c).end()

typedef double decimal;
typedef complex<decimal> P;

const decimal EPS = 1e-8;

const int MOD = 1000000007;

static pair<pair<int, int>, int> pos(int x, int R, int C){
  if(x < C){
    return make_pair(make_pair(-1, x), 2);
  }else if(x - C < R){
    return make_pair(make_pair(x - C, C), 3);
  }else if(x - C - R < C){
    return make_pair(make_pair(R, C - (x - C - R) - 1), 0);
  }else{
    return make_pair(make_pair(R - (x - C - R - C) - 1, -1), 1);
  }
}

static bool solve(bool f[][102], int p[][2], int R, int C){
  int delta[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
  int refl[4][2] = {{3, 1}, {2, 0}, {1, 3}, {0, 2}};
  REP(i, R + C){
    pair<pair<int, int>, int> s, t;
    s = pos(p[i][0], R, C);
    t = pos(p[i][1], R, C);
    int x, y, d;
    d = s.second;
    x = s.first.first + delta[d][0];
    y = s.first.second + delta[d][1];
    while(x >= 0 && x < R && y >= 0 && y < C){
      d = refl[d][f[x][y]];
      x += delta[d][0];
      y += delta[d][1];
    }
    if(x != t.first.first || y != t.first.second){
      return false;
    }
  }
  return true;
}

int main(){
  int T;
  cin >> T;
  REP(i, T){
    int R, C;
    cin >> R >> C;
    int p[200][2];
    REP(j, R + C) REP(k, 2){
      int d;
      cin >> d;
      p[j][k] = d - 1;
    }
    printf("Case #%d:\n", i+1);
    bool f[102][102];
    bool ok = false;
    REP(x, 1 << R * C){
      REP(q, R * C){
        f[q / C][q % C] = (x & (1 << q)) != 0;
      }
      if(solve(f, p, R, C)){
        REP(j, R){
          REP(k, C){
            putchar(f[j][k] ? '/' : '\\');
          }
          puts("");
        }
        ok = true;
        break;
      }
    }
    if(!ok){
      puts("IMPOSSIBLE");
    }
  }

  return 0;
}

