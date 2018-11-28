#include <iostream>
using namespace std;

int main() {
  int T;
  cin >> T;
  for (int tt = 0; tt < T; tt++) {
    string a, b;
    cin >> a >> b;
    int cur = 0;
    int ans = 0;
    for (int i = 0; i < b.size(); i++) {
      int num = b[i] - '0';
      if (cur + ans < i) {
        ans += i - (cur + ans);
      }
      cur += num;
    }
    printf("Case #%d: %d\n", tt+1, ans);
  }
}
