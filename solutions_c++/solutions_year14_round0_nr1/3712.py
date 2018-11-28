#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
using namespace std;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef long long LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for (int i=0; i<(n); ++i)
#define FOR(var,pocz,koniec) for (int var=(pocz); var<=(koniec); ++var)
#define FORD(var,pocz,koniec) for (int var=(pocz); var>=(koniec); --var)
#define FOREACH(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define SIZE(x) (int)x.size()

int q[2];
int a[2][4][4];

int main(){
  int testy;
  scanf("%d",&testy);
  int numer=0;
  while (testy--){
    printf("Case #%d: ",++numer);
    REP(i,2) {
      scanf("%d",q+i);
      REP(j,4) REP(k,4) scanf("%d",&a[i][j][k]);
    }
    int ile = 0, res = -1;
    FOR(x,1,16) {
      int ok[2] = {0,0};
      REP(i,2) REP(k,4) if (a[i][q[i]-1][k] == x) ok[i] = 1;
      if (ok[0] && ok[1]) {
        ile++;
        res = x;
      }
    }
    if (ile == 0) puts("Volunteer cheated!");
    else if (ile > 1) puts("Bad magician!");
    else printf("%d\n", res);
  }
  return 0;
}
