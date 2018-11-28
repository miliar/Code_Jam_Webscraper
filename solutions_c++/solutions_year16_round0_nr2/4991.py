#include <iostream>
#include <string>
using namespace std;

int main() {
  int T;
  string input;
  char str[101];
  cin >> T;
  for (int x=1; x<=T; ++x) {
    cin >> input;
    int len = 1;
    str[0] = input[0];
    for (int i=1; i<input.length(); ++i) {
      if (input[i] != str[len-1])
        str[len++] = input[i];
    }

    int ans = 0;
    if (len == 1) {
      ans = (str[0] == '+')? 0:1;
    }
    else {
      char pre = str[0];
      for (int i=1; i<len; ++i) {
        if (str[i] == pre) continue;

        ans += (pre == '-' && str[i] == '+')? 1:2;
        pre = '+';
      }
    }

    cout << "Case #" << x << ": " << ans << endl;
  }
  return 0;
}
