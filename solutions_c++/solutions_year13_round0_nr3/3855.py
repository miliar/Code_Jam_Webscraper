#include<iostream>

using namespace std;

#define rep(i, n) for (int i = 0; i < int(n); ++i)

bool ispal(long long n) {
  int a[20], i = 0;;
  while (n != 0) {
    a[i++] = n % 10;
    n /= 10;
  }
  rep (j, i) if (a[j] != a[i - j - 1]) return false;
  return true;
}

int main() {
  int t;
  cin >> t;
  rep (iii, t) {
    long long a, b;
    cin >> a >> b;
    long long res = 0;
    for (long long i = 1; i * i <= b; ++i) {
      if (i * i < a) continue;
      if (ispal(i) && ispal(i * i)) ++res;
    }
    cout << "Case #" << iii + 1 << ": " << res << endl;
  }
  return 0;
}
