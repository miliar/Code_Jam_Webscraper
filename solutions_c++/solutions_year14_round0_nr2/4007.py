#include <iostream>

int main() {
  std::cout.precision(7);
  int n;
  double c, f, x;
  double rate, nextCurr, nextRate, t;

  std::cin >> n;
  
  for(int i=0; i<n; i++) {
    std::cin >> c >> f >> x;
    rate = 2;
    t = 0;

    while(true) {
      nextRate = rate + f;
      if( (x/rate) < ((c/rate) + (x/nextRate))) {
        t += (x/rate);
        break;
      } else {
        t += c/rate;
        rate = nextRate;
      }
    }
    std::cout << std::fixed << "Case #" << i+1 << ": " << t << std::endl;
  }

  return 0;
}
