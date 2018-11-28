#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <vector>

using namespace std;

#define FOR(prom, a, b) for(int prom = (a); prom < (b); prom++)
#define FORD(prom, a, b) for(int prom = (a); prom > (b); prom--)
#define FORDE(prom, a, b) for(int prom = (a); prom >= (b); prom--)

#define DRI(a) int a; scanf("%d ", &a);
#define DRII(a, b) int a, b; scanf("%d %d ", &a, &b);
#define DRIII(a, b, c) int a, b, c; scanf("%d %d %d ", &a, &b, &c);
#define DRIIII(a, b, c, d) int a, b, c, d; scanf("%d %d %d %d ", &a, &b, &c, &d);
#define RI(a) scanf("%d ", &a);
#define RII(a, b) scanf("%d %d ", &a, &b);
#define RIII(a, b, c) scanf("%d %d %d ", &a, &b, &c);
#define RIIII(a, b, c, d) scanf("%d %d %d %d ", &a, &b, &c, &d);

#define PB push_back
#define MP make_pair

#define ll long long
#define ull unsigned long long

#define MM(co, cim) memset((co), (cim), sizeof((co)))

#define DEB(x) cerr << ">>> " << #x << " : " << x << endl;

char mp[107][107];

int main ()
{
  DRI(T);
  FOR(t,0,T) {
    DRII(R,C);
    FOR(i,0,R) cin >> mp[i];
    int cnt = 0;
    try {
    FOR(r,0,R) FOR(c,0,C) {
      bool safe = false;
      switch(mp[r][c]) {
      case '^': FORDE(r2,r-1,0) if(mp[r2][c] != '.') safe = true; break;
      case 'v': FOR(r2,r+1,R) if(mp[r2][c] != '.') safe = true; break;
      case '<': FORDE(c2,c-1,0) if(mp[r][c2] != '.') safe = true; break;
      case '>': FOR(c2,c+1,C) if(mp[r][c2] != '.') safe = true; break;
      default: safe = true; break;
      }
      if(!safe) {
        FORDE(r2,r-1,0) if(mp[r2][c] != '.') safe = true;
        FOR(r2,r+1,R) if(mp[r2][c] != '.') safe = true;
        FORDE(c2,c-1,0) if(mp[r][c2] != '.') safe = true;
        FOR(c2,c+1,C) if(mp[r][c2] != '.') safe = true;
        if(!safe) {
          cnt = -1;
          throw -1;
        } else cnt++;
      }
    }
    } catch(int e) {}
    if(cnt == -1) printf("Case #%d: IMPOSSIBLE\n", t+1);
    else printf("Case #%d: %d\n", t+1, cnt);
  }
  return 0;
}
