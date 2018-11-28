#include <iostream>
#include <fstream>
#include <vector>
#include <string>

std::fstream in("input.txt");
std::fstream out("output.txt");

long CountAnswer(std::string str) {
  char prev = 'a';
  long counter = 0;
  for (size_t i = 0; i < str.length(); ++i) {
//    std::cout << prev << ' ' << str[i] << "\n";
    if (str[i] != prev) {
      ++counter;
      prev = str[i];
    }
  }
  if (prev == '+') {
    --counter;
  }
  return counter;
}

int main() {
  int data_size;
  in >> data_size;
  std::vector<std::string> pancakes_sets(data_size);
  for (int i = 0; i < data_size; ++i) {
    in >> pancakes_sets[i];
  }
  for (int i = 0; i < data_size; ++i) {
    long answer = CountAnswer(pancakes_sets[i]);
    out << "Case #" << i + 1 << ": " << answer << "\n";
  }
  return 0;
}
