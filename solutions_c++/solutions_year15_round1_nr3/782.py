#include <algorithm>
#include <cmath>
#include <climits>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <tuple>
using namespace std;

typedef long long int64;
//typedef __int128_t int128;
typedef vector<int> veci;
typedef vector<string> vecs;

#define VAR(a, b) __typeof(b) a=(b)
#define FOREACH(it, c) for (VAR(it, (c).begin()); it != (c).end(); ++it)
#define TRACE(x) cout << #x << endl
#define DEBUG(x) cout << #x " = " << (x) << endl
#define DEBUGA(a, n) VAR(__p, a); cout << #a " = {"; for (int __i = 0; __i < n; ++__i, ++__p) cout << (__i == 0 ? "" : ", ") << *(__p); cout << "}" << endl
#define CLR(a, val) memset(a, val, sizeof(a))

template<class T1, class T2> ostream& operator << (ostream &o, const pair<T1, T2> &p)
{
  return o << "(" << p.first << ", " << p.second << ")";
}

template<class T1, class T2, class T3> ostream& operator << (ostream &o, const tuple<T1, T2, T3> &t)
{
  return o << "(" << get<0>(t) << ", " << get<1>(t) << ", " << get<2>(t) << ")";
}

template<class T1, class T2, class T3, class T4> ostream& operator << (ostream &o, const tuple<T1, T2, T3, T4> &t)
{
  return o << "(" << get<0>(t) << ", " << get<1>(t) << ", " << get<2>(t) << ", " << get<3>(t) << ")";
}

template<class T> ostream& operator << (ostream &o, const vector<T> &v)
{
  o << '{';
  FOREACH(it, v) o << (it == v.begin() ? "" : ", ") << *it;
  return o << '}';
}

template <class T> struct point2
{
  T x, y, val;
  point2(T x=0, T y=0) : x(x), y(y) {}

  point2 operator +  (const point2 &p) const { return point2(x + p.x, y + p.y); }
  point2 operator -  (const point2 &p) const { return point2(x - p.x, y - p.y); }
  point2 operator *  (const T& s)      const { return point2(x*s, y*s); }
  point2 operator /  (const T& s)      const { return point2(x/s, y/s); }
  T      operator *  (const point2 &p) const { return x*p.x + y*p.y; }
  T      operator ^  (const point2 &p) const { return x*p.y - y*p.x; }
  bool   operator == (const point2 &p) const { return x == p.x && y == p.y; }

  T magsq() const { return x*x + y*y; }
  double mag() const { return sqrt(magsq()); }
  point2<double> dir() const { return point2<double>(x, y) / mag(); }

  struct by_x { bool operator() (const point2 &p1, const point2 &p2) const { return p1.x == p2.x ? (p1.y < p2.y) : (p1.x < p2.x); } };
  struct by_y { bool operator() (const point2 &p1, const point2 &p2) const { return p1.y == p2.y ? (p1.x < p2.x) : (p1.y < p2.y); } };
  friend ostream& operator << (ostream &o, const point2 &p) { return o << "(" << p.x << ", " << p.y << ")"; }
};

template <class T> vector<point2<T>> hull(vector<point2<T>> &pts)
{
  if (pts.size() <= 2)
    return pts;

  int n = pts.size(), k = 0;
  vector< point2<T> > H(2*n);
  sort(pts.begin(), pts.end(), typename point2<T>::by_x());

  for (int i = 0; i < n; i++) {
    while (k >= 2 && ((H[k-1] - H[k-2]) ^ (pts[i] - H[k-2])) < 0) k--;
    H[k++] = pts[i];
  }
  for (int i = n-2, t = k+1; i >= 0; i--) {
    while (k >= t && ((H[k-1] - H[k-2]) ^ (pts[i] - H[k-2])) < 0) k--;
    H[k++] = pts[i]; }

  H.resize(k);
  return H;
}

void run(int tc)
{
  int N;
  cin >> N;
  vector<point2<int64>> pts(N);
  for (int i = 0; i < N; i++) {
    cin >> pts[i].x >> pts[i].y;
    pts[i].val = i;
  }

  vector<int> res(N, -1);
  const int S = (1 << N) - 1;
  for (int s = 0; s < S; s++) {
    vector<point2<int64>> trees;
    int ncuts = 0;
    for (int i = 0; i < N; i++) {
      if (s & (1 << i))
        ncuts++;
      else
        trees.push_back(pts[i]);
    }

    vector<point2<int64>> h = hull(trees);
    for (int i = 0; i < h.size(); i++) {
      int pos = h[i].val;
      if (res[pos] == -1 || ncuts < res[pos])
        res[pos] = ncuts;
    }
  }

  cout << "Case #" << (tc + 1) << ": " << endl;
  for (int i = 0; i < N; i++)
    cout << res[i] << endl;
}

int main()
{
  int T = 0, tc = 0;
  for (cin >> T; tc < T; tc++) run(tc);
  return 0;
}
