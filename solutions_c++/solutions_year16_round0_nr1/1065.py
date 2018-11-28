#include <iostream>
#include <array>
#include <cassert>

using Hist = std::array<bool, 10>;

int fallAsleep(int n)
{
  if (!n) {
    return -1;
  }
  
  Hist hist;
  hist.fill(false);
  int digits = 0;

  for (int i = 1; ; ++i) {
    const long long j = (long long)i * n;
    assert (j > 0);

    long long k = j;
    while (k > 0) {
      const int digit = k % 10;

      if (!hist[digit]) {
	hist[digit] = true;
	++digits;
      }

      k /= 10;
    }

    if (digits == 10) {
      return j;
    }
  }
}

int main()
{
  int cases = 0;
  std::cin >> cases;

  for (int i = 1; i <= cases; ++i) {
    int n = 0;
    std::cin >> n;

    std::cout << "Case #" << i << ": ";
    const int last = fallAsleep(n);

    if (last < 0) {
      std::cout << "INSOMNIA";
    }
    else {
      std::cout << last;
    }

    std::cout << std::endl;
  }
  
  return 0;
}
