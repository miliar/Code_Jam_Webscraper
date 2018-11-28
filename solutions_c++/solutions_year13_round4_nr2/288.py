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
typedef pair<ll, ll> P;
const int INF = 1000 * 1000 * 1000 + 7;
const double EPS = 1e-10;


ll calc1(ll N, ll P){
  ll ub = 1LL << N;
  ll lb = 0;
  while(ub - lb > 1){
    ll mb = (ub + lb) / 2;
    
    ll L = (1LL << N) - mb - 1;
    ll U =  mb;
    // 自分が負けまくる
    // 強い人が勝ちまくる

    int l;
    for(l = 0; l < N; l++){
      if(U == 0) break;         // もう負けられない
      U--;
      assert((U + L) % 2 == 0);
      if(U % 2){
        U = (U - 1) / 2;
        L = (L + 1) / 2;
      }else{
        U /= 2;
        L /= 2;
      }
    }
    // 自分が下位何人か
    
    ll S = 1LL << (N - l);
    if(S + P - 1 >= 1LL << N){
      lb = mb;
    }else{
      ub = mb;
    }
  }
  return lb;
}

ll calc2(ll N, ll P){
  ll ub = 1LL << N;
  ll lb = 0;
  while(ub - lb > 1){
    ll mb = (ub + lb) / 2;

    
    ll L = (1LL << N) - mb - 1;     
    ll U = mb;

    // 自分が勝ちまくる
    // 弱い人が勝ちまくる
    int w;
    for(w = 0; w < N; w++){
      if(L == 0) break;         // もう負けられない
      
      L--;
      assert((U + L) % 2 == 0);

      if(U % 2){
        U = (U + 1) / 2;
        L = (L - 1) / 2;
      }else{
        U /= 2;
        L /= 2;
      }
    }
    // 自分が上位何人か
    
    ll S = 1LL << (N - w);
    if(S <= P){
      lb = mb;
    }else{
      ub = mb;
    }
  }
  return lb;
}

string solve(){
  ll N, P;
  cin >> N >> P;

  ostringstream out;
  out << calc1(N, P) << " " << calc2(N, P);
  
  return out.str();;

}

int main(){
  int T;
  cin >> T;
  REP2(t, 1, T + 1){
    cout << "Case #" << t << ": " << solve() << endl;
  }
  return 0;
}
