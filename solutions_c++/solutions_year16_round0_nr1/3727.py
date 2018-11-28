#include <iostream>
#include <vector>

int count(long n) {
  int curr = n;
  std::vector<bool> v(10, false);
  int unique_cnt = 0;
  while (true) {
    int t = curr;
    while (t > 0) {
      int digit = t % 10;
      if (!v[digit]) {
        v[digit] = true;
        ++unique_cnt;
      }
      t /= 10;
    }
    if (unique_cnt == 10) {
      return curr;
    }
    curr += n;
  }
}

int main() {
  int sz;
  std::cin >> sz;
  for (int i = 1; i <= sz; ++i) {
    long n;
    std::cin >> n;
    std::cout << "Case #" << i << ": ";
    if (n == 0) {
      std::cout << "INSOMNIA" << std::endl;
    } else {
      std::cout << count(n) << std::endl;
    }
  }
}