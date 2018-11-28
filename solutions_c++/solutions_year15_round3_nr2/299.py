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
  int K, L, S;
  cin >> K >> L >> S;
  string k, l;
  cin >> k >> l;
  
  int freq[256] = {0};
  for (int i = 0; i < K; i++)
    freq[k[i]]++;

  double p = 1.0;
  bool iszero = false;
  for (int i = 0; i < L; i++) {
    p *= freq[l[i]];
    if (freq[l[i]] == 0)
      iszero = true;
  }
  p /= pow(double(K), double(L));

  double expgood = p * (S-L+1);

  int needed = 0;
  for (int i = 0; i < L; i++) {
    bool isgood = true;
    int start = L-i;
    for (int j = start; j < L; j++)
      if (l[j-start] != l[j])
        isgood = false;

    if (isgood) {
      needed = 1 + (S - L) / (L - i);
    }
  }
  if (iszero)
    needed = 0;

  double res = needed - expgood;
  cout << "Case #" << (tc + 1) << ": ";
  printf("%.9f\n", res);
}

int main()
{
  int T = 0, tc = 0;
  for (cin >> T; tc < T; tc++) run(tc);
  return 0;
}
