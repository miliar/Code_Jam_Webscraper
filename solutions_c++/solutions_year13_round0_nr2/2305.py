#include <cstdio>
#include <algorithm>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)

const int N = 110;
int Te,n,m,a[N][N],maxw[N],maxk[N],ok;

int main() {
   scanf("%d",&Te);
   REP(te,Te) {
      scanf("%d%d",&n,&m);
      REP(i,n) REP(j,m) scanf("%d",&a[i][j]);
      REP(i,n) maxw[i] = 0;
      REP(j,m) maxk[j] = 0;
      REP(i,n) REP(j,m) {
         maxw[i] = max(maxw[i], a[i][j]);
         maxk[j] = max(maxk[j], a[i][j]);
      }
      ok=1;
      REP(i,n) REP(j,m) {
         if (maxw[i] > a[i][j] && maxk[j] > a[i][j])
            ok=0;
      }
      printf("Case #%d: %s\n", te+1, ok ? "YES":"NO");
   }
}
