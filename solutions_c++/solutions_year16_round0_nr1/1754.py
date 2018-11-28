#include <iostream>
#include <map>
#include <vector>
#include <deque>
#include <string>

#include <cstdio>
#include <cstdlib>
#include <cstring>

bool full(int* digits) {
  for(int i = 0; i < 10; ++i) 
    if (digits[i] == 0) return false;
  return true;
}

std::string solve() {
  int digits[10] = {0, 0, 0, 0, 0, 
                   0, 0, 0, 0, 0};
  
  char number[200];
  int n;
  std::cin >> n;
  if (n == 0) return std::string("INSOMNIA");
  
  int c = 1;
  
  while (1) {
    snprintf(number, 200, "%d", c * n);
    int l = strlen(number);
    for (int i = 0; i < l; i++) {
      digits[number[i] - '0'] = 1;      
    }
    if (full(digits)) return std::string(number);
    c++;
  }
}

int main(int argc, char* argv[]) {
  int T;
  std::cin >> T;
  for(int t = 1; t <= T; ++t) {
    
    std::string response = solve();
    std::cout << "Case #" << t << ": " << response << std::endl;
  }
  return 0;
}