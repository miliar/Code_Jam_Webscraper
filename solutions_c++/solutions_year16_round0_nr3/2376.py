#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <set>
#include <queue>

using namespace std;

#define forn(i, n) for(int i = 0; i < (n); ++i)

vector<int> primes;

void solve(int n, int q) {
  vector<int> divisors;
  forn (i, 1 << (n - 2)) {
    int mask = (1 << (n - 1)) | (i << 1) | 1;
    // cout << i << endl;
    divisors.clear();
    for (int b = 2; b <= 10; ++b) {
      long long p = 1;
      long long s = 0;
      int x = mask;
      while (x) {
        s += (x & 1) * p;
        p *= b;
        x >>= 1;
      }
      bool found = false;
      for (int p : primes) {
        if (1LL * p * p > s) {
          break;
        }
        if (s % p == 0) {
          // cout << s << ' ' << p << endl;
          found = true;
          divisors.push_back(p);
          break;
        }
      }
      if (!found) {
        break;
      }
    }
    if (divisors.size() == 9) {
      for (int j = n - 1; j >= 0; --j) {
        cout << ((mask >> j) & 1);
      }
      for (int d : divisors) {
        cout << ' ' << d;
      }
      cout << endl;
      q--;
    }



    if (q == 0) {
      break;
    }

  }
}

void init_primes() {
  const int N = 1000000;
  vector<bool> prime(N + 1, true);
  for (int i = 2; i <= N; ++i) {
    if (prime[i]) {
      primes.push_back(i);
      for (long long j = 1LL * i * i; j <= N; j += i) {
        prime[j] = false;
      }
    }
  }
  // cout << primes.size() << endl;
}

int main() {

  init_primes();

  freopen("in.txt", "r", stdin);
  // freopen("B-large.in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  // ios_base::sync_with_stdio(false);
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    cout << "CASE #" << i + 1 << ":\n";
    solve(16, 50);

    // string s;
    // cin >> s;
    // cout << solve_fast(s) << endl;
  }

  // solve(32, 50);

  return 0;
}