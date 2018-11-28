#include <string>
#include <vector>
#include <cmath> 
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
 
using namespace std;
 
#define REP(a,n) for(int a=0; a<(n); ++a)
#define FORD(a,b,c) for(int a=(b); a>=(c); --a)
 
template<class T>
inline int size(const T&t){return t.size();}
 
//////////////////////////////////////////

int K, N;
int pocz[40];
int kl_wew[20][40];
int ile_wew[20];
int kl_pot[20];

bool wygr[1<<20];
int next[1<<20];

void licz() {
  wygr[(1<<N)-1] = 1;
  FORD(xx, (1<<N)-2, 0) {
    map<int, int> mam;
    REP(a, K)
      ++mam[pocz[a]];
    REP(a, N)
      if (xx&(1<<a)) {
        --mam[kl_pot[a]];
        REP(b, ile_wew[a])
          ++mam[kl_wew[a][b]];
      }
    wygr[xx] = 0;
    REP(a, N)
      if (!(xx&(1<<a)) && wygr[xx|(1<<a)] && mam[kl_pot[a]]>0) {
        wygr[xx] = 1;
        next[xx] = a;
        break;
      }
  }
}

int main() {
  int TT;
  scanf("%d ", &TT);
  REP(tt, TT) {
    scanf("%d%d", &K, &N);
    REP(a, K)
      scanf("%d", &pocz[a]);
    REP(a, N) {
      scanf("%d%d", &kl_pot[a], &ile_wew[a]);
      REP(b, ile_wew[a])
        scanf("%d", &kl_wew[a][b]);
    }
    licz();
    printf("Case #%d:", tt+1);
    if (!wygr[0])
      printf(" IMPOSSIBLE");
    else {
      int x = 0;
      while (x<(1<<N)-1) {
        printf(" %d", next[x]+1);
        x |= 1<<next[x];
      }
    }
    printf("\n");
  }
}
