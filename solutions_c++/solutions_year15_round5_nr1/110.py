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

void solve(){
  ll N, D;
  cin >> N >> D;
  vector<ll> S(N), M(N);
  ll AS, CS, RS;
  ll AM, CM, RM;
  cin >> S[0] >> AS >> CS >> RS;
  cin >> M[0] >> AM >> CM >> RM;
  REP(i, N - 1){
    S[i + 1] = ((ll)S[i] * AS + CS) % RS;
    M[i + 1] = ((ll)M[i] * AM + CM) % RM;
  }
  // cout <<S << endl;

  vector<vector<int> > G(N);
  REP2(i, 1, N){
    M[i] %= i;
    G[M[i]].push_back(i);
  }
  vector<pair<int, int> > vp;
  REP(i, N) {
    if (abs(S[i] - S[0]) <= D) vp.push_back(make_pair(S[i], i));
  }
  sort(ALL(vp));

  int l = 0;
  int r = 0;
  int res = 0;
  int sum = 0;

  vector<int> alive(N, false);
  // cout << vp << endl;
  
  while (r < vp.size()){
    while (r < vp.size() && abs(vp[l].first - vp[r].first) <= D){
      int x = vp[r].second;
      assert(r < vp.size());
      assert(x < N);
      assert(x == 0 || M[x] < N);
      
      if (alive[x] == 0 && (x == 0 || alive[M[x]] == 1)){

        alive[x] = 1;
        sum++;
        
        queue<int> que;
        que.push(x);

        // cout << G[vp[r].second] << endl;
        while (!que.empty()){
          int v = que.front(); que.pop();
          for (int w : G[v]){
            // cout << v << " " << vp[l].first << " " << S[w] << endl;
            // cout << w << " " << abs(vp[l].first - S[w])  << endl;
            if (alive[w] == 0 && abs(vp[l].first - S[w]) <= D && abs(S[w] - S[0]) <= D && vp[r].first >= S[w] && S[w] >= vp[l].first){
              
              alive[w] = true;
              sum++;
              
              que.push(w);
            }
            
          }
        }
      }
      r++;
    }
    // cout << vp.size() << " " << l << " " << r << endl;
    // cout << alive << " " << sum << endl;
    res = max(res, sum);

    if (alive[vp[l].second] == true){
      alive[vp[l].second] = -1;
      sum--;
    
      queue<int> que;
      que.push(vp[l].second);
      while (!que.empty()){
        int v = que.front(); que.pop();
        for (int w : G[v]){
          if (alive[w] == true){
            alive[w] = -1;
            sum--;
            que.push(w);
          }
        }
      }
    }
    l++;
  }
  cout <<res << endl;
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
