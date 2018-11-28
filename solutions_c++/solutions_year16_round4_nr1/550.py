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

string solve(int n, int r, int c, int p) {
  vector<string> R(r, "R");
  vector<string> C(c, "S");
  vector<string> P(p, "P");
  REP(i,n) {
    // cout << r << " " << c << " " << p << endl;
    int s = (r + c + p) / 2;
    int nr = s - p;
    int nc = s - r;
    int np = s - c;
    if (nr < 0 || nc < 0 || np < 0) {
      return "IMPOSSIBLE";
    }
    r = nr; c = nc; p = np;
    vector<string> NR, NC, NP;
    int ir = 0, ic = 0, ip = 0;
    while (nr > 0 || nc > 0 || np > 0) {
      // cout << nr << " " << nc << " " << np << " ";
      // cout << ir << " " << ic << " " << ip << endl;
      tuple<string,int,int,int> mi("xx", 0, 0, 0);
      if (nr > 0) {
        chmin(mi, make_tuple(R[ir] + C[ic], 1, 1, 0));
        chmin(mi, make_tuple(C[ic] + R[ir], 1, 1, 0));
      }
      if (np > 0) {
        chmin(mi, make_tuple(R[ir] + P[ip], 1, 0, 1));
        chmin(mi, make_tuple(P[ip] + R[ir], 1, 0, 1));
      }
      if (nc > 0) {
        chmin(mi, make_tuple(C[ic] + P[ip], 0, 1, 1));
        chmin(mi, make_tuple(P[ip] + C[ic], 0, 1, 1));
      }
      // cout << "OK" << endl;
      string str;
      int dr, dc, dp;
      tie(str, dr, dc, dp) = mi;
      ir += dr; ic += dc; ip += dp;
      nr -= min(dr, dc);
      np -= min(dr, dp);
      nc -= min(dc, dp);
      if (dp == 0) NR.push_back(str);
      if (dr == 0) NC.push_back(str);
      if (dc == 0) NP.push_back(str);
    }
    R = move(NR); C = move(NC); P = move(NP);
    // for (string s: R) cout << s << " "; cout << endl;
    // for (string s: C) cout << s << " "; cout << endl;
    // for (string s: P) cout << s << " "; cout << endl;
    sort(ALL(R));
    sort(ALL(C));
    sort(ALL(P));
  }
  if (r > 0) return R[0];
  if (c > 0) return C[0];
  if (p > 0) return P[0];
  return "";
}

int main() {
  cout << setprecision(12) << fixed << boolalpha;
  int T; cin >> T;
  for (int cas = 1; cas <= T; ++cas) {
    int n, r, c, p;
    cin >> n >> r >> p >> c;
    cout << "Case #" << cas << ": " << solve(n, r, c, p) << endl;
  }
  return 0;
}
