#include <iostream>
#include <set>
#include <algorithm>

int main() {
  int cas;
  std::cin >> cas;
  for (int _t = 1; _t <= cas; _t++) {
    printf("Case #%d: ", _t);
    int n;
    std::cin >> n;
    long long cur = n;
    if (n == 0) {
      std::cout << "INSOMNIA" << std::endl; 
      continue;
    }
    bool flag = false;
    std::set<int> S;
    while (!flag) {
      long long tmp = cur;
      while (tmp) {
        S.insert(tmp % 10);
        tmp /= 10;
      }
      if (S.size() == 10) {
        flag = true;
        std::cout << cur << std::endl;
      }
      cur += n;
    }
  }
  return 0;
}
