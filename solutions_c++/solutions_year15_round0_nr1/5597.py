#include <iostream>
using namespace std;

int main() {
  int T;
  cin >> T;

  for (int CASE = 1; CASE <= T; CASE++) {
    cout << "Case #" << CASE << ": ";

    int n;
    string s;
    cin >> n >> s;

    int ans = 0;
    int sum = 0;

    for (int i = 0; i < n + 1; i++) {
      int d = s[i] - '0';

      if (sum < i) {
        ans += i - sum;
        sum += i - sum;
      }
      sum += d;
    }

    cout << ans << endl;
  }
}
