#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>

#define FOR(i,n) for(int i=0; i<n; i++)

typedef long long LL;

using namespace std;

bool seen[10];

void solve() {
  LL n;
  cin >> n;
  memset(seen, 0, sizeof(seen));
  for (LL i = 1; i <= 10000000l; i++) {
    LL r = n * i;
    while (r != 0) {
      seen[r % 10] = 1;
      r /= 10;
    }

    bool bad = false;
    FOR(j,10) {
      if (!seen[j]) {
        bad = 1;
        break;
      }
    }

    if (!bad) {
      cout << n * i << endl;
      return;
    }
  }

  cout << "INSOMNIA" << endl;
}

int main() {
  ios_base::sync_with_stdio(0);
  int tt;
  cin >> tt;
  FOR(t,tt) {
    cout << "Case #" << t + 1 << ": ";
    solve();
  }
  return 0;
}
