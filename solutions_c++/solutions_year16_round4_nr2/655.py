#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <complex>
#include <ctime>
#include <cassert>
#include <functional>

using namespace std;

typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define REP(i,s,t) for(int i=(s);i<(t);i++)
#define FILL(x,v) memset(x,v,sizeof(x))

const int INF = (int)1E9;
#define MAXN 205

int N, K;
double P[MAXN], A[MAXN], dp[20][20];
double solve() {
  FILL(dp, 0);
  dp[0][0] = 1.0;
  REP(i,1,K+1) {
    REP(v,0,K+1) {
      dp[i][v+1] += dp[i-1][v] * A[i];
      dp[i][v] += dp[i-1][v] * (1 - A[i]);
    }
  }
  return dp[K][K/2];
}
int main() {
  freopen("input", "r", stdin);
  //freopen("output", "w", stdout);
  int cs;
  cin >> cs;
  REP(csn, 1, cs + 1) {
    printf("Case #%d: ", csn);
    //cerr << csn << endl;
    cin >> N >> K;
    int sel[20] = {};
    REP(i,0,K) sel[i] = 1;
    sort(sel, sel+N);
    REP(i,0,N) cin >> P[i];
    double ans = 0;
    do {
      int M = 0;
      REP(i,0,N) {
        if (sel[i]) A[++M] = P[i];
      }
      double sol = solve();
      ans = max(ans, sol);
    } while (next_permutation(sel, sel+N));
    printf("%.9f\n", ans);
  }
  return 0;
}
