#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <iterator>
#include <cstdint>
#include <deque>
#include <string>

/*
1 2 4 8 16 32 64 
*/

long long counting_sheep(long long sheep) {
  std::vector<bool> visited(10, false);
  auto countdown = visited.size();
  std::string string_number;
  long long count = 0;
  do {
    if (count * sheep < 0) {
      std::cout << "DS\n";
    }
    count++;
    string_number = std::to_string(count * sheep);
    for (auto sym : string_number) {
      int i = (sym - 48) % 10;
      if (visited[i] == false) {
        countdown--;
        visited[i] = true;  
      }
    }
  } while (countdown > 0);
  return count * sheep;
}

int main() {
  long long n, x;
  std::cin >> n;
  for (long long i = 0; i < n; i++) { 
    std::cin >> x;
    if (x != 0) {
      std::cout << "Case #" << i + 1 << ": " << counting_sheep(x) << std::endl;
    } else {
      std::cout << "Case #" << i + 1 << ": " << "INSOMNIA" << std::endl;
    }
  }
  return 0;
}
