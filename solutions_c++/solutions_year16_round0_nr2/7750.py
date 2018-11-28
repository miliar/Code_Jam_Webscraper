#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

void solve(const size_t case_number, const size_t solution) {
  cout << "Case #" << case_number << ": ";
  cout << solution;
  cout << "\n";
}

size_t get_pancakes() {
  string line;
  getline(std::cin, line);
  assert(!line.empty());

  auto count = 0u;
  char last = line.front();
  for (char c : line) {
    if (c != last)
      ++count;
    last = c;
  }

  if (last != '+')
    ++count;

  assert(!std::cin.fail());

  return count;
}

int main() {
  auto t = 0u;

  std::cin >> t >> ws;
  assert(std::cin.good());

  for (auto i = 1u; i <= t; ++i) {
    auto count = get_pancakes();
    solve(i, count);
  }
  assert(std::cin.eof());
}
