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


int C[2000];

void dfs(int sum, int pos, int M, int N,
         const vector<string> &S,
         vector<string> B[])
{
  if (pos == M){
    bool ok = true;
    for (int i = 0; i < N; i++) if (B[i].empty()) ok = false;
    if (ok) C[sum + N]++;
  } else {
    const auto &s = S[pos];
    
    for (int i = 0; i < N; i++){
      int best_cost = s.size();
      for (auto &t : B[i]){
        int cost = s.size();
        REP(k, min(s.size(), t.size())){
          if (s[k] == t[k]){
            cost--;
          } else {
            break;
          }
        }
        best_cost = min(best_cost, cost);
      }
      
      B[i].push_back(s);
      dfs(sum + best_cost, pos + 1, M, N, S, B);
      B[i].pop_back();
    }
  }
}

void solve(){
  int M, N;
  cin >> M >> N;

  vector<string> S(M);
  vector<string> B[N];
  
  REP(i, M) cin >> S[i];
  memset(C, 0, sizeof(C));

  dfs(0, 0, M, N, S, B);

  int len = 0;
  int res = 0;
  for (int i = 0; i < 2000; i++){
    if (C[i] > 0){
      len = i;
      res = C[i];
    }
  }
  cout << len << " " << res << endl;
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
