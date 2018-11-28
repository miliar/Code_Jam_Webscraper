#define NDEBUG
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <random>
#include <set>
#include <string>
#include <vector>
using namespace std;

template <typename T> string itosb( T x, int base = 10 ) { string s; if ( x == 0 ) return "0"; int sign = x < 0 ? -1 : 1; while ( x != 0 ) { int digit = sign * ( x % base ); x /= base; if ( digit < 10 ) s.push_back( '0' + digit ); else s.push_back( 'A' + digit - 10 ); } if ( sign == -1 ) s.push_back( '-' ); reverse( s.begin(), s.end() ); return s; }
template<typename Set, typename Element> inline bool inset( const Set &S, const Element &E ) { return S.find(E) != S.end(); }

vector<int> primes;
void prep_primes(int upto) {
  for (int p=2; p<=upto; ++p) {
    bool prime = true;
    for (int i=2; i*i<=p; ++i) {
      if (p%i == 0) {
        prime = false;
        break;
      }
    }
    if (prime) {
      primes.push_back(p);
    }
  }
}

void solve() {
  int N, J;
  cin >> N >> J;
  prep_primes(1000);

  std::mt19937 rng(0xbabadeda);
  vector<int> divs;
  set<uint32_t> found;
  while (J > 0) {
    uint32_t X = rng();
    X &= (1llu<<N) - 1;
    X |= 1;
    X |= 1llu << (N-1);
    if (inset(found, X)) {
      continue;
    }
    string str = itosb(X, 2);
    assert((int)str.size() == N && str[0] == '1' && str[N-1] == '1');
    divs.clear();
    for (int b=2; b<=10; ++b) {
      __uint128_t Y = 0;
      for (char ch : str) {
        Y = b*Y + ch - '0';
      }
      int div = -1;
      for (uint32_t p : primes) {
        if (uint64_t(p)*p > Y) {
          break;
        }
        if (Y % p == 0) {
          div = p;
          break;
        }
      }
      if (div == -1) {
        break;
      }
      divs.push_back(div);
    }
    if (divs.size() == 9) {
      found.insert(X);
      --J;
      cout << str;
      for (int div : divs) {
        cout << ' ' << div;
      }
      cout << '\n' << flush;
    }
  }
}

int main() {
  ios_base::sync_with_stdio(false);

  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) {
    cout << "Case #" << tt << ":\n";
    solve();
  }
}
