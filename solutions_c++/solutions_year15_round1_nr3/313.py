// {{{ template
#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<string> vs;
typedef vector<long long> vll;
typedef vector<pii> vpii;
// }}}

typedef pii Point;

Point operator-(const Point &p, const Point &q) {
  return Point(p.first - q.first, p.second - q.second);
}

template<class T> inline int signum(const T &x) {
  return x < 0 ? -1 : x > 0;
}

int cross(const Point &p, const Point &q) { //vektor [-1..1]
  return signum(1LL * p.first * q.second - 1LL * q.first * p.second);
}

bool ccw(const Point &p, const Point &q, const Point &r) {
  return cross(q - p, r - p) > 0;
}

vector<Point> convexHull(vector<Point> &a) {
  if (a.size() <= 3) {
    return a;
  }
  sort(begin(a), end(a));
  int n = a.size();
  vector<Point> res(2 * n);
  int size = 0;
  for (int i = 0; i < n; i++) {
    while (size >= 2 && ccw(res[size - 2], res[size - 1], a[i])) size--;
    res[size++] = a[i];
  }
  int save = size + 1;
  for (int i = n - 1; i >= 0; i--) {
    while (size >= save && ccw(res[size - 2], res[size - 1], a[i])) size--;
    res[size++] = a[i];
  }
  res.resize(size);
  assert(size == 0 || size == 1 || res.back() == res[0]);
  return res;
}

int main() {
  cin.sync_with_stdio(0); cin.tie(0);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int n;
    cin >> n;
    map<Point, int> id;
    vector<Point> a(n);
    for (int i = 0; i < n; i++) {
      cin >> a[i].first >> a[i].second;
      id[a[i]] = i;
    }
    vi ans(n, INT_MAX);
    for (int mask = 0; mask < (1 << n); mask++) {
      vector<Point> b;
      for (int i = 0; i < n; i++) {
        if (mask & (1 << i)) {
          b.push_back(a[i]);
        }
      }
      b = convexHull(b);
      int cnt = __builtin_popcount(mask);
      for (auto it : b) {
        ans[id[it]] = min(ans[id[it]], n - cnt);
      }
    }
    cout << "Case #" << t << ":\n";
    for (auto i : ans) {
      cout << i << endl;
    }
  }
  return 0;
}

