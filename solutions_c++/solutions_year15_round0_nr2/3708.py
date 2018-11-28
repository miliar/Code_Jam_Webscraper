#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cassert>
#include <cstdlib>

using namespace std;

#define ri(X) scanf("%d", &(X))
#define pi(X) printf("%d", (X))
#define mp(X,Y) make_pair(X,Y)
#define pb(X) push_back(X)
#define lint long long
#define pii pair<int,int>
#define inf 1e9
#define linf 1e18
#define X first
#define Y second
#define all(X) (X).begin(),(X).end()
#define uni(X) X.erase(unique(X.begin(), X.end()), X.end());

int t, D, a[1005], dp[1005][1005];

int solve(int ind, int big) {
  if (ind >= D) return big;
  if (dp[ind][big] != -1) return dp[ind][big];
  int r = inf, sq = a[ind]/2+1;
  for (int i = 1; i <= sq; i++) {
    r = min(r, i-1 + solve(ind+1, max(big, a[ind]/i + (a[ind]%i>0 ? 1 : 0))));
  }
  return dp[ind][big] = r;
}

int main(){
  ri(t);
  for (int te = 1; te <= t; te++) {
    memset(dp, -1, sizeof dp);
    ri(D);
    for (int i = 0; i < D; i++) ri(a[i]);
    sort(a, a+D, greater<int>());
    cout << "Case #" << te << ": " << solve(0, 0) << endl;
  }
  
  return 0;
}
