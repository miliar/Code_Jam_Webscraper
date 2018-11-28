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

template<class T> ostream& operator << (ostream &o, const vector<T> &v)
{
  o << '{';
  FOREACH(it, v) o << (it == v.begin() ? "" : ", ") << *it;
  return o << '}';
}

void run(int tc)
{
  int N, M;
  cin >> N >> M;
  vector<vector<int>> lawn(N, vector<int>(M));
  for (int i = 0; i < N; i++)
    for (int j = 0; j < M; j++)
      cin >> lawn[i][j];
  
  bool can = true;
  for (int i = 0; i < N && can; i++)
    for (int j = 0; j < M && can; j++) {
      for (int k = 0; k < N; k++)
        if (lawn[k][j] > lawn[i][j])
          can = false;
      if (!can) {
        can = true;
        for (int k = 0; k < M; k++)
          if (lawn[i][k] > lawn[i][j])
            can = false;
      }
    }

  cout << "Case #" << (tc + 1) << ": " << (can ? "YES" : "NO") << endl;
}

int main()
{
  int T = 0, tc = 0;
  for (cin >> T; tc < T; tc++) run(tc);
  return 0;
}
