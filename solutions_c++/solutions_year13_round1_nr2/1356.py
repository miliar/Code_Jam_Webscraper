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
  int E, R, N;
  cin >> E >> R >> N;
  vector<int64> v(N);
  for (int i = 0; i < N; i++)
    cin >> v[i];
  R = min(R, E);

  vector<int64> *v0 = new vector<int64>(E+1);
  vector<int64> *v1 = new vector<int64>(E+1);
  for (int i = 0; i < N; i++) {
    vector<int64> &v0r = *v0;
    vector<int64> &v1r = *v1;
    for (int j = R; j <= E; j++) {
      int64 mx = 0;
      for (int k = j-R; k <= E; k++) {
        mx = max(mx, v0r[k] + (R+(k-j))*v[i]);
      }
      v1r[j] = mx;
    }
    swap(v0, v1);
  }

  int64 res = 0;
  for (int i = R; i <= E; i++)
    res = max(res, (*v0)[i]);

  cout << "Case #" << (tc + 1) << ": " << res << endl;
  delete v0;
  delete v1;
}

int main()
{
  int T = 0, tc = 0;
  for (cin >> T; tc < T; tc++) run(tc);
  return 0;
}
