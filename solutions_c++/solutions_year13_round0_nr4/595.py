#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)
#define REPDN(i,n) for(int i=(n)-1;i>=0;--i)
#define FORE(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)

const int N = 21;
int Te,k,n,typ[N],a;
vector<int> pocz,klucze[N];

int mozna[1<<N], najm[1<<N];

int main() {
   scanf("%d",&Te);
   REP(te,Te) {
      scanf("%d%d",&k,&n);
      pocz.clear();
      REP(i,n) klucze[i].clear();
      REP(i,k) { scanf("%d",&a); pocz.push_back(a); }
      REP(i,n) {
         int ile;
         scanf("%d%d",&typ[i],&ile);
         REP(j,ile) { scanf("%d",&a); klucze[i].push_back(a); }
      }
      // mozna[mask] - zakladajac, ze otworzylismy mask, czy da sie dalej?
      mozna[(1<<n)-1] = 1;
      REPDN(mask,(1<<n)-1) {
         mozna[mask] = 0;
         int zmask = (1<<n)-1 - mask;
         vector<int> v = pocz;
         REP(i,n) if (mask&1<<i) FORE(j,klucze[i]) v.push_back(*j);
         REP(i,n) if (mask&1<<i) {
            vector<int>::iterator it=find(v.begin(),v.end(),typ[i]);
            if (it == v.end()) goto end;
            v.erase(it);
         }

         REP(i,n) if (zmask&1<<i) {
            vector<int> u = v;
            vector<int>::iterator it = find(u.begin(),u.end(),typ[i]);
            if (it == u.end()) continue;
            if (!mozna[mask + (1<<i)]) continue;
            u.erase(it);
            mozna[mask] = 1;
            najm[mask] = i;
            break;
         }
end: ;
      }
      printf("Case #%d:", te+1);
//REP(ii,1<<n) printf("%d: %d\n",ii,mozna[ii]);
      if (mozna[0]) {
         int mask=0;
         REP(i,n) {
            printf(" %d",najm[mask]+1);
            mask += 1<<najm[mask];
         }
         printf("\n");
      }
      else printf(" IMPOSSIBLE\n");
   }
}
