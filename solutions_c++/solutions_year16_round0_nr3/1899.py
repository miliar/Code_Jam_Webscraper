#include <iostream>
#include <set>
#include <vector>

using namespace std;

typedef long long ll;
typedef vector<ll> VL;

void solve(int N, int J) {
  int n = (1 << 16) - 1;

  int cnt = 0;
  while (cnt < J) {
    n -= 2;
    VL divs;
    for (int base = 2; base <= 10; base++) {
      ll num = 0;
      for (int i = 15; i >= 0; i--) {
        num *= base;
        if ((n >> i) % 2) num++;
      }

      bool prime = true;
      int div = 2;
      for (div = 2; div < 100 && div*div <= num; div++) {
        if (num % div == 0) {
          prime = false;
          break;
        }
      }
      if (prime) {
        break;
      } else {
        divs.push_back(div);
      }
    }
    if (divs.size() == 9) {
      // ok
      for (int i = 0; i < N/16; i++) {
        for (int j = 15; j >= 0; j--) {
          cout << ((n >> j) % 2);
        }
      }
      for (ll div: divs) {
        cout << " " << div;
      }
      cout << endl;
      cnt++;
    }
  }
}

int main() {
  int N;
  cin >> N;
  for (int i = 0; i < N; i++) {
    int n, j;
    cin >> n >> j;
    cout << "Case #" << (i+1) << ": " << endl;
    solve(n, j);
  }

  return 0;
}
