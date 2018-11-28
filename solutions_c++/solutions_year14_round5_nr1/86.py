#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <vector>
using namespace std;

#define REP2(i, m, n) for(int i = (int)(m); i < (int)(n); i++)
#define REP(i, n) REP2(i, 0, n)
#define ALL(c) (c).begin(), (c).end()
#define FOREACH(i, c) for(auto i = (c).begin(); i != (c).end(); ++i)
#define BIT(n, m) (((n) >> (m)) & 1)

typedef long long ll;

const ll inf = 1e15;
const ll mod = 1000 * 1000 * 1000 + 7;
const double eps = 1e-9;

void solve(){
  ll p, q, r, s, N;
  cin >> N >> p >> q >> r >> s;
  
  vector<ll> A(N);
  vector<ll> S(N + 1, 0);
  
  REP(i, N){
    A[i] = (i * p + q) % r + s;
  }

  S[0] = 0;
  REP(i, N){
    S[i + 1] = S[i] + A[i];
  }
  
  ll ub = 1LL << 60;
  ll lb = 0;
  while (ub - lb > 1){
    ll mb = (ub + lb) / 2;
    ll X = 0;
    REP(i, 3){
      ll Y = mb + X;
      int idx = upper_bound(ALL(S), Y) - S.begin() - 1;
      X = S[idx];
    }

    // cout << S[N] << " " << X << endl;
    if (X == S[N]){
      ub = mb;
    } else {
      lb = mb;
    }
  }
  
  cout << fixed << setprecision(20) << 1 - (double)ub / S[N] << endl;
}

int main(){
  int T;
  cin >> T;
  REP(t, T){
    cout << "Case #" << t + 1 << ": ";
    solve();
  }
  return 0;
}
