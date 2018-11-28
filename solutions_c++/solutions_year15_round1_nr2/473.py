

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

#define rep(i,n) for (int i=0; i<(n); i++)
#define repf(i,a,b) for (int i=(a); i<=(b); i++)
#define repb(i,a,b) for (int i=(a); i>=(b); i--)

#define D(x) cout << #x << " = " << x << endl;
#define endl '\n'

using namespace std;

typedef long long int LL;

template<class T>
ostream& operator<<(ostream& a, const vector<T>& v) {
    a << "{";
    if (v.size()>0) a << v[0];
    for (int i=1; i<v.size(); i++) a << ", " << v[i];
    a << "}";
    return a;
}

int main() {
    cin.sync_with_stdio(false);
    cout.sync_with_stdio(false);
    cin.tie(NULL);
    int TC, B, N;
    int ans;
    cin >> TC;
    for (int tc=1; tc<=TC; tc++) {
      cin >> B >> N;
      vector<LL> M(B);
      rep(i,B) cin >> M[i];
      ans=-1;
      for (int barber=0; barber < B; barber++) {
        LL left=0, right=N;
        while (left <= right) {
          LL xk = (left+right) / 2;
          LL tmp_ans = 0;
          LL time = M[barber]*xk;
          for (int i=0; i<=barber; i++) {
            tmp_ans += 1LL + (time / M[i]);
          }
          for (int i=barber+1; i<B; i++) {
            tmp_ans += 1LL + ((time - 1LL) / M[i]);
          }
          if (tmp_ans == N) {
            ans = barber+1;
            break;
          } else if (N < tmp_ans) {
            right = xk-1;
          } else {
            left = xk+1;
          }
        }
        if (ans != -1) break;
      }
      cout << "Case #" << tc << ": " << ans << endl;
    }
}
