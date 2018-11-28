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

#define MXA 1000006
#define MXN 105

int A, n, ar[MXN];

int solve() {
  A = SI; n = SI;
  REP(i, n) ar[i] = SI;
  if (A == 1) return n;
  sort(ar, ar+n);
  int ans = n, newCount = 0;
  for (int i = 0; i < n; i++) {
    ans = min(ans, newCount + n - i);
    while (A <= ar[i]) {
      A += A-1;
      newCount++;
    }
    A += ar[i];
  }
  ans = min(ans, newCount);
  return ans;
}

int main()
{
  for(int kase=1,kases=SI;kase<=kases;kase++)
  {
    printf("Case #%d: %d\n", kase, solve());
  }
  return 0;
}
