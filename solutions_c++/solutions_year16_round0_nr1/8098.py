#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(false);cout.tie(0);cin.tie(0);
using namespace std;

void solve() {
  
  int freq[10] = {0};
  long long n, c = 10, i = 1;

  cin >> n;
  if (!n) {
    cout << "INSOMNIA" << "\n";
    return;
  }
  while (c) {
    long long nn = n*i;
    while (nn) {
      if (freq[nn%10] == 0) {
        freq[nn%10] = 1;
        c--;
      }
      nn /= 10;
    }
    i++;
  }
  cout << n*(i-1) << "\n";
}

int main() { _
  int tt;
  cin >> tt;
  for (int t = 1; t <= tt; t++) {
    cout << "Case #" << t << ": ";
    solve();
  }
  return 0;
}
