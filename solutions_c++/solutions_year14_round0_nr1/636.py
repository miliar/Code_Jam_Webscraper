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
  int r1; cin >> r1;
  vector<veci> cards1(4, veci(4));
  for (int i = 0; i < 4; i++)
    for (int j = 0; j < 4; j++)
      cin >> cards1[i][j];
  int r2; cin >> r2;
  vector<veci> cards2(4, veci(4));
  for (int i = 0; i < 4; i++)
    for (int j = 0; j < 4; j++)
      cin >> cards2[i][j];

  veci options(16);
  for (int i = 0; i < 4; i++)
    options[cards1[r1-1][i]-1]++;
  for (int i = 0; i < 4; i++)
    options[cards2[r2-1][i]-1]++;

  int res = -1, c = 0;
  for (int i = 0; i < 16; i++)
    if (options[i] == 2) {
      res = i + 1;
      c++;
    }

  cout << "Case #" << (tc + 1) << ": ";
  if (c > 1)
    cout << "Bad magician!" << endl;
  else if (c == 0)
    cout << "Volunteer cheated!" << endl;
  else
    cout << res << endl;
}

int main()
{
  int T = 0, tc = 0;
  for (cin >> T; tc < T; tc++) run(tc);
  return 0;
}
