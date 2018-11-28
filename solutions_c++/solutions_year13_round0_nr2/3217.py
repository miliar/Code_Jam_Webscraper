#include<iostream>
#include<string.h>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<deque>
#include<set>
#include<list>
#include<stack>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<cassert>
#define CLRM(x) memset(x,-1,sizeof(x))
#define CLR(x) memset(x,0,sizeof(x))
#define ALL(x) x.begin(),x.end()
#define GI(x) scanf("%d", &x);
#define FORN(i, n) for(int i = 0; i < n; i++)
#define FOR(i, start, end) for(int i = start; i < end; i++)
#define PB push_back
#define MP make_pair
#define VI vector<int> 
#define VVI vector<vector<int> >
#define PII pair<int,int>
#define SZ(x) (int)x.size()
#define LL long long
#define MIN(a,b) (a)<(b)?(a):(b)
#define MAX(a,b) (a)>(b)?(a):(b)
#define LMAX 1000000000000000000LL
#define IMAX 1000000000
using namespace std;

int N, M;
int a[110][110];
int vis[110][110];
void input() {
  GI(N); GI(M);
  FORN(i, N)
    FORN(j, M)
      GI(a[i][j])
}

bool solve() {
  CLR(vis);
  input();
  FORN(i, N) {
    FORN(j, M) {
      if (vis[i][j])
        continue;
      int done = 0;
      bool flag = false;
      FORN(k, M) {
        if(a[i][k] > a[i][j]) {
          flag = true;
          break;
        }
      }
      if (!flag) {
        done++;
        FORN(k, M) {
          if (a[i][k] == a[i][j])
            vis[i][k] = 1;
        }
      }
      flag = false;
      FORN(k, N) {
        if (a[k][j] > a[i][j]) {
          flag = true;
          break;
        }
      }
      if (!flag) {
        done++;
        FORN(k, N) {
          if (a[k][j] == a[i][j])
            vis[k][j] = 1;
        }
      }
      if (done == 0) {
        return false;
      }
    }
  }
  return true;
}
int main() {
  int T;
  GI(T);
  FORN(i, T) {
    printf("Case #%d: ", i+1);
    bool ans = solve();
    if (ans) {
      printf("YES\n");
    } else {
      printf("NO\n");
    }
  }
  return 0;
}
