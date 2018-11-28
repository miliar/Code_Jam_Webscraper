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
#define INIT(i,v) __typeof(v) i = (v)
#define FOREACH(i,v) for(INIT(i, (v).begin()); i!=(v).end(); ++i)
#define MP make_pair
#define PB push_back
 
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long LL;
 
template<class T>
inline int size(const T&t){return t.size();}

#define INF 1000000000
 
//////////////////////////////////////////

int tab[10][10], bylo;

int R, C, M;

int sx[8] = { 1, 1, 1, 0,-1,-1,-1, 0},
    sy[8] = {-1, 0, 1, 1, 1, 0,-1,-1};

inline bool czy_mina_obok(int x, int y) {
  REP(d, 8)
    if (tab[x+sx[d]][y+sy[d]]==1)
      return 1;
  return 0;
}

void rozszerzaj(int x, int y) {
  ++bylo;
  tab[x][y] = 0;
  if (!czy_mina_obok(x, y))
    REP(d, 8)
      if (tab[x+sx[d]][y+sy[d]]==2)
        rozszerzaj(x+sx[d], y+sy[d]);
}

void sprawdz() {
  FOR(x, 1, C)
    FOR(y, 1, R)
      if (tab[x][y]==2 && !czy_mina_obok(x, y)) {
        FOR(x2, 1, C)
          FOR(y2, 1, R)
            if (tab[x2][y2]==0)
              tab[x2][y2] = 2;
        bylo = 0;
        rozszerzaj(x, y);
        if (bylo==R*C-M) {
          tab[x][y] = 2;
          throw 0;
        }
      }
}

void probuj(int poz, int min) {
  if (poz==R*C) 
    sprawdz();
  if (min) {
    tab[1+poz%C][1+poz/C] = 1; // mina
    probuj(poz+1, min-1);
  }
  if (min<R*C-poz) {
    tab[1+poz%C][1+poz/C] = 2; // puste
    probuj(poz+1, min);
  }
}

void licz() {
fprintf(stderr, "%d %d %d\n", R, C, M);
  try {
    REP(y, R+2) 
      REP(x, C+2)
        tab[x][y] = -1;
    if (M==R*C-1) {
      FOR(x, 1, C)
        FOR(y, 1, R)
          tab[x][y] = 1;
      tab[1][1] = 2;
      throw 0;
    }
    probuj(0, M);
    printf("Impossible\n");
  }
  catch (...) {
    FOR(y, 1, R) {
      FOR(x, 1, C)
        printf("%c", tab[x][y]==0 ? '.' : tab[x][y]==1 ? '*' : 'c');
      printf("\n");
    }
  }
}

void przelicz() {
  for (R = 1; R<=5; ++R)
    for (C = 1; C<=5; ++C)
      for (M = 0; M<R*C; ++M)
        licz();
}

int main(int argc, char **) {
  if (argc>1)
    przelicz();
  else {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
      scanf("%d%d%d", &R, &C, &M);
      printf("Case #%d:\n", tt+1);
      licz();
    }
  }
}


