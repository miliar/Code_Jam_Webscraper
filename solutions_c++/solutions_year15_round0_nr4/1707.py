#include <vector>
#include <list>
#include <map>
#include <set>

#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <assert.h>

#define INF 1023123123
#define EPS 1e-11
#define LSOne(S) (S & (-S))

#define FORN(X,Y) for (int (X) = 0;(X) < (Y);++(X))
#define FORB(X,Y) for (int (X) = (Y);(X) >= 0;--(X))
#define REP(X,Y,Z) for (int (X) = (Y);(X) < (Z);++(X))
#define REPB(X,Y,Z) for (int (X) = (Y);(X) >= (Z);--(X))

#define SZ(Z) ((int)(Z).size())
#define ALL(W) (W).begin(), (W).end()
#define PB push_back

#define MP make_pair
#define A first
#define B second

#define FORIT(X,Y) for(typeof((Y).begin()) X = (Y).begin();X!=(Y).end();X++)

using namespace std;

typedef long long ll;
typedef double db;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

vi pset;
vi cset;
int ndisjoint;
void initSet(int N) { cset = vi(N); pset.assign(N, 0); ndisjoint = N; for (int i = 0; i < N; i++) { pset[i] = i; cset[i] = 1; } }
int findSet(int i) { return pset[i] == i ? i : pset[i] = (findSet(pset[i])); }
bool isSameSet(int i, int j) { return findSet(i) == findSet(j); }
void unionSet(int i, int j) { int pi = findSet(i); int pj = findSet(j); if (pi != pj) { pset[pi] = pj; ndisjoint--; cset[pj] += cset[pi]; } }
int numDisjointSets() { return ndisjoint; }
int sizeOfSet(int i) { return cset[findSet(i)]; }


int main() {

   int ntc;
   cin >> ntc;
   FORN(kk, ntc)
   {
      int X, R, C;
      cin >> X >> R >> C;
      bool fill_possible = true;
      int size = R*C;
      if (size % X != 0)
         fill_possible = false;
      if (fill_possible)
      {
         int x, y;
         if (X % 2 == 1)
         {
            x = y = X / 2 + 1;
         }
         else
         {
            x = X / 2 + 1;
            y = X / 2;
         }
         if (max(x, y) > max(R, C) || min(x, y) > min(R, C))
            fill_possible = false;
      }
      if (fill_possible)
      {
         if (X > max(R, C))
            fill_possible = false;
      }
      if (X == 4 && max(R, C) == 4 && min(R, C) == 2)
         fill_possible = false;

      //printf("X: %d R: %d C: %d\n", X, R, C);
      printf("Case #%d: %s\n", kk + 1, (fill_possible ? "GABRIEL" : "RICHARD"));
   }
   return 0;
}
