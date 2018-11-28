#include <iostream>
#include <fstream>
#include <vector>

int main() {
  std::ifstream problem;
  problem.open("input_big.in");
  std::ofstream output;
  output.open("output.txt");
  std::string test_cases;
  std::getline(problem, test_cases);
  int number_of_test_cases = std::stoi(test_cases);
  int current_test_case = 1;
  while(std::getline(problem, test_cases)) {
    std::vector<bool> numbers = {false, false, false, false, false, false, false, false, false, false};
    int initial_integer = std::stoi(test_cases);
    int output_integer = -1;
    int i = 0;
    while (output_integer == -1) {
      if (initial_integer == 0) {
	break;
      }
      ++i;
      int current_integer = initial_integer * (i);
      std::string integer_string = std::to_string(current_integer);
      for (char c : integer_string) {
	int number_pos = c - '0';
	numbers[number_pos] = true;
      }
      if (std::all_of(numbers.begin(), numbers.end(), [] (bool v) { return v; })) {
	output_integer = current_integer;
	break;
      }
    }
    if (output_integer == -1) {
      output << "Case #" << current_test_case << ": INSOMNIA" << std::endl;
    } else {
      output << "Case #" << current_test_case << ": " << output_integer << std::endl;
    }
    ++current_test_case;
  }
  return 0;
}
