

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

pair<LL,LL> solve(const vector<LL>& X) {
  LL ans1=0, ans2=0, rate=0;
  for (int i=0; i<(X.size()-1); i++) {
    ans1 += max(X[i] - X[i+1], 0LL);
    rate = max(X[i] - X[i+1], rate);
  }
  for (int i=0; i<(X.size()-1); i++) {
    ans2 += min(rate,X[i]);
  }
  return make_pair(ans1, ans2);
}

int main() {
    cin.sync_with_stdio(false);
    cout.sync_with_stdio(false);
    cin.tie(NULL);
    int TC,N;
    cin >> TC;
    for (int tc=1; tc<=TC; tc++) {
      cin >> N;
      vector<LL> states(N);
      rep(i,N) cin >> states[i];
      pair<LL,LL> ans = solve(states);
      cout << "Case #" << tc << ": " << ans.first << " " << ans.second << endl;
    }
}
