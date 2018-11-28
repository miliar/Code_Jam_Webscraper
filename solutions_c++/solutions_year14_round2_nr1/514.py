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
  int N;
  cin >> N;
  vector<string> s(N);
  for (int i = 0; i < N; i++)
    cin >> s[i];

  cout << "Case #" << (tc + 1) << ": ";

  vector<string> clean(N);
  vector<veci> reps(N);
  for (int i = 0; i < N; i++)
    for (int j = 0; j < s[i].size(); j++) {
      if (j == 0 || s[i][j] != s[i][j-1]) {
        clean[i].append(1, s[i][j]);
        reps[i].push_back(0);
      }
      reps[i].back()++;
    }
  for (int i = 1; i < N; i++)
    if (clean[i] != clean[i-1]) {
      cout << "Fegla Won" << endl;
      return;
    }

  int res = 0;
  for (int i = 0; i < reps[0].size(); i++) {
    int low, high;
    for (int j = 0; j < N; j++) {
      if (j == 0 || reps[j][i] < low)
        low = reps[j][i];
      if (j == 0 || reps[j][i] > high)
        high = reps[j][i];
    }
    int curmin;
    for (int j = low; j <= high; j++) {
      int cost = 0;
      for (int k = 0; k < N; k++)
        cost += abs(reps[k][i] - j);
      if (j == low || cost < curmin)
        curmin = cost;
    }
    res += curmin;
  }
  cout << res << endl;
}

int main()
{
  int T = 0, tc = 0;
  for (cin >> T; tc < T; tc++) run(tc);
  return 0;
}
