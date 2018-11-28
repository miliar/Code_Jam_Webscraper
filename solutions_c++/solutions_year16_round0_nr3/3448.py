#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cassert>

std::string output(int number) {
  std::string str(16, '0');
  for (int i = 0; i < 16; i++) {
    if ((1 << i) & number) {
      str[i] = '1';
    }
  }
  std::reverse(str.begin(), str.end());
  return str;
}

inline long long p(int a, int x) {
  long long ret = 1LL;
  for (int i = 0; i < x; i++) {
    ret *= a;
  }
  return ret;
}

int divisor(long long ans) {
  for (int i = 2; (long long)i * i <= ans; i++) {
    if (ans % i == 0) {
      return i;
    }
  }
  return 1;
}

int main() {
  int num = 0;
  printf("Case #%d:\n", 1);
  for (int i = 1 + (1 << 15); i < (1 << 16); i += 2) {
    auto s = output(i);
    bool flag = false;
    std::vector<std::pair<long long, int>> V;
    for (int base = 2; base <= 10; base++) {
      long long ans = 0;
      for (int digit = 0; digit < 16; digit++) {
        if (s[digit] == '1') {
          ans += p(base, 15-digit);
        }
      } 
      int div = divisor(ans);
      if (div == 1) {
        flag = true; 
        break;
      } else {
        V.push_back(std::make_pair(ans, div));
      }
    }
    if (!flag) {
      std::cout << s << ' ';
      assert(V.size() == 9);
      for (auto &elem : V) {
        std::cout << elem.second << ' '; 
        // std::cout << elem.first << ' ' << elem.second << ' ';
      }
      std::cout << std::endl;
      num ++;
    }
    if (num == 50) {
      break;
    }
  }
  return 0;
}
