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

set<int> func() {
  int r;
  cin >> r;r--;
  int a[4][4];
  REP(i,4)REP(j,4) {
    cin >> a[i][j];
  }
  set<int> S;
  REP(j,4) S.insert(a[r][j]);
  return S;
}
int main() {
  int T; cin >> T;
  REP(cs,T) {
    set<int> S1 = func();
    set<int> S2 = func();
    int cnt = 0;
    int ans;
    FOR(it, S1) {
      if (S2.count(*it)) {
        ans = *it;
        cnt++;
      }
    }
    printf("Case #%d: ", cs+1);
    if (cnt == 1) {
      cout << ans << endl;
    } else if (cnt > 1) {
      puts("Bad magician!");
    } else {
      puts("Volunteer cheated!");
    }
  }
}
