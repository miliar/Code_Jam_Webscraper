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

LL could(LL N, LL P){
  LL kolko_horsich = 0;
  //musi postupit cez i prvych kol
  FOR(i,N){
    LL ostalo = (1LL << (N-i));
    if (P >= ostalo) break;
    kolko_horsich += (1+i);
  }
  return (1LL<<N) - kolko_horsich - 1;
}

LL guaranteed(LL N, LL P){
  LL kolko_lepsich = 0;
  LL este_cena = P;
  FOR(i,N){
    kolko_lepsich += (1+i);
    este_cena -= (1LL<<(N-i-1));
    if (este_cena <= 0) break;
  }
  return kolko_lepsich-1;
}

int NP[1024],P[1024];

void turnajuj(int od, int po, int kol){
  if (kol == 0) return;

//  int kolko = (1<<kol)/2;
  int delim = (od+po)/2;

  int horei = od;
  int dolei = delim+1;

  for(int i = od; i <= po; i+=2){
    if (P[i] > P[i+1]){
      NP[horei] = P[i+1];
      NP[dolei] = P[i];
    }else{
      NP[horei] = P[i];
      NP[dolei] = P[i+1];
    }
    horei++;
    dolei++;
  }

  for(int i = od; i <= po; i++) P[i] = NP[i];
  turnajuj(od, delim, kol-1);
  turnajuj(delim+1,po, kol-1);
}

void solve(int test_case){
  LL N,PP;
  cin >> N >> PP;

  FOR(i,(1<<N)) P[i] = i;
  turnajuj(0,(1<<N)-1, N);

  int najhorsi = 0;
  int najlepsi = (1<<N)-1;
  FOR(i,PP) if (P[i] > najhorsi) najhorsi = P[i];
  for(int i=PP; i < (1<<N); i++) if (najlepsi > P[i]) najlepsi = P[i];

//  FOR(i,(1<<N)) printf("%d ", P[i]);
//  printf("\n");
//

//  cou/

  if (PP == (1<<N)) najlepsi = (1<<N);
  cout << "Case #" << test_case << ": " << najlepsi-1 << " " << najhorsi << endl;

}

int main(){
  int TT;
  cin >> TT;
  FOR(tt,TT) solve(tt+1);
  return 0;
}
