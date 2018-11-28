#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define X first
#define Y second

typedef long long ll;
typedef long double ld;
typedef pair<int, int> P;
typedef vector<bool> Vb;
typedef vector<Vb> Mb;
typedef vector<char> Vc;
typedef vector<Vc> Mc;
typedef vector<int> Vi;
typedef vector<Vi> Mi;
typedef vector<ll> Vll;
typedef vector<Vll> Mll;
typedef vector<P> Vp;
typedef vector<Vp> Mp;
typedef vector<string> Vs;
typedef vector<Vs> Ms;

typedef set<int> SET;
typedef SET::iterator Sit;
typedef map<int, int> MAP;
typedef MAP::iterator Mit;
typedef stringstream SS;

template <class Ta, class Tb> inline Tb cast(Ta a) { SS ss; ss << a; Tb b; ss >> b; return b; };

const double EPS = 1e-9;
const int INF = 1000000000;
const int diri[8] = { -1, 0, 1, 0, -1, 1, 1, -1 };
const int dirj[8] = { 0, 1, 0, -1, 1, 1, -1, -1 };

ll funworst(ll n, ll p) {
  ll res = 0;
  while (n > 0) {
    res = 2*res + 1;
    n = (n + 1)/2 - 1;
    --p;
  }
  res *= 1LL<<p;
  return res;
}

ll funbest(ll n, ll p) {
  return (1LL<<p) - 1 - funworst((1LL<<p) - 1 - n, p);
}

ll find_guaranteed(ll n, ll p) {
  ll e = 0;
  ll d = (1LL<<n) - 1;
  while (e <= d) {
    ll m = (e + d)/2;
    if (funworst(m, n) < p) {
      e = m + 1;
    }
    else {
      d = m - 1;
    }
  }
  return e - 1;
}

ll find_could(ll n, ll p) {
  ll e = 0;
  ll d = (1LL<<n) - 1;
  while (e <= d) {
    ll m = (e + d)/2;
    if (funbest(m, n) < p) {
      e = m + 1;
    }
    else {
      d = m - 1;
    }
  }
  return e - 1;
}

int main() {
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    ll n, p;
    cin >> n >> p;
    cout << "Case #" << cas << ": " << find_guaranteed(n, p) << " " << find_could(n, p) << endl;
  }
}
