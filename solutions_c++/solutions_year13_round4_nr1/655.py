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

#define MOD 1000002013

LL kolko(LL stanic, LL N){
  LL res = N;
  res *= stanic;
  res -= (stanic*(stanic-1))/2;
  res %= MOD;
  return res;
}

priority_queue<PII> Q;
VPII events;


void solve(int test_case){
  events.resize(0);
  while(!Q.empty()) Q.pop();

  int N,M;
  LL povodna = 0, nova = 0;
  
  scanf("%d %d ", &N, &M);

  FOR(i,M){
    int x,y,z;
    scanf("%d %d %d ", &x, &y, &z);
    povodna += z * kolko(y-x, N);
    povodna %= MOD;
    events.PB(MP(x,-z));
    events.PB(MP(y,z));
  }

//  cout << povodna << endl;

  sort(events.begin(), events.end());

  FOR(i,events.size()){
    PII p = events[i];

    if (p.second < 0) Q.push( MP(p.first, -p.second) );
    else{
      int este = p.second;
      while(este > 0){
        PII deti = Q.top();
        Q.pop();
        if (deti.second < este){
          nova += deti.second * kolko(p.first - deti.first, N);
          nova %= MOD;
          este -= deti.second;
        }else{
          nova += este * kolko(p.first - deti.first, N);
          nova %= MOD;
          Q.push( MP(deti.first, deti.second - este));
          este = 0;
        }
      }
    }

//    cout << "po evente " << i << ": " << nova << endl;
  }

  povodna += MOD;
  printf("Case #%d: %lld\n", test_case, (povodna - nova) % MOD);
}

int main(){

//  cout << kolko(6,10) << endl;

  int TT;
  scanf("%d ", &TT);
  FOR(tt,TT) solve(tt+1);
  return 0;
}
