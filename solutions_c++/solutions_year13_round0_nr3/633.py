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

bool ispal(int64 a) {
  char buf[150];
  int sz = 0;
  while (a) {
    buf[sz] = a%10;
    a /= 10;
    sz++;
  }
  for (int i = 0; i < sz/2; i++)
    if (buf[i] != buf[sz - i - 1])
      return false;
  return true;
}

void run(int tc)
{
  int64 A, B;
  cin >> A >> B;
  int64 sA = sqrt(A-1)+1, sB = sqrt(B);

  int cnt = 0;
  for (int64 i = sA; i <= sB; i++)
    if (ispal(i) && ispal(i*i)) {
      //DEBUG(make_pair(i, i*i));
      cnt++;
    }

  cout << "Case #" << (tc + 1) << ": " << cnt << endl;
}

int main()
{
  int T = 0, tc = 0;
  for (cin >> T; tc < T; tc++) run(tc);
  return 0;
}
