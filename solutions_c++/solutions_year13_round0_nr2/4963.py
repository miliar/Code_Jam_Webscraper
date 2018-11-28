#include<iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <vector>
#include <cmath>
#include <list>
#include <sstream>
#include <algorithm>

using namespace std;

typedef pair<int,int> PII;
typedef long long LL;
typedef vector<int> VI;
typedef pair<LL,LL> PLL;
typedef vector<pair<int,int> > VPII;
typedef vector<LL> VLL;
typedef vector<vector<int> > VVI;
typedef vector<string> VS;
typedef long double LD;

#define PI 3.14159265358979323
#define EE 2.71828182845
#define EPS 10e-10
#define INF 10000000

inline LL MAX(LL a, LL b){ return a < b ? b : a;}
inline LL MIN(LL a, LL b){ return a < b ? a : b;}

#define FOR(i,n)      for(int i=0;i<(n);i++)
#define FORD(i,n)     for(int i=(n)-1;i>=0;i--)

#define MP make_pair
#define PB push_back

int D[105][150];

void solve(int tt){
  int N,M;
  scanf("%d %d ", &N, &M);
  FOR(i,N){
    FOR(j,M) scanf("%d ", &D[i][j]);
  }

  FOR(i,N)FOR(j,M){

    int mozem = 0;
    int ok = 1;
    FOR(k,M) if (D[i][j] < D[i][k]) ok = 0;
    if (ok == 1) mozem++;

    ok = 1;
    FOR(k,N) if (D[k][j] > D[i][j]) ok = 0;
    if (ok == 1) mozem++;

    if (mozem == 0){
      printf("Case #%d: NO\n", tt+1);
      return;
    }

  }
  printf("Case #%d: YES\n", tt+1);
  return;
}

int main(){
  int TT; 
  scanf("%d ", &TT);
  FOR(tt,TT) solve(tt);
  return 0;
}
