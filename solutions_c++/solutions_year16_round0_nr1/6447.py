#include <iostream>
#include <set>
#include <functional>

void digitize(int num, std::function<void(int)> fn) {
  while (num > 9) {
    fn(num % 10);
    num /= 10;
  }
  fn(num);
}

int main(int argc, char* argv[])
{
  int T, j;
  for (std::cin >> T, j = 0; j < T; ++j) {
    std::cout << "Case #" << j + 1 << ": ";
    int N;
    std::cin >> N;
    if (N == 0) {
      std::cout << "INSOMNIA\n";
    } else {
      std::set<int> s;
      auto i = 1;
      for (; s.size() < 10; ++i) {
        digitize(N * i, [&s](int num) {
            s.insert(num);
        });
      }
      std::cout << N * (i - 1) << '\n';
    }
  }


  return 0;
}
