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
 
#define REP(a, b) for (int a = 0; a<(b); ++a)
#define FOR(a, b, c) for (int a = (b); a<=(c); ++a)
#define FORD(a, b, c) for (int a = (b); a>=(c); --a)
#define VAR(a, b) __typeof(b) a = (b)
#define FOREACH(a, b) for (VAR(a, (b).begin()); a!=(b).end(); ++a)
 
#define MP make_pair
#define PB push_back
#define INF 1000000000

typedef long long LL; 

template<class T>
inline int size(const T&t){return t.size();}
 
//////////////////////////////////////////

#define MOD 1000002013

int N, ilep;
int start[1000], stop[1000], ile[1000];

inline int koszt(int a, int b, LL mn) {
//  printf("z %d do %d jedzie %lld ludzi\n", a, b, mn);
  int odl = b-a;
  int w = ((LL)2*N+1-odl)*odl/2%MOD;
  return w*(mn%MOD)%MOD;
}

int licz() {
  map<int, LL> ws;
  REP(a, ilep) {
    ws[start[a]] += ile[a];
    ws[stop[a]] -= ile[a];
  }
  int plac = 0;
  vector<pair<int, LL> > pasa;
  FOREACH(it, ws) {
    int poz = it->first;
    LL ilosc = it->second;
    if (ilosc>0)
      pasa.PB(MP(poz, ilosc));
    else {
      ilosc = -ilosc;
      while (ilosc) {
        LL wys = min(ilosc, pasa.back().second);
        ilosc -= wys;
        plac = (plac+koszt(pasa.back().first, poz, wys))%MOD;
        pasa.back().second -= wys;
        if (!pasa.back().second)
          pasa.pop_back();
      }
    }
  }
//  printf("aa\n");
  int pow = 0;
  REP(a, ilep)
    pow = (pow+koszt(start[a], stop[a], ile[a]))%MOD;
  return (pow+MOD-plac)%MOD;
  
}

int main() {
  int TT;
  scanf("%d ", &TT);
  REP(tt, TT) {
    scanf("%d%d", &N, &ilep);
    REP(a, ilep)
      scanf("%d%d%d", &start[a], &stop[a], &ile[a]);
    printf("Case #%d: %d\n", tt+1, licz());
  }
}
