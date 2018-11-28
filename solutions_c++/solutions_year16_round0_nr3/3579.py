#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <complex>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <iomanip>
#include <assert.h>
#include <array>
#include <cstdio>
#include <cstring>
#include <random>
#include <functional>
#include <numeric>
#include <bitset>

using namespace std;

//struct before_main{before_main(){cin.tie(0); ios::sync_with_stdio(false);}} before_main;

#define REP(i,a,b) for(int i=a;i<(int)b;i++)
#define rep(i,n) REP(i,0,n)
#define all(c) (c).begin(), (c).end()
#define zero(a) memset(a, 0, sizeof a)
#define minus(a) memset(a, -1, sizeof a)
template<class T1, class T2> inline bool minimize(T1 &a, T2 b) { return b < a && (a = b, 1); }
template<class T1, class T2> inline bool maximize(T1 &a, T2 b) { return a < b && (a = b, 1); }

typedef long long ll;
int const inf = 1<<29;

template<class T> vector<T> divisors(T x) {
  vector<T> ret;
  int p = 1;
  while((ll)p * p <= x) {
    if(x % p == 0) {
      ret.push_back(p);
      ret.push_back(x/p);
    }
    p ++;
  }
  return ret;
}

int main() {

  int T; cin >> T;
  int N, J; cin >> N >> J;
  cout << "Case #1:" << endl;

  auto is_prime = [&](ll x) {
    for(int i=2; (ll)i*i<=x; i++) {
      if(x % i == 0) { return false; }
    }
    return true;
  };

  auto to_bit_string = [&](ll x) {
    string s;
    while(x) {
      s.push_back(x%2 + '0');
      x /= 2;
    }
    reverse(all(s));
    return s;
  };

  auto change_base = [&](ll x, int base) {
    string s = to_bit_string(x);
    int dcnt = s.size();
    ll ret = 0;
    ll bpow = 1;
    rep(i, dcnt) {
      ret += (s[dcnt-1-i] - '0') * bpow;
      bpow *= base;
    }

    return ret;
  };


  int jcnt = 0;

  REP(bit, 2, 1<<N) {
    if(!((bit & 1) == 1 && (bit >> (N-1) & 1) == 1)) {
      continue;
    }

    vector<ll> v;

    REP(base, 2, 11) {
      auto r = change_base(bit, base);

      if(!is_prime(r)) {
        auto D = divisors(r);
        for(auto u: D) {
          if(u != 1 && u != r) {
            v.push_back(u);
            break;
          }
        }
      }
    }

    if(v.size() == 9) {
      jcnt ++;
      cout << to_bit_string(bit);
      for(auto && e: v) {
        cout << " " << e;
      }
      cout << endl;
      if(jcnt == J) {
        break;
      }
    }
  }
  
  return 0;
}