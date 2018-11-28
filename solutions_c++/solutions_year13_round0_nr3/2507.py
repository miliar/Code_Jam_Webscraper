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

#define MX 100005

bool palin(LL x) {
  LL y = x, ry = 0;
  while (x!=0) ry=ry*10+x%10, x/=10;
  return y == ry;
}

int main()
{
  vector<LL> yo;
  for (LL x = 1; x <= 10000000; x++) {
    if (palin(x) && palin(x*x)) yo.PB(x*x);
  }
  for(int kase=1,kases=SI;kase<=kases;kase++)
  {
    printf("Case #%d: ",kase);
    LL a, b;
    scanf("%lld %lld", &a, &b);
    int ans = 0;
    EACH(it, yo) if(a<=*it && *it<=b) ans++;
    printf("%d\n",ans);
  }
  return 0;
}
