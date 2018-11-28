#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <functional>
#include <cmath>
#include <set>
#include <map>
#include <queue>
using namespace std;

#define rep(i, m, n) for(int i = m; i < n; i++)
#define repr(i, n, m) for(int i = n; i >= m; i--)
#define rep1(i, x) for(int i = 0; i < (int)(x).size(); i++)
#define mkp(v,x,y) for(int i=0;i<(int)(x).size();i++)v.push_back(make_pair(x[i],y[i]))
#define pb push_back
#define mp make_pair
#define si(x) ((int)(x).size())
#define al(x) x.begin(), x.end()
#define x first
#define y second

typedef vector<int> VI;
typedef long long LL;
typedef pair<int, int> PII;

const int INF = 1000000007;
VI cakes;

int dp[1001][1010];

int calc(int index, int m){
  if(index >= si(cakes)) return m;
  int ans = dp[index][m];
  if(ans < INF) return ans;
  rep(i, 1, cakes[index]+1){
    int mx = ceil(cakes[index] / (double)i);
    ans = min(ans, i-1 + calc(index+1, max(m, mx)));
  }
  dp[index][m] = ans;
  return ans;
}

int main(){
  int T; cin >> T;
  rep(case_loop, 1, T+1){
    int D, tmp; cin >> D;
    cakes.clear();
    rep(i, 0, 1001) rep(j, 0, 1010) dp[i][j] = INF;
    rep(i, 0, D){
      cin >> tmp;
      cakes.pb(tmp);
    }
    sort(al(cakes), greater<int>());
    int ans = INF;
    rep(i, 1, cakes[0]+1){
      int mx = ceil(cakes[0] / (double)i);
      ans = min(ans, i-1 + calc(1, mx));
    }
    printf("Case #%d: %d\n", case_loop, ans);
  }
  return 0;
}
