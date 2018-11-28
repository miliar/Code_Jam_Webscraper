#include <iostream>
#include <cstring>
using namespace std;

long times(long n) {
  bool dig[10] = {false};
  int left = 10, i = n;
  for (; true; i += n) {
    long k = i;
    while (k > 0) {
      if (!dig[k%10]) {
        --left;
        dig[k%10] = true;
        if (!left) return i;
      }
      k /= 10;
    }
  }
}

int main() {
  int N;
  cin >> N;
  for (int num = 1; num <= N; ++num) {
    long n; cin >> n;
    cout << "Case #" << num << ": ";
    if (n == 0) cout << "INSOMNIA" << endl;
    else cout << times(n) << endl;
  }
  return 0;
}
