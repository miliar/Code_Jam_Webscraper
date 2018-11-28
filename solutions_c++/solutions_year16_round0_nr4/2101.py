#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cctype>
#include <sstream>
#include <iterator>
#include <string>
#include <vector>

using namespace std;

typedef long long LL;

#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define FORL(v,p,k) for(int v=p;v<k;++v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()

int main()
{
  int n, k, c, s;
  scanf("%d", &n);
  REP(ii, n) {
    printf("Case #%d:", ii+1);
    scanf("%d%d%d", &k, &c, &s);
    if (s * c < k) printf(" IMPOSSIBLE");
    else{
      int cc = 0;
      long long w = 1LL, z = 1LL;
      REP(i, k){
        w += z * (LL)i;
        z *= (LL)k;
        cc++;
        if (cc == c){
          cc = 0;
          printf(" %lld", w);
          w = z = 1LL;
        }
      }
      if (cc > 0) printf(" %lld", w);
    }
    printf("\n");
  }
  return 0;
}
