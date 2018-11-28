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

template <typename S, typename T> ostream &operator<<(ostream &out, const pair<S, T> &p) {
  out << "(" << p.first << ", " << p.second << ")";
  return out;
}

template <typename T> ostream &operator<<(ostream &out, const vector<T> &v) {
  out << "[";
  REP(i, v.size()){
    if (i > 0) out << ", ";
    out << v[i];
  }
  out << "]";
  return out;
}

typedef long long ll;

const ll inf = 1e15;
const ll mod = 1000 * 1000 * 1000 + 7;
const double eps = 1e-9;

const int NMAX = 300;
double memo[NMAX][NMAX];
vector<double> P;

double rec(int pos, int n, int a){
  int b = pos - a;
  if (pos == n){
    return a == b ? 1 : 0;
  } else if (memo[pos][a] > -eps){
    return memo[pos][a];
  } else {
    double &res = memo[pos][a] = 0;
    res +=      P[pos]  * rec(pos + 1, n, a + 1);
    res += (1 - P[pos]) * rec(pos + 1, n, a + 0);
    return res;
  }
}

void solve(){
  int N, K;
  cin >> N >> K;
  vector<double> ps(N);
  REP(i, N) cin >> ps[i];
  sort(ALL(ps));

  double best = 0;
  vector<double> best_ps;
  REP(i, K + 1){
    // REP(mask, 1 << N){
    vector<double> ps_;
    // REP(i, N) if (mask & (1 << i)) ps_.push_back(ps[i]);
    REP(j, i) ps_.push_back(ps[j]);
    REP(j, K - i) ps_.push_back(ps[N - 1 - j]);
    
    if (int(ps_.size()) == K){
      P = ps_;
      // danger!!!!!!!!
      fill(&memo[0][0], &memo[0][0] + NMAX * NMAX, -1);
      double prob = rec(0, K, 0);
      // cout << prob << " " << ps_ << endl;
      if (prob > best){
        best = prob;
        best_ps = P;
      }
    }
  }
  cout << fixed << setprecision(10) << best << endl;
  // cout << best_ps << endl;
}
 
int main(){
  int T;
  cin >> T;
  REP(t, T){
    printf("Case #%d: ", t + 1);
    solve();
  }
  return 0;
}
