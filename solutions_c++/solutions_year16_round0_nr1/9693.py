#include <bits/stdc++.h>

using namespace std;

int main() {
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    long long b;
    cin >> b;
    if (b == 0) {
      cout << "Case #" << i +1 << ": INSOMNIA" << endl;
      continue;
    }
    long long a = b;
    bool digits[10] = {false};
    int done = 0;
    int j = 1;
    bool bs=false;
    while (true) {
      int t = abs(a);
      while (t > 0) {
        if (!digits[t%10]) {
          digits[t%10] = true;
          done++;
        }
        t /= 10;
      }
      if (done == 10) {
        break;
      }
      j++;
      a = b*j;
      if (j == 10000000) {
        cout << "Case #" << i +1 << ": INSOMNIA" << endl;
        bs=true;
        break;
      }
    }
    if(!bs) cout << "Case #" << i +1 << ": " << a << endl;
  }

  return 0;
}
