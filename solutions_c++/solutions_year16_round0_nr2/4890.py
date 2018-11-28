#include <iostream>
#include <fstream>

int main() {
  std::ifstream problem;
  problem.open("input.in");
  std::ofstream output;
  output.open("output.txt");
  std::string test_cases;
  std::getline(problem, test_cases);
  //  int number_of_test_cases = std::stoi(test_cases);
  int current_test_case = 1;
  //scan and record all sign changes
  while (std::getline(problem, test_cases)) {
    // true if sign is positive, false if negative
    bool current_sign = (test_cases[0] == '+') ? true : false;
    int number_of_sign_changes = 0;
    for (int i = 0; i < test_cases.size(); ++i) {
      if (current_sign != (test_cases[i] == '+')) {
	++number_of_sign_changes;
	current_sign = !current_sign;
      }
      // if the last sign is negative, add one more
      if ((i == test_cases.size() - 1) && (test_cases[i] == '-')) {
	++number_of_sign_changes;
      }
    }
    output << "Case #" << current_test_case << ": " << number_of_sign_changes << std::endl;
    ++current_test_case;
  } 
}
