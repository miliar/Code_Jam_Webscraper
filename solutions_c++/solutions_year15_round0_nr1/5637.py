#include <iostream>

using namespace std;

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; i++) {
    int a; string b;
    cin >> a >> b;
    int c = 0;
    int ans = 0;
    for (int j = 0; j < b.size(); j++) {
      if (c < j) {
        ans += j-c;
        c = j;
      }
      c += b[j] - '0';
    }
    cout << "Case #" << i << ": " << ans << endl;
  }
}