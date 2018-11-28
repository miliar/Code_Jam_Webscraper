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
 
#define INF 1000000000

typedef long long LL; 

template<class T>
inline int size(const T&t){return t.size();}
 
//////////////////////////////////////////

LL licz(int N, LL P) {
  --P;
  int ile0 = N;
  REP(a, N+1) {
    int x = 0;
    REP(b, N)
      if (!((1LL<<b)&P))
        ++x;
    ile0 = min(ile0, x);
    if (a==N) break;
    if ((1LL<<a)&P) {
      P &= ~(1LL<<a);
      REP(b, a)
        P |= 1LL<<b;
    }
  }
  return (1LL<<N)-(1LL<<ile0);
}

int main() {
  int TT;
  scanf("%d ", &TT);
  REP(tt, TT) {
    int N;
    LL P;
    scanf("%d%lld", &N, &P);
    printf("Case #%d: %lld %lld\n", tt+1, P==(1LL<<N) ? (1LL<<N)-1: ((1LL<<N)-2-licz(N, (1LL<<N)-P)), licz(N, P));
  }
}
