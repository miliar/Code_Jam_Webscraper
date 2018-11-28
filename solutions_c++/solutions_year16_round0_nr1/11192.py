#include <iostream>
#include "math.h"

int main() {

  int T,N;
  std::cin>>T;
  for (int i = 1; i <= T; i++) {
    std::cin >> N;
    if (N==0) {
      std::cout << "Case #"<<i<<":"<<" INSOMNIA" << std::endl;
    }
    else {
      int count = 1;
      int a[10] = {0};
      while (true) {
        int T = count * N;
        int J = T;
        while (T) {
          int digit = T % 10;
          a[digit] = 1;
          T = T/10;
        }
        int sum = 0;
        for (int i = 0; i<10; i++) {
          sum = sum + a[i];
        }
        if (sum == 10) {
          std::cout <<  "Case #"<<i<<": "<< J << std::endl;
          break;
        }
        else {
          count++;
        }
      }
    }
  }
  return 0;
}
