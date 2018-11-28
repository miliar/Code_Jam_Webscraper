#include <iostream>
#include <float.h>

#define CPS 2.0

int main(int argc, char* argv[]) {
  int test_cases = 0;
  std::cin >> test_cases;
  std::cout.precision(7);
  for (int i = 0;i < test_cases;i++) {
    double c, f, x;
    std::cin >> c >> f >> x;
    double rate = CPS;
    double best = DBL_MAX;
    double t = 0.0;
    int a = 0;
    do {
      double next = x / rate + t;
      if (best > next) best = next;
      else break;
      t += c / rate;
      a++;
      rate += f;
    } while (t < best);
    std::cout << "Case #" << (i+1) << ": " << std::fixed << best << std::endl;
  }
}

