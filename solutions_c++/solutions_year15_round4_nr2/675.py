#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const ll INF = 5000000000;
#define PB push_back
#define sz(a) (a).size()
#define reps(i,n,m) for(int (i)=(n);(i)<(m);++(i))
#define rep(i,n) reps(i,0,n)
ll T;

int main(){
  cin >> T;
  reps(times, 1, T+1) {
    ll n;
    double v,x;
    double rs[110];
    double cs[110];
    cin >> n;
    cin >> v >> x;
    double mn = 1000000;
    double mx = -1999;
    rep(i,n){
      cin>>rs[i]>>cs[i];
      mx = max(mx, cs[i]);
      mn = min(mn, cs[i]);
    }
    if (n == 1) {
      if (x == cs[0]) {
        printf("Case #%d: %.10lf\n", times, v/rs[0]);
      } else {
        printf("Case #%d: %s\n", times, "IMPOSSIBLE");
      }
    } else if (n == 2) {
      int t = mn == cs[0] ? 0 : 1;
      if (mn == x && mx == x) {
        printf("Case #%d: %.10lf\n", times, v / (rs[t]+rs[1]));
      } else if (mn <= x && x <= mx) {
        double a = x - mn;
        double b = mx - x;
        double av = v * a /(a + b);
        double bv = v * b /(a + b);
        printf("Case #%d: %.10lf\n", times, max(bv / rs[t], av / rs[(t+1)%2]));
      } else {
        printf("Case #%d: %s\n", times, "IMPOSSIBLE");
      }
    }
  }

}
