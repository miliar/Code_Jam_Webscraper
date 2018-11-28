#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <unordered_set>
#include <unordered_map>

using namespace std;

long long T, N, J;
long long ans[11];

inline bool t(long long n, long long k) {
  long long p = 0, q = 1;
  for (long long i = 0; i < N; ++i) {
    p += ((n>>i)&1) * q;
    q *= k;
  }
  // cout << k <<": " <<p<< endl;
  for (long long i = 2; i <= sqrt(p); ++i) {
    if (p % i == 0) {
      ans[k] = i;
      return true;
    }
  }
  return false;
}

inline bool f(long long n) {
  for (long long i = 2; i <= 10; ++i)
    if (!t(n, i))
      return false;
  return true;
}

inline void output(long long n) {
  --J;
  for (long long i = N-1; i >= 0; --i)
    cout << ((n>>i)&1);
  for (long long i = 2; i <= 10; ++i)
    cout << ' ' << ans[i];
  cout << endl;
}

int main() {
  cin >> T;
  for (long long ti = 1; ti <= T; ++ti) {
    cin >> N >> J;
    cout << "Case #" << ti << ":" << endl;
    for (long long n = 0; J > 0 && n < (1<<(N-2)); ++n) {
      long long m = (1<<(N-1)) + (n<<1) + 1;
      if (f(m))
        output(m);
    }
  }
  return 0;
}
