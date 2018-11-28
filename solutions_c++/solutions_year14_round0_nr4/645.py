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
  int N; cin >> N;
  vector<double> naomi(N), ken(N);
  for (int i = 0; i < N; i++)
    cin >> naomi[i];
  for (int i = 0; i < N; i++)
    cin >> ken[i];

  sort(naomi.begin(), naomi.end());
  sort(ken.begin(), ken.end());

  vector<bool> nplayed(N);
  vector<bool> kplayed(N);
  int war = 0;
  for (int i = 0; i < N; i++) {
    double n = naomi[i];
    int kmin = -1, next = -1;
    for (int j = 0; j < N; j++) {
      if (!kplayed[j]) {
        if (kmin < 0) kmin = j;
        if (next < 0 && ken[j] > naomi[i])
          next = j;
      }
    }
    if (next > -1)
      kplayed[next] = true;
    else {
      kplayed[kmin] = true;
      war++;
    }
    nplayed[i] = true;
  }

  kplayed = vector<bool>(N);
  nplayed = vector<bool>(N);
  int dwar = 0;
  for (int i = 0; i < N; i++) {
    int kmax = -1;
    for (int j = N-1; j >= 0; j--)
      if (!kplayed[j]) {
        kmax = j;
        break;
      }

    int nmin = -1, next = -1;
    for (int j = 0; j < N; j++) {
      if (!nplayed[j]) {
        if (nmin < 0)
          nmin = j;
        if (next < 0 && naomi[j] > ken[kmax])
          next = j;
      }
    }

    if (next > -1) {
      nplayed[next] = true;
      dwar++;
    } else
      nplayed[nmin] = true;
    kplayed[kmax] = true;
  }

  cout << "Case #" << (tc + 1) << ": " << dwar << " " << war << endl;
}

int main()
{
  int T = 0, tc = 0;
  for (cin >> T; tc < T; tc++) run(tc);
  return 0;
}
