#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <cassert>
#include <string>
#include <memory.h>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <map>
#include <cctype>
#include <iomanip>
#include <sstream>
#include <cctype>
#include <fstream>
#include <cmath>
using namespace std;

#define REP2(i, m, n) for(int i = (int)(m); i < (int)(n); i++)
#define REP(i, n) REP2(i, 0, n)
#define ALL(c) (c).begin(), (c).end()
#define ITER(c) __typeof((c).begin())
#define PB(e) push_back(e)
#define FOREACH(i, c) for(ITER(c) i = (c).begin(); i != (c).end(); ++i)
#define MP(a, b) make_pair(a, b)
#define PARITY(n) ((n) & 1)

typedef long long ll;
typedef pair<ll, ll> PL;
const int INF = 1000 * 1000 * 1000 + 7;
const double EPS = 1e-10;
const ll mod = 1000002013;


ll cost(ll D, ll N){
  N %= mod;
  D %= mod;
  return (N + (N - D + 1)) * D / 2 % mod;
}

ll solve(){
  ll N, M;
  cin >> N >> M;

  vector<ll> O(M);
  vector<ll> E(M);
  vector<ll> P(M);
  vector<PL> event;

  ll old = 0;
  
  REP(i, M){
    cin >> E[i] >> O[i] >> P[i];
    old += cost(O[i] - E[i], N) * P[i];
    old %= mod;
    
    event.push_back(PL(E[i], - P[i]));
    event.push_back(PL(O[i], + P[i]));
    
  }
  sort(ALL(event));
  
  
  ll res = 0;
  priority_queue<PL> que;
  
  REP(i, event.size()){
    PL e = event[i];
    ll pos = e.first;
    ll p = e.second;

    if(p > 0){
      while(p > 0){
        
        PL pl = que.top(); que.pop();
        ll c = pl.second;
        ll v = pl.first;
        ll d = min(p, c);
        p -= d;
        c -= d;
        res = (res + d * cost(pos - v, N) % mod) % mod;
        if(c > 0) que.push(PL(v, c));
      }
    }else{
      que.push(PL(pos, -p));
    }
  }
  return (old - res + mod) % mod;
}

int main(){
  int T;
  cin >> T;
  REP2(t, 1, T + 1){
    cout << "Case #" << t << ": " << solve() << endl;
  }
  return 0;
}
