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

map<pair<int64, int64>, int64> memo;
int64 minop(const vector<int64> &motes, int64 i, int64 sz) {
  if (i >= motes.size())
    return 0;
  if (memo.find(make_pair(i, sz)) != memo.end())
    return memo[make_pair(i, sz)];
  if (sz > motes[i])
    return memo[make_pair(i, sz)] = minop(motes, i + 1, sz + motes[i]);
  if (sz == 1)
    return memo[make_pair(i, sz)] = 1 + minop(motes, i + 1, sz);
  return memo[make_pair(i, sz)] =
    1 + min(
      minop(motes, i, sz + sz - 1),
      minop(motes, i + 1, sz)
    );
}

void run(int64 tc)
{
  int64 A, N;
  cin >> A >> N;
  vector<int64> motes(N);
  for (int64 i = 0; i < N; i++)
    cin >> motes[i];
  sort(motes.begin(), motes.end());

  //DEBUG(make_pair(A, motes));
  memo.clear();
  int64 n = minop(motes, 0, A);

  cout << "Case #" << (tc + 1) << ": " << n << endl;
}

int main()
{
  int T = 0, tc = 0;
  for (cin >> T; tc < T; tc++) run(tc);
  return 0;
}
