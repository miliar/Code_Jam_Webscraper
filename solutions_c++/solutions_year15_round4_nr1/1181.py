#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

#ifdef DEBUG
#include "/home/lucas/Topcoder/debug.h"
#define dbg(args...) do {cerr << #args << ": "; debug,args; cerr << endl;} while(0)
#else
#define dbg(args...)
#endif

int r,c;

#define MAX 200
char f[MAX][MAX];

bool is_it_ok(int i, int j, char dir) {
  int dx = 0 , dy = 0;
  if (dir == '^') dx = -1;
  else if(dir == 'v') dx = +1;
  else if(dir == '<') dy = -1;
  else if(dir == '>') dy = +1;

  if (dir == '.') return true;

  i += dx;
  j += dy;

  while ( i >= 0 && i < r && j >= 0 && j < c) {
    if (f[i][j] != '.') return true;
    i += dx;
    j += dy;
  }
  return false;
}

int cn;

bool solve() {
  int ans = 0;
  for(int i=0; i<r; i++) {
    for(int j=0; j<c; j++) {
      if (!is_it_ok(i, j, f[i][j])) {
        bool ok = false;
        for(char x : {'<', '>', '^', 'v'}) {
          if (is_it_ok(i,j, x)) {
            ok = true;
            break;
          }
        }
        if (!ok) return false;
        ans ++;
      }
    }
  }
  printf("Case #%d: %d\n", cn, ans);
  return true;
}

int main() {
  ios :: sync_with_stdio(0);
  int t; cin >> t;
  for(cn=1; cn<=t; cn++) {
    cin >> r >> c;
    for(int i=0; i<r; i++) {
      cin >> f[i];
    }


    if (!solve()) {
      printf("Case #%d: IMPOSSIBLE\n", cn);
    }
  }
  return 0;
}
