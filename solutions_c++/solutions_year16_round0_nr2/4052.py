#include <algorithm>
#include <cstdio>
#include <iostream>
#include <string>

int main() {
  int cas;
  std::cin >> cas;
  for (int _t = 1; _t <= cas; _t++) {
    printf("Case #%d: ", _t);
    std::string str;
    std::cin >> str;
    std::string str2 = str.substr(1, str.length() - 1);
    char pre = str[0];
    int ans = str[0] == '-';
    int cur = 1;
    for (auto &s : str2) {
      if (s != pre) {
        cur ++;
      }
      if (s == '-') {
        ans = cur;
      }
      pre = s;
    }
    std::cout << ans << std::endl;
  }
  return 0;
}
