#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <functional>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <valarray>
#include <vector>
#include <ext/algorithm>
#include <ext/hash_map>
#include <ext/hash_set>
#include <ext/numeric>
using namespace std;
using namespace __gnu_cxx;

#define F(i,a,b)for(int i=a;i<b;++i)
#define rep(i,n)F(i,0,n)
#define all(a)a.begin(),a.end()
template<class T>vector<T>&operator<<(vector<T>& v,T t){v.push_back(t);return v;} 

typedef long long ll;

const ll BOUND = (1LL << 51);


ll clog2(ll x) {
  ll res = 0;
  while (x) {
    x = (x - 1) / 2;
    res++;
  }
  return res;
}

ll worstloc(ll n, ll p, ll k) {
  if (k == 0) return 0;
  return ((1LL << clog2(k)) - 1) << (n - clog2(k));
}

ll bestloc(ll n, ll p, ll k) {
  ll N = (1LL << n);
  ll zeros = clog2(N - k - 1);
  return (1LL << (n - zeros)) - 1;
}

bool feas(ll n, ll p, ll k) {
  return worstloc(n, p, k) < p;
}

bool poss(ll n, ll p, ll k) {
  return bestloc(n, p, k) < p;
}

ll guaranteed(ll n, ll p) {
  if (p == (1LL << n)) return p - 1;
  ll low = 0;
  ll high = (1LL << n);
  while (high - low > 5) {
    ll mid = low/2 + high/2;
    if (feas(n, p, mid)) {
      low = mid;
    } else {
      high = mid;
    }
  }

  for(ll i = low; i < high + 1; ++i) {
    if (!feas(n, p, i)) return i - 1;
  }

  assert(0);
}

ll best(ll n, ll p) {
  if (p == (1LL << n)) return p - 1;
  ll low = 0;
  ll high = (1LL << n);
  while (high - low > 5) {
    ll mid = low/2 + high/2;
    if (poss(n, p, mid)) {
      low = mid;
    } else {
      high = mid;
    }
  }

  for(ll i = low; i < high + 1; ++i) {
    if (!poss(n, p, i)) return i - 1;
  }
  assert(0);
}

int main() {
  int T;
  cin >> T;
  rep(t, T) {
    ll n, p;
    cin >> n >> p;
    printf("Case #%d: %lld %lld\n", t + 1, guaranteed(n, p), best(n, p));
  }
}
