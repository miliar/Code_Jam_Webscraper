#include <bits/stdc++.h>
using namespace std;

int main() {
  using ll = long long;
  ll t;
  cin >> t;
  for (int z = 1; z <= t; ++z) {
    ll n;
    cin >> n;
    cout << "Case #" << z << ": ";
    if (n == 0) cout << "INSOMNIA" << endl;
    else {
      vector<bool> dig(10), comp(10, 1);
      ll curr = 0;
      do {
        curr += n;
        ll aux = curr;
        while (aux != 0) {
          dig[aux % 10] = true;
          aux /= 10;
        }
      } while (dig != comp);
      cout << curr << endl;
    }
  }
}