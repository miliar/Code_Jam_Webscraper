#include <iostream>


int main(int argc, char** argv)
{
  std::cin.tie(0);
  std::ios_base::sync_with_stdio(0);

  int T;
  
  std::cin >> T;

  for (int i = 1; i <= T; i ++) {
    long long r, t;

    std::cin >> r >> t;

    int c = 0;

    for (long long n = 0; ; n += 2, c ++) {
      long long s = 2 * r + (n + 1) * (n + 1) - n * n;

      if (s > t)
        break;

      t -= s;
    }

    std::cout << "Case #" << i << ": " << c << std::endl;
  }
}
