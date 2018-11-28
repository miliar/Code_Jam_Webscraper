#include <iostream>
#include <set>

int LastValue(int n)
{
  std::set<int> s;
  for (int i = 0; i < 10; i++) {
    s.insert(i);
  }
  int i = 1;
  while (s.size()) {
    int x = n * i++;
    while (x) {
      s.erase(x%10);
      x /= 10;
    }
  }
  return n * (i-1);
}

int main()
{
  int T;
  std::cin >> T;
  for (int i = 1; i <= T; i++) {
    int n;
    std::cin >> n;
    std::cout << "Case #" << i << ": ";
    if (n == 0) {
      std::cout << "INSOMNIA" << std::endl;
    } else {
      std::cout << LastValue(n) << std::endl;
    }
  }
}
