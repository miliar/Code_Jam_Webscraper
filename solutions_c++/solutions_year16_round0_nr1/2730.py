#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

int check(LL a, char * t) {
  int res = 0;
  while (a) {
    int c = a % 10;
    a /= 10;
    res += t[c];
    t[c] = 0;
  }
  
  return res;
}

void solve() {
  LL n;
  cin >> n;

  if (n == 0) {
    cout << "INSOMNIA" << endl;
  } else {
    LL a = n;
    char k[10];
    for (int i = 0; i < 10; ++i)
      k[i] = 1;

    int tmp = check(a, k);
    while (tmp < 10) {
      a += n;
      tmp += check(a, k);
    }

    cout << a << endl;
  }
}

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    cerr << "Test #" << i + 1 << " of " << t << endl;
    cout << "Case #" << i + 1 << ": ";
    solve();
  }

  return 0;
}
