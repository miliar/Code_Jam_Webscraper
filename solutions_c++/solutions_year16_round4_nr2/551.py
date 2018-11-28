#include <bits/stdc++.h>

#define REP(i,n) for(int i=0, i##_len=(n); i<i##_len; ++i)
#define ALL(x) (x).begin(),(x).end()

using namespace std;

template <typename T> T &chmin(T &a, const T &b) { return a = min(a, b); }
template <typename T> T &chmax(T &a, const T &b) { return a = max(a, b); }

using ll = long long;
using ld = long double;

const int INF = 1e9;
const ld eps = 1e-9, pi = acos(-1.0);

ld dp(const vector<ld> &p) {
  int n = p.size();
  vector<vector<ld>> d(n + 1, vector<ld>(n / 2 + 1));
  d[0][0] = 1;
  REP(i,n) REP(j,n/2+1) {
    d[i+1][j] += d[i][j] * (1 - p[i]);
    if (j < n/2) d[i+1][j+1] += d[i][j] * p[i];
  }
  return d[n][n/2];
}

ld solve2() {
  int N, K;
  cin >> N >>
 K;
  vector<ld> p(N);
  REP(i,N) cin >> p[i];
  sort(ALL(p));
  // for (ld i: p) cout << i << " "; cout << endl;
  vector<int> perm(N);
  REP(i,K) perm[i] = 1;
  reverse(ALL(perm));
  ld res = 0;
  vector<int> resv;
  do {
    vector<ld> pp;
    REP(i,N) if (perm[i]) pp.push_back(p[i]);
    ld r = dp(pp);
    if (r > res) { res = r; resv = perm; }
  } while (next_permutation(ALL(perm)));
  // for (int i: resv) cout << i << " "; cout << endl;
  return res;
}

ld solve() {
  int N, K;
  cin >> N >> K;
  vector<ld> p(N);
  REP(i,N) cin >> p[i];
  sort(ALL(p));
  ld res = 0;
  for (int i = 0; i <= K; ++i) {
    vector<ld> pp;
    for (int j = 0; j < i; ++j) pp.push_back(p[j]);
    for (int j = 0; j < K-i; ++j) pp.push_back(p[N-j-1]);
    chmax(res, dp(pp));
  }
  return res;
}

int main() {
  cout << setprecision(12) << fixed << boolalpha;
  int T; cin >> T;
  for (int cas = 1; cas <= T; ++cas) {
    cout << "Case #" << cas << ": " << solve() << endl;
  }
  return 0;
}
