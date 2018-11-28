#include <iostream>
#include <vector>

using namespace std;

typedef long long int ll;

ll reverse(ll x) {
  ll r = 0;
  while (x > 0) {
    r *= 10;
    r += (x % 10);
    x /= 10;
  }
  return r;
}

int main_() {
//   int tt;
//   cin >> tt;
  int N = 1e6;
  vector<int> M(N + 1);
  for (int i = 0; i <= N; ++i) M[i] = i;  
  for (int i = 1; i <= N; ++i) {
    int r = reverse(i);
    M[i + 1] = min(M[i + 1], M[i] + 1);
    if (r <= N) M[r] = min(M[r], M[i] + 1);
  }
  for (int i = 1; i <= N; ++i) cout << i << " " << M[i] << endl;
//   for (int t = 1; t <= tt; ++t) {
//     cout << "Case #" << t << ": ";
//     ll n;
//     cin >> n;
//     cout << M[n] << endl;
//   }
}

int dig(ll n) {
  int r = 0;
  while (n > 0) {
    n /= 10;
    ++r;
  }
  return r;
}

bool isp(ll n) {
  int d = dig(n);
  ll r = 1;
  for (int i = 0; i < d - 1; ++i) r *= 10;
  return n == r;
}

ll f(ll n) {
  //cerr << n << '-';
  if (n < 20) return n; //!
  if (n % 10 == 0) return f(n - 1) + 1;
  ll res = 0;
  int d = dig(n);
  ll c = n;
  ll p = 1;
  for (int i = 0; i < d - d/2; ++i) p *= 10ll;
  c = (n) - (n % p) + 1;
  // if (isp(n)) return f(n - 1) + 1;
  if (isp(n / p)) return f(n - n/p) + (n/p);
  res += n - c;
  return res + 1 + f(reverse(c));
}

int main() {
  int tt;
  cin >> tt;
  for (int t = 1; t <= tt; ++t) {
    cout << "Case #" << t << ": ";
    ll n;
    cin >> n;
    cout << f(n) << endl;
  }
}

int omain() {
  for (int i = 1; i <= 1e6; ++i) cout << i << ' ' << f(i) << endl;
}