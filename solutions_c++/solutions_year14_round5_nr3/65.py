#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <utility>
#include <vector>
using namespace std;

typedef long long ll;
typedef pair<int, int> P;
typedef vector<P> Vp;
typedef vector<int> Vi;
typedef vector<Vi> Mi;
typedef vector<Mi> MMi;
typedef map<int, int> MAP;
typedef vector<char> Vc;

const int INF = 1000000000;

int N;
int M;
Vc act;
Vi id;
MAP mp;
MMi dp;

int fun(int n, int m, int r) {
  if (dp[n][m][r] != -1) return dp[n][m][r];
  
  if (n == N) {
    int q = 0;
    for (int i = 0; (m>>i) != 0; ++i)
      if ((m>>i)&1) ++q;
    return dp[n][m][r] = q + r;
  }
  
  if (id[n] != -1) {
    int b = (m>>id[n])&1;
    if ((act[n] == 'E' and b == 1) or (act[n] == 'L' and b == 0)) return dp[n][m][r] = INF;
    return dp[n][m][r] = fun(n + 1, m^(1<<id[n]), r);
  }
  
  int res = INF;
  
  if (act[n] == 'E' or r > 0) {
    res = min(res, fun(n + 1, m, r + (act[n] == 'E' ? 1 : -1)));
  }
  
  for (int i = 0; i < M; ++i) {
    int b = (m>>i)&1;
    if ((act[n] == 'E' and b == 1) or (act[n] == 'L' and b == 0)) continue;
    res = min(res, fun(n + 1, m^(1<<i), r));
  }
  
  return dp[n][m][r] = res;
}

int main() {
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    cin >> N;
    act = Vc(N);
    id = Vi(N);
    for (int i = 0; i < N; ++i) cin >> act[i] >> id[i];
    mp.clear();
    M = 0;
    for (int i = 0; i < N; ++i) {
      if (id[i] == 0) {
        id[i] = -1;
        continue;
      }
      if (mp.count(id[i]) == 0) mp[id[i]] = M++;
      id[i] = mp[id[i]];
    }
    dp = MMi(N + 1, Mi(1<<M, Vi(2*N + 2, -1)));
    int res = INF;
    for (int m = 0; m < (1<<M); ++m)
      for (int r = 0; r <= N; ++r)
        res = min(res, fun(0, m, r));
    cout << "Case #" << cas << ": ";
    if (res < INF) cout << res << endl;
    else cout << "CRIME TIME" << endl;
  }
}
