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

void run(int tc)
{
  int T[5][5] = {
    { 0, 0,  0,  0,  0 },
    { 0, 1,  2,  3,  4 },
    { 0, 2, -1,  4, -3 },
    { 0, 3, -4, -1,  2 },
    { 0, 4,  3, -2, -1 },
  };

  int64 L, X;
  cin >> L >> X;
  string s;
  cin >> s;

  int64 N = L * X;
  string ijk = s;
  for (int i = 0; i < X; i++)
    ijk += s;

  vector<int64> left(N);
  left[0] = ijk[0] - 'i' + 2;
  for (int i = 1; i < N; i++) {
    int val = ijk[i] - 'i' + 2;
    left[i] = T[abs(left[i - 1])][val];
    if (left[i - 1] < 0) left[i] = -left[i];
  }

  vector<int64> right(N);
  right[N-1] = ijk[N-1] - 'i' + 2;
  for (int i = N-2; i >= 0; i--) {
    int val = ijk[i] - 'i' + 2;
    right[i] = T[val][abs(right[i + 1])];
    if (right[i + 1] < 0) right[i] = -right[i];
  }

  cout << "Case #" << (tc + 1) << ": ";
  for (int i = 0; i < N; i++) {
    if (left[i] != 2) continue;

    for (int j = i + 2; j < N; j++) {
      if (right[j] != 4) continue;

      int m = T[abs(left[i])][3];
      if (left[i] < 0) m = -m;
      if (m == left[j-1]) {
        cout << "YES" << endl;
        return;
      }
    }
  }
  cout << "NO" << endl;
}

int main()
{
  int T = 0, tc = 0;
  for (cin >> T; tc < T; tc++) run(tc);
  return 0;
}
