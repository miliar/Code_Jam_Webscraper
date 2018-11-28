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

int ys, xs;
int tab[100][100];
int row[100], col[100];

bool licz() {
  REP(y, 100) row[y] = col[y] = 0;
  REP(x, xs) REP(y, ys) {
    row[y] = max(row[y], tab[y][x]);
    col[x] = max(col[x], tab[y][x]);
  }
  REP(x, xs) REP(y, ys)
    if (tab[y][x]<min(row[y], col[x]))
      return 0;
  return 1;
}

int main() {
  int TT;
  scanf("%d ", &TT);
  REP(tt, TT) {
    scanf("%d%d", &ys, &xs);
    REP(y, ys)
      REP(x, xs)
        scanf("%d", &tab[y][x]);
    printf("Case #%d: %s\n", tt+1, licz() ? "YES" : "NO");
  }
}
