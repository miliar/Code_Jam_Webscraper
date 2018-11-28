#include <iostream>
#include <string>

const std::string impossible = "impossible";

int main() {
  int T;
  std::cin >> T;

  for (int i = 1; i <= T; ++i) {
    std::cout << "Case #" << i << ": ";

    std::string tmp;
    std::cin >> tmp;

    long P, Q;
    auto slash = tmp.find('/');
    P = std::atol(tmp.substr(0, slash).c_str());
    Q = std::atol(tmp.substr(slash + 1).c_str());

    auto check_pow2 = [](long q) {
      while(q) {
        if (q%2 == 1 && q != 1) return false;
        q /= 2;
      }
      return true;
    };

    auto nod = [](long p, long q) {
      long a, b;
      if (p > q) { a = p; b = q; }
      else { a = q; b = p; }

      while (a%b) {
        long tmp_b = a%b;
        a = b;
        b = tmp_b;
      }

      return b;
    };

    int result = 0;
    auto my_nod = nod(P, Q);
    P /= my_nod;
    Q /= my_nod;
    if (!check_pow2(Q)) std::cout << impossible;
    else {
      while(P < Q) {
        Q /= 2;
        result++;
      }
      std::cout << result;
    }

    std::cout << std::endl;
  }
}
