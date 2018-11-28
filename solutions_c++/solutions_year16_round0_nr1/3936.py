#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

set<int> digits;

void add(ll x) {
  while (x) {
    digits.insert(x % 10);
    x /= 10;
  }
}

ll n;
int mx = 0;

void read() {
  cin >> n;
}

void kill() {
  if (n == 0) {
    cout << "INSOMNIA\n";
    return;
  }

  digits.clear();

  int ans = 0;
  ll cur = 0;

  while (digits.size() < 10) {
    cur += n;
    add(cur);
    ++ans;
  }

  mx = max(ans, mx);

  cout << cur << "\n";
}


int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cout << "Case #" << i << ": ";
    read();
    kill();
    cerr << "Case #" << i << " done.\n";
  }
  cerr << "max = " << mx << endl;
  return 0;
}
