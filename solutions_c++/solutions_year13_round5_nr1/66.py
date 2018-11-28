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
const ll INF = 1LL << 55;
const double EPS = 1e-10;

ll use_money(ll x, int num, const vector<ll> &bets){
  ll ans = 0;
  
  REP(i, num){
    if(bets[i] > x) return INF;
    ans += x - bets[i];
  }

  REP2(i, num, bets.size()){
    if(bets[i] < x + 1){
      ans += x + 1 - bets[i];
    }
  }
  return ans;
}

double solve(){
  ll B, N;
  cin >> B >> N;
  
  vector<ll> bets(37, 0);
  REP(i, N) cin >> bets[i];
  sort(ALL(bets));

  double ans = 0;

  REP(i, 36){
    ll ub = INF;
    ll lb = bets[0];

    while(ub - lb > 1){
      ll mb = (ub + lb) / 2;
      if(use_money(mb, i + 1, bets) <= B){
        lb = mb;
      }else{
        ub = mb;
      }
    }

    ll um = use_money(lb, i + 1, bets);
    if(um > B) continue;
    
    double e = 0;
    REP(j, i + 1){
      e += lb - bets[j];
    }
    ans = max(ans, e * 36 / (i + 1) - um);
  }
  
  return ans;
}

int main(){
  int T;
  cin >> T;
  REP2(t, 1, T + 1){
    cout << "Case #" << t << ": " << fixed << setprecision(20) << solve() << endl;
  }
  return 0;
}
