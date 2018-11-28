#include <iostream>
using namespace std;

int digs(int n) {
  int bm = 0;
  while (n) {
    bm |= (1<<(n%10));
    n /= 10;
  }
  return bm;
}
int main() {
  int T; cin >> T;
  for (int ncase = 1; ncase <= T; ++ncase) {
    int n; cin >> n;
    if (!n) cout << "Case #" << ncase << ": INSOMNIA" << endl;
    else {
      int bm = digs(n);
      int k = 0;
      do bm |= digs(k+=n); while (bm != (1<<10)-1);
      cout << "Case #" << ncase << ": " << k << endl;
    }
  }
}
