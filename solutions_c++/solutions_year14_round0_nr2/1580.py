#include <bits/stdc++.h>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)n;++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()
#define chmax(a,b) (a<(b)?(a=b,1):0)
#define chmin(a,b) (a>(b)?(a=b,1):0)
#define valid(y,x,h,w) (0<=y&&y<h&&0<=x&&x<w)
const int INF = 1<<29;
const double EPS = 1e-8;
const double PI = acos(-1);
typedef pair<int,int> pii;
typedef long long ll;

double dp[1000001];

int main() {
  int T; cin >> T;
  REP(cs,T) {
    double C,F,X;
    cin >> C >> F >> X;

    double speed = 2;
    dp[0] = 0;
    double ans = 1e100;
    REP(i,1000000) {
      if (ans < dp[i]) break;
      dp[i+1] = dp[i] + C/speed;
      chmin(ans, dp[i]+X/speed);
      speed += F;
    }
    
    printf("Case #%d: %.10f\n", cs+1, ans);
  }

}
