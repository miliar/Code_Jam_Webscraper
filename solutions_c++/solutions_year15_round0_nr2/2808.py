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
    int D;
    cin >> D;
    vector<int> P(D);
    rep(i, D) cin >> P[i];
    
    int ans = 10000;

    REP(i, 1, 1001) {
      int cnt = i;
      rep(j, D) cnt += P[j] / i + (P[j] % i ? 0 : -1);
      ans = min(ans, cnt);
    }
    
    cout << "Case #" << tc + 1 << ": " << ans << endl;
  }
  return 0;
}

// int ans;

// void rec(vector<int> P, int t) {
//   if(t > ans) return;
  
//   sort(rall(P));

//   ans = min(ans, t + P[0]);

//   REP(i, 1, P[0] / 2 + 1) {
//     vector<int> p = P;
//     p[0] -= i;
//     p.push_back(i);
//     rec(p, t + 1);
//   }
// }

// int main() {
//   // ios_base::sync_with_stdio(false);
//   int T;
//   cin >> T;

//   rep(tc, T) {
//     int D;
//     cin >> D;
//     vector<int> P(D);
//     rep(i, D) cin >> P[i];

//     ans = 100000;
//     rec(P, 0);
    
//     cout << "Case #" << tc + 1 << ": " << ans << endl;
//   }
//   return 0;
// }
