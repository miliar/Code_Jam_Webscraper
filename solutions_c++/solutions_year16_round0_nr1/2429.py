#include <iostream>
#include <fstream>
#include <vector>

std::fstream in("input.txt");
std::fstream out("output.txt");

long FindWhenToSleep(long number) {
  std::vector<bool> ints_found(11);
  long current_number = number;
  while (!ints_found[10]) {
    ints_found[10] = true;
    long buf = current_number;
    int completed = 0;
    while (buf != 0) {
      ints_found[buf%10] = true;
      buf /= 10;
    }
    for (int i = 0; i < 10; ++i) {
      ints_found[10] = ints_found[10] && ints_found[i];
      completed += ints_found[i];
    }
    if (completed == 0) {
      return -1;
    }
    current_number += number;
  }
  return current_number - number;
}

int main() {
  int data_size;
  in >> data_size;
  std::vector<int> numbers(data_size);
  for (int i = 0; i < data_size; ++i) {
    in >> numbers[i];
  }
  for (int i = 0; i < data_size; ++i) {
    long number = FindWhenToSleep(numbers[i]);
    if(number != -1) {
      out << "Case #" << i + 1 << ": " << number << "\n";
    } else {
      out << "Case #" << i + 1 << ": INSOMNIA\n";
    }
  }
  return 0;
}
