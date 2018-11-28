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

int solve1(vector<double> av, vector<double> bv) {
  deque<double> a,b;
  FOR(it, av) a.push_back(*it);
  FOR(it, bv) b.push_back(*it);
  int res = 0;
  while(a.size()) {
    if (a.back() > b.back()) {
      res++;
      a.pop_back();
      b.pop_back();
    } else {
      a.pop_front();
      b.pop_back();
    }
  }
  return res;
}

int solve2(vector<double> av, vector<double> bv) {
  int res = 0;
  REP(i,av.size()) {
    bool ok = 0;
    REP(j,bv.size()) {
      if (bv[j] != -1) {
        if (bv[j] > av[i]) {
          bv[j] = -1;
          ok = 1;
          break;
        }
      }
    }
    if (!ok) res++;
  }
  return res;
}

int main() {
  int T; cin >> T;
  REP(cs,T) {
    int n;
    cin >> n;
    vector<double> a(n);
    vector<double> b(n);
    REP(i,n) cin >> a[i];
    REP(i,n) cin >> b[i];
    sort(ALL(a));
    sort(ALL(b));
    // REP(i,n) cout << a[i] << " "; cout << endl;
    // REP(i,n) cout << b[i] << " "; cout << endl;
    int ans1 = solve1(a,b);
    int ans2 = solve2(a,b);
    printf("Case #%d: %d %d\n", cs+1, ans1, ans2);
  }
}
