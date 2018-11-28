#include <string>
#include <cstring>
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
#define FOR(a,b,c) for(int a=(b); a<=(c); ++a)
#define FORD(a,b,c) for(int a=(b); a>=(c); --a)
#define INIT(a, v) __typeof(v) a = (v)
#define FOREACH(a, v) for (INIT(a, (v).begin()); a!=(v).end(); ++a)
 
template<class T>
inline int size(const T&t){return t.size();}
 
typedef vector<string> vs;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long LL;

#define INF 1000000000
#define PB push_back
#define MP make_pair
 
//////////////////////////////////////////

int N, x[1000], y[1000];


inline int il_wek(int w1, int w2, int w3) {
  return (x[w2]-x[w1])*(y[w3]-y[w1])-(x[w3]-x[w1])*(y[w2]-y[w1]);
}

inline bool czy_przec(int w1, int w2, int w3, int w4) {
  LL i1 = il_wek(w1, w2, w3)*(LL)il_wek(w1, w2, w4);
  LL i2 = il_wek(w3, w4, w1)*(LL)il_wek(w3, w4, w2);
  if (i1==0 && i2 == 0) {
    int xx = max(x[w1], x[w2]);
    int xx2 = min(x[w3], x[w4]);
    if (xx<xx2) return 0;
    xx = min(x[w1], x[w2]);
    xx2 = max(x[w3], x[w4]);
    if (xx2<xx) return 0;
    int yy = max(y[w1], y[w2]);
    int yy2 = min(y[w3], y[w4]);
    if (yy<yy2) return 0;
    yy = min(y[w1], y[w2]);
    yy2 = max(y[w3], y[w4]);
    if (yy2<yy) return 0;
    return 1;
  }
  else
  return i1<=0 && i2<=0;
}

int perm[1000];

int best;
int best_kol[1000];

void licz() {
   best = 0;
        REP(a, N)
          perm[a] = a;
  for(;;) {
    REP(a, N)
      REP(b, a-1) {
        if (a==N-1 && b==0) continue;
        if (czy_przec(perm[a], perm[(a+1)%N], perm[b], perm[(b+1)%N])) 
          goto zle;
      }
    {
    int pole = 0;
    REP(a, N) {
      int w1 = perm[a];
      int w2 = perm[(a+1)%N];
      pole += (x[w2]-x[w1])*(y[w2]+y[w1]);
    }
    pole = abs(pole);
    if (pole>=best) {
      REP(a, N)
        best_kol[a] = perm[a];
      best = pole;
    }
    }
    zle:;  
    if (!next_permutation(perm, perm+N))  break;
  }

}

int main() {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        scanf("%d", &N);
        REP(a, N)
          scanf("%d%d", &x[a], &y[a]);
        licz();
        printf("Case #%d:", (tt+1));
        REP(a, N)
          printf(" %d", best_kol[a]);
        printf("\n");
    }
}


