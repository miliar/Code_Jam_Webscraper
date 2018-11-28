#include <iostream>
#include <string>
#include <vector>

int main() {
  // Read parameters
    int cases;
    std::cin >> cases;

  for (int c = 1; c <= cases; c++) {
      int n;
      std::cin >> n;
      std::cin.ignore();
      
      int count = 0;
      int adds = 0;
      
      
      for (int i = 0; i <= n; i++) {
          char s[2];
          std::cin.get (s,2);
          int shy = std::stoi(s);
          
          if (i > count) {
            adds += i - count;
            count += i - count;
          }
          count += shy;
      }
      
    std::cout << "Case #" << c << ": " << adds << '\n';
  }
  return 0;
}
