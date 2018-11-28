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
typedef pair<ll, ll> P;
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

const ll MOD = 1000002013LL;

ll sum(ll n) {  // 1 + 2 + ... + n
  return n*(n + 1)/2;
}

ll fun(ll n, ll m) {
  return sum(n) - sum(n - m);
}

bool sortf(P a, P b) {
  if (a.X != b.X) return a.X > b.X;
  return a.Y < b.Y;
}

int main() {
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    ll n, m;
    cin >> n >> m;
    
    ll cost1 = 0;
    Vp v(2*m);
    for (int i = 0; i < m; ++i) {
      ll a, b, q;
      cin >> a >> b >> q;
      v[2*i] = P(a, q);
      v[2*i + 1] = P(b, -q);
      cost1 = (cost1 + ((fun(n, b - a)%MOD)*q)%MOD)%MOD;
//       cerr << "cost1 += " << fun(n, b - a) << endl;
    }
    sort(v.begin(), v.end(), sortf);
    
//     for (int i = 0; i < 2*m; ++i) cerr << " (" << v[i].X << " " << v[i].Y << ")";
//     cerr << endl;
    
    ll cost2 = 0;
    priority_queue<P> cua;
    for (int i = 0; i < 2*m; ++i) {
//       cerr << "i=" << i << endl;
      if (v[i].Y < 0) cua.push(P(-v[i].X, -v[i].Y));
      else {
        ll a = v[i].X;
        ll p = v[i].Y;
        while (p > 0) {
          ll b = -cua.top().X;
          ll q = cua.top().Y;
          cua.pop();
          
          ll t = min(p, q);
          p -= t;
          q -= t;
          
          cost2 = (cost2 + ((fun(n, b - a)%MOD)*t)%MOD)%MOD;
          
          if (q > 0) cua.push(P(-b, q));
        }
      }
    }
    
//     cerr << "cost1=" << cost1 << endl;
//     cerr << "cost2=" << cost2 << endl;
    
    ll res = ((cost1 - cost2)%MOD + MOD)%MOD;
    
    cout << "Case #" << cas << ": " << res << endl;
  }
}
