#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int sz = 1e6 + 1;
const int len = 50;
typedef unsigned long long int ll;
vector<ll> primes;
bool not_primes[sz];
bool bits[len];
int acc = 0;
int N, J;

void Verify(int b, int tl, ll p) {
  ll m = 1;
  ll bm = 1;
  for (int i = 1; i < tl; ++i) {
    bm *= b;
    if (bits[i]) {
      m += bm;
    }
  }

  if (m % p != 0) {
    cout << "Shit" << endl;
  }
  if (m == p) {
    cout << "Fuck" << endl;
  }

  cout << "XX " << m << " " << p << endl;
}

bool non_eq(int b, ll p, int tl) {
  for (int i = 0; i < tl; ++i) {
    if (p % b != bits[i]) {
      return true;
    }
    p /= b;
  }
  return false;
}

bool can_d(ll b, ll p, int tl) {
  ll m = 1;
  ll bm = 1;
  for (int i = 1; i < tl; ++i) {
    bm *= b;
    bm %= p;
    if (bits[i]) {
      m += bm;
      m %= p;
    }
  }
  return (m == 0) && non_eq(b, p , tl);
}

void pbits(int tl) {
  for (int i = tl - 1; i >= 0; --i) {
    cout << bits[i];
  }
}

void setp(int i, int tl) {
  if (acc == J) {
    return;
  }
  if (i == 0) {
    vector<ll> ans;
    for (ll b = 2; b <= 10; ++b) {
      bool found = false;
      for (ll p : primes) {
        if (can_d(b, p, tl)) {
          ans.push_back(p);
          // Verify(b, tl, p);
          found = true;
          break;
        }
      }
      if (!found) {
        return;
      }
    }

    pbits(tl);
    cout << " ";
    for (ll num : ans) {
      cout << num << " ";
    }
    cout << endl;
    ++acc;
  } else {
    setp(i - 1, tl);
    bits[i] = true;
    setp(i - 1, tl);
    bits[i] = false;
  }
}

int main() {
  for (ll i = 2; i < sz; i += 1) {
    if (!not_primes[i]) {
      primes.push_back(i);
    }
    for (ll j = 0, e = primes.size(); j < e && i * primes[j] < sz; ++j) {
      not_primes[i * primes[j]] = true;
      if (i % primes[j] == 0) {
        break;
      }
    }
  }
  int T;
  cin >> T >> N >> J;

  cout << "Case #1:" << endl;
  bits[0] = true;
  bits[N - 1] = true;
  setp(N - 2, N);

}
