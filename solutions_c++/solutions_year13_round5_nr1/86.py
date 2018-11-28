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

LL B;
int N;
LL wpl[38];
LL moje[38];

double oblicz() {
  int ok = 1;
  double res = 0;
  REP(a, 37) {
    if (moje[a]+wpl[a]==moje[0])
      ok = a+1;
    res -= moje[a];
  }
  REP(a, ok)
    res += moje[a]*36./ok;
  return res;
}

double licz() {
  double best = 0;
  REP(a, 37)
    moje[a] = 0;
  FOR(a, N, 36)
    wpl[a] = 0;
  sort(wpl, wpl+37);
  FORD(a, 36, 0)
    wpl[a] -= wpl[0];
  wpl[37] = INF*(LL)INF;
  moje[37] = 0;
  LL zos = B;
  FOR(a, 1, 36) {
    if (moje[a]>0)
      continue;
    LL moge = max(0LL, min(zos/a, wpl[a]-moje[0])-1);
    REP(b, a) {
      moje[b] += moge;
      zos -= moge;
    }
    best = max(best, oblicz());
    REP(x, 2) {
      FORD(y, 36, 0)
        if (wpl[y]+moje[y]==moje[0] && zos) {
          ++moje[y];
          --zos;
          best = max(best, oblicz());
        }
    }
  }
  return best;
}

int main() {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        scanf("%lld%d", &B, &N);
        REP(a, N)
          scanf("%lld", &wpl[a]);
        printf("Case #%d: %.9f\n", (tt+1), licz());
    }
}


