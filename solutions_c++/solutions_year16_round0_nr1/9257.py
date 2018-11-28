#include <iostream>
using namespace std;

int main() {
  int T, _42=1;
  cin >> T;
  while (T--) {
    long long N;
    cin >> N;
    cout << "Case #" << _42++ << ": ";
    if (N != 0) {
      int seen[10] = {0};
      bool hasAll = false;
      long long ans = N;
      while (!hasAll) {
        long long aux = ans;
        while (aux > 0) {
          seen[aux%10] = 1;
          aux = aux/10;
        }
        hasAll = true;
        for (int i = 0; i <= 9; i++) {
          if (seen[i] == 0) hasAll = false;
        }
        ans += N;
      }
      cout << ans-N << endl;
    } else {
      cout << "INSOMNIA" << endl;
    }
  }
  return 0;
}
