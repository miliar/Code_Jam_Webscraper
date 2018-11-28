#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

#define REP(i,n) for(int i = 0; i < (n); ++i)
#define FOR(i,a,b) for(int i = (a); i <= (b); ++i)
#define FORD(i,a,b) for(int i = (a); i >= (b); --i)
#define FORE(it,V) for(__typeof__(V.begin()) it = V.begin(); it != V.end(); ++it)
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
typedef long long LL;

int poziom[105][105];
int poziom2[105][105];

bool kos(int startx, int starty, int stopx, int stopy, int v) {
  FOR(i,startx, stopx) FOR(j,starty,stopy) {
    poziom2[i][j] = min(poziom2[i][j], v);
    if (poziom2[i][j] < poziom[i][j]) {
      return false;
    }
  }
  return true;
}

bool testcase() {
  int n, m;
  scanf("%d%d", &n, &m);
  REP(i,n) REP(j,m) scanf("%d", &poziom[i][j]);
  REP(i,n) REP(j,m) poziom2[i][j] = 100;

  REP(i,n) {
    bool identyczne = true;
    FOR(j,0,m-2) if (poziom[i][j] != poziom[i][j+1]) {
      identyczne = false; 
    }
    if (identyczne) {
      if (!kos(i,0,i,m-1,poziom[i][0])) {
	return false;
      }
    } else {
      REP(j,m) {
	if (!kos(0,j,n-1,j,poziom[i][j])) {
	  return false;
	}
      }
    }
  }

  REP(i,n) REP(j,m) if (poziom2[i][j] != poziom[i][j]) {
    return false;
  }
  return true;
}

int main() {
  int t;
  scanf("%d", &t);
  FOR(i,1,t) {
    printf("Case #%d: ", i);
    if (testcase()) {
      printf("YES\n");
    } else {
      printf("NO\n");
    }
  }
}
