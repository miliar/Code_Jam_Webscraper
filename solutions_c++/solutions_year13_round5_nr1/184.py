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
typedef map<ll, ll> MAP;
typedef MAP::iterator Mit;
typedef stringstream SS;

template <class Ta, class Tb> inline Tb cast(Ta a) { SS ss; ss << a; Tb b; ss >> b; return b; };

const double EPS = 1e-9;
const int INF = 1000000000;
const int diri[8] = { -1, 0, 1, 0, -1, 1, 1, -1 };
const int dirj[8] = { 0, 1, 0, -1, 1, 1, -1, -1 };

ld fun(const Vll& v, ll h, ll budget) {
  int n = v.size();
  Vll u;
  for (int i = 0; i < n; ++i)
    if (v[i] <= h) u.push_back(h - v[i]);
  sort(u.begin(), u.end());
  int m = u.size();
  
  ll cost = 0;
  for (int i = 0; i < m; ++i) cost += u[i];
  if (cost > budget) return -1;
  
  ld res = 36*cost/ld(m) - cost;
  
  ll g = cost;
  for (int i = 0; i < m; ++i) {
    ++cost;
    g -= u[i];
    if (cost > budget) return res;
    ld r = 36*g/ld(m - i - 1) - cost;
    res = max(res, r);
  }
  return res;
}

ld vaca(const Vll& v, ll budget, ll e, ll d) {
  while (d - e > 100) {
    ll m1 = e + (d - e)/3;
    ll m2 = e + 2*(d - e)/3;
    
    ld r1 = fun(v, m1, budget);
    ld r2 = fun(v, m2, budget);
    
    if (r1 < r2) {
      e = m1;
    }
    else {
      d = m2;
    }
  }
  ld res = 0;
  for (ll x = e; x <= d; ++x) {
    res = max(res, fun(v, x, budget));
  }
  return res;
}

int main() {
  cout.setf(ios::fixed);
  cout.precision(10);
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    ll b;
    int n;
    cin >> b >> n;
    Vll v(37, 0);
    for (int i = 0; i < n; ++i) cin >> v[i];
    ld res = 0;
    for (int i = 0; i < 37; ++i) {
      if (v[i] > 0) res = max(res, fun(v, v[i] - 1, b));
      res = max(res, fun(v, v[i], b));
      res = max(res, fun(v, v[i] + 1, b));
    }
    
    ll e = 0, d = 100000000000000LL;
    while (e <= d) {
      ll m = (e + d)/2;
      ld r = fun(v, m, b);
      res = max(res, r);
      if (r > EPS) {
        e = m + 1;
      }
      else {
        d = m - 1;
      }
    }
    
    sort(v.begin(), v.end());
    res = max(res, vaca(v, b, 0, v[0]));
    for (int i = 0; i + 1 < 37; ++i) {
      res = max(res, vaca(v, b, v[i], v[i + 1]));
    }
    res = max(res, vaca(v, b, v[36], INF));
    
//     MAP mp;
//     for (int i = 0; i < 37; ++i) ++mp[v[i]];
//     
//     for (Mit it = mp.begin(); it != mp.end(); ++it) {
//       ll m = 0;
//       ll r = 0;
//       ll t = 0;
//       for (Mit jt = mp.begin(); jt != it; ++jt) {
//         m += (it->first - jt->first)*jt->second;
//         r += 36*(it->first - jt->first)*jt->second;
//         t += jt->second;
//       }
//       for (int i = 0; i <= it->second; ++i) {
//         ll m2 = m;
//         ll r2 = r;
//         ll t2 = t;
//         m2 += i;
//         t2 += it->second - i;
// //         if (it->first == 0 and i == 1) cerr << "mp=" << mp << " rp=" << rp << " tp=" << tp << endl;
//         if (m2 <= b) {
//           res = max(res, r2/ld(t2) - m2);
//         }
//       }
//     }
    
    cout << "Case #" << cas << ": " << res << endl;
  }
}
