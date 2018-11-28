#include <iostream>
#include <unordered_set>
#include <unordered_map>
#include <fstream>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <numeric>
#include <iterator>

std::unordered_set<int> digits(int v) {
  std::unordered_set<int> result;
  while(v > 0) {
    result.insert(v % 10);
    v /= 10;
  }
  return result;
}

int main() {
  int T; std::cin >> T;
  for(int i = 0; i < T; ++i) {
    std::cout << "Case #" << (i+1) << ": "; 
    int N; std::cin >> N;
    if(N == 0) { std::cout << "INSOMNIA" << std::endl; continue; }
    std::unordered_set<int> seen_digits = digits(N);
    int V = N;
    while(seen_digits.size() != 10) {
      auto new_digits = digits(V += N);
      seen_digits.insert(new_digits.begin(), new_digits.end());
    }
    std::cout << V << std::endl;
  }
}
