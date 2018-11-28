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

using sliced = std::vector<std::string::iterator>;

sliced slice(std::string& str) {
  sliced result;
  auto it = str.begin();
  result.push_back(it);
  while(it != str.end()) {
    it = std::find_if(it, str.end(), [it](char c) { return c != *it; });
    result.push_back(it);
  }
  return result;
}

int count_segments(std::string const& str) {
  int segments = 0;
  auto it = str.begin();
  while(it != str.end()) {
    it = std::find_if(it, str.end(), [it](char c) { return c != *it; });
    segments++;
  }
  return segments;
}

int main() {
  int T; std::cin >> T;
  for(int i = 0; i < T; ++i) {
    std::cout << "Case #" << (i+1) << ": "; 
    std::string stack;
    std::cin >> stack;
    int steps_required = 0;
    if(stack == "") { std::cout << "0" << std::endl; continue; }
    steps_required = count_segments(stack) - 1;
    if(stack[stack.size() - 1] != '+') steps_required++;
    std::cout << steps_required << std::endl;
  }
}
