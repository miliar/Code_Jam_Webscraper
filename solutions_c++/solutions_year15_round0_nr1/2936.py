#include <bits/stdc++.h>

#define REP(i, x, n) for(int i = x; i < (int)(n); i++)
#define rep(i, n) REP(i, 0, n)
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define F first
#define S second
#define mp make_pair

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> P;

int main() {
  // ios_base::sync_with_stdio(false);
  int T;
  cin >> T;

  rep(tc, T) {
    int maxS;
    string s;
    cin >> maxS >> s;

    int ans = 0;
    int cnt = 0;
    rep(j, s.size()) {
      if(cnt < j) {
        ans += j - cnt;
        cnt = j;
      }
      cnt += s[j] - '0';
    }
    
    cout << "Case #" << tc + 1 << ": " << ans << endl;
  }
  return 0;
}
