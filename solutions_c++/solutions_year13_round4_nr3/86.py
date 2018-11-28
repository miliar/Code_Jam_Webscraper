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
#define FOR(a, b, c) for (int a = (b); a<=(c); ++a)
#define FORD(a, b, c) for (int a = (b); a>=(c); --a)
#define VAR(a, b) __typeof(b) a = (b)
#define FOREACH(a, b) for (VAR(a, (b).begin()); a!=(b).end(); ++a)
 
#define MP make_pair
#define PB push_back 
#define INF 1000000000

typedef long long LL; 
typedef pair<int, int> pii;
typedef vector<int> vi;

template<class T>
inline int size(const T&t){return t.size();}
 
//////////////////////////////////////////

int N, A[2000], B[2000];
vi rel[2000];
int zajete[2001];


int tab[2000];

void dfs(int st) {
  if (tab[st]) return;
  tab[st] = 1;
  FOREACH(it, rel[st])
    dfs(*it);
}

int ile_mn(int st) {
  REP(a, N)
    tab[a] = 0;
  dfs(st);
  int ile = 0;
  FOR(x, st+1, N-1)
    ile += tab[x];
  return ile;
}

int wyn[2000];

void licz() {
  REP(a, N) rel[a].clear();
  REP(a, N) {
    FORD(b, a-1, 0)
      if (A[b]==A[a]) {
        rel[b].PB(a);
        break;
      }
    if (A[a]>1)
      FORD(b, a-1, 0)
        if (A[b]+1==A[a]) {
          rel[a].PB(b);
          break;
        }
  }
  REP(a, N) {
    FOR(b, a+1, N-1)
      if (B[b]==B[a]) {
        rel[b].PB(a);
        break;
      }
    if (B[a]>1)
      FOR(b, a+1, N-1)
        if (B[b]+1==B[a]) {
          rel[a].PB(b);
          break;
        }
  }
  
  REP(a, N)
    zajete[a] = 0;
  REP(a, N) {
    int i = ile_mn(a);
    int p = 0;
    while (zajete[p] || i) {
      if (zajete[p]) ++p;
      else {
        --i; ++p;
      }
    }
    wyn[a] = p;
    zajete[p] = 1;
  }
}

int main() {
  int TT;
  scanf("%d ", &TT);
  REP(tt, TT) {
    scanf("%d", &N);
    REP(a, N)
      scanf("%d", &A[a]);
    REP(a, N)
      scanf("%d", &B[a]);
    printf("Case #%d:", tt+1);
    licz();
    REP(a, N)
      printf(" %d", wyn[a]+1);
    printf("\n");
  }
}
