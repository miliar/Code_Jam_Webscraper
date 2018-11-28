#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define MOD 1000002013

struct pt {
  long long x, v;
  long long prev;

  pt(long long x, long long v, long long prev) : x(x), v(v), prev(prev) {}

  bool operator<(const pt& o) const {
    if (x != o.x) return x < o.x;
    if (v != o.v) return v > o.v;
    return false;
  }
};

long long div2(long long x) {
  x %= MOD;
  if (x % 2 == 0) return x / 2;
  else return (x + MOD) / 2;
}

long long diff(long long n, long long a, long long b) {
  return div2(((2*n-a-b+1) % MOD) * ((a-b+MOD) % MOD));
}

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    long long n, m; cin >> n >> m;
    long long tot = 0;
    vector<pt> pts;
    for (int i = 0; i < m; i++) {
      long long a, b, p;
      cin >> a >> b >> p;
      // a = 10000LL * i; b = 1000000L * i; p = 1000000000LL;
      pts.push_back(pt(a, p, -1));
      pts.push_back(pt(b, -p, a));
    }
    sort(pts.begin(), pts.end());

    long long res = 0;
    vector<pair<long long, long long> > cur;
    for (int i = 0; i < pts.size(); i++) {
      long long p = pts[i].v;
      if (p > 0) {
        cur.push_back(make_pair(pts[i].x, p));
      } else {
        p = -p;
        while (p > 0) {
          int last = cur.size() - 1;
          if (cur[last].second > p) {
            res += (p * diff(n, pts[i].x - pts[i].prev, pts[i].x - cur[last].first)) % MOD;
            res %= MOD;
            cur[last].second -= p;
            p = 0;
          } else {
            res += (cur[last].second * diff(n, pts[i].x - pts[i].prev, pts[i].x - cur[last].first)) % MOD;
            res %= MOD;
            p -= cur[last].second;
            cur.pop_back();
          }
        }
      }
    }
    cout << "Case #" << c << ": " << res << endl;
  }
  return 0;
}
