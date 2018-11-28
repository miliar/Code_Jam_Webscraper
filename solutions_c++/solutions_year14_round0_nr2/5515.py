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

//inline LABS(LL a){}

#define FOR(i,n)      for(int i=0;i<(n);i++)
#define FORD(i,n)     for(int i=(n)-1;i>=0;i--)

#define MP make_pair
#define PB push_back

void solve(int tc){
  double C, F, X;
  scanf("%lf %lf %lf ", &C, &F, &X);
  double best = X + 7;
  double rychlost = 2;
  //cas doteraz straveny stavanim farmy
  double nakupu = 0;
  //stacilo by urvat ked to zacne klesat
  FOR(i, (int)(X) + 1){
    best = min(best, nakupu + X/rychlost);
    nakupu += C / rychlost;
    rychlost += F;
    //kupime dalsiu rarmu
  }
  printf("Case #%d: %.12lf\n", tc, best);
}

int main(){
  int TT;
  cin >> TT;
  FOR(tc, TT) solve(tc+1);
  return 0;
}

