#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <stack>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
#define REP(i,a,n) for(int i=(a); i<(int)(n); i++)
#define rep(i,n) REP(i,0,n)
#define FOR(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define ALLOF(c) (c).begin(), (c).end()
typedef long long ll;

ll solve(ll N){
  if(N == 0) return -1;
  ll cnt = 1;
  vector<int> memo(10, 0);
  while(true){
    ll prod = cnt * N;
    while(prod>0){
      memo[prod%10] = 1;
      prod /= 10;
    }
    bool flg = true;
    rep(i,10) if(memo[i] == 0){ flg = false; break; }
    if(flg) break;
    cnt++;
  }
  return cnt * N;
}

int check(){
  rep(i,1000001){
    cout << solve(i) << endl;
  }
  return 0;
}

int main(){
  ios::sync_with_stdio(false);
  int T;
  cin >> T;
  rep(t,T){
    ll N;
    cin >> N;
    ll ret = solve(N);
    cout << "Case #" << t+1 << ": ";
    if(ret < 0) cout << "INSOMNIA";
    else cout << ret;
    cout << endl;
  }
  
  return 0;
}

