#include <iostream>
#include <string>

int main() {
  int T, sm, ans, n_friend, n;
  std::string str;

  std::cin >> T;
  for (int n_case = 1; n_case <= T; n_case++) {
    std::cin >> sm >> str;

    ans = n_friend = 0;
    for (int i = 0; i <= sm; i++) {
      n = str[i] - '0';
      if (ans >= i) {
        ans += n;
      }
      else {
        n_friend += i-ans;
        ans = i+n;
      }
    }
    std::cout << "Case #" << n_case << ": " << n_friend << '\n';
  }

  return 0;
}
