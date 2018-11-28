/* AnilKishore * India */

#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>

#include <iostream>
#include <algorithm>
#include <string>

#include <vector>
#include <set>
#include <map>
#include <queue>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PI;

#define PB(x) push_back(x)
#define MP(x,y) make_pair(x,y)
#define F first
#define S second
#define SET(v,x) memset(v,x,sizeof v)
#define FOR(i,a,b) for(int _n(b),i(a);i<_n;i++)
#define EACH(it,v) for(typeof((v).begin()) it = (v).begin();it!=(v).end();it++)
#define REP(i,n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()
#define SORT(v) sort(ALL(v))
#define SZ(v) int(v.size())
#define SI ({int x;scanf("%d",&x);x;})

#define MX 105

int n, m;
int A[MX][MX];
int mustCut[MX];

bool colOK() {
  REP(j,m) if (mustCut[j]) {
    bool allEqual = true;
    REP(i,n-1) if (A[i][j] != A[i+1][j]) return false;
  }
  return true;
}

int main()
{
  for(int kase=1,kases=SI;kase<=kases;kase++)
  {
    printf("Case #%d: ",kase);
    n = SI; m = SI;
    REP(i,n) REP(j,m) A[i][j] = SI;
    SET(mustCut, 0);
    REP(i,n) {
      int mx = 0;
      REP(j,m) mx = max(mx, A[i][j]);
      REP(j,m) if (A[i][j]!=mx) mustCut[j] = 1;
    }
    puts(colOK() ? "YES" : "NO");
  }
  return 0;
}
