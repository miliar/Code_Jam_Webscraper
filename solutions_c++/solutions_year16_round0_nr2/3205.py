#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <unordered_map>
#include <numeric>
#include <deque>


template<typename T>
std::vector<T> space_split_string(std::string& input)
{
  std::stringstream ss(input);
  std::vector<T> return_value;
  T value;
  while (ss >> value)
  {
    return_value.push_back(value);
  }
  return return_value;
}

template<typename T>
std::string print_results(const std::vector<T>& results)
{
  std::stringstream output;
  int case_number = 1;
  for (auto result : results) {
    output << "Case #" << case_number << ": " << result << std::endl;
    case_number++;
  }
  return output.str();
}

std::string flip_stack(std::string input)
{
  std::string output;
  for (size_t i = 0; i < input.size(); i++) {
    if (input[i] == '+') {
      output.push_back('-');
    } else {
      output.push_back('+');
    }
  }
  std::reverse(output.begin(), output.end());
  return output;
}

int main(int argc, char** argv)
{
  if (argc < 2) {
    return -1;
  }
  std::ifstream input_file(argv[1]);
  if (!input_file.is_open()) {
    return -1;
  }
  std::string num_cases_str;
  std::getline(input_file, num_cases_str);
  int num_cases = std::stoi(num_cases_str);

  std::vector<int> result;
  for (int i = 0; i < num_cases; i++) {
    std::string stack;
    std::getline(input_file, stack);
    int num_flips = 0;
    //printf("%s\n", stack.c_str());
    while (true) {
      // Find first minus from the right
      auto last_minus = std::find(stack.rbegin(), stack.rend(), '-');
      // Get rid of the correctly positioned pancakes
      stack.erase(last_minus.base(), stack.end());
      if (stack.size() == 0) break;
      // Find first minus from the left
      auto first_minus = std::find(stack.begin(), stack.end(), '-');
      // Flip all first pluses if there are any
      if (first_minus != stack.begin()) {
        auto begin_flip = flip_stack(std::string(stack.begin(), first_minus));
        stack.replace(stack.begin(), first_minus, begin_flip);
        num_flips++;
        //printf("First flip: %s\n", stack.c_str());
      }
      // Flip the whole remaining stack
      stack = flip_stack(stack);
      num_flips++;
      //printf("Second flip: %s\n", stack.c_str());
    }
    result.push_back(num_flips);
  }

  std::string result_str = print_results(result);

  std::ofstream output_file(argv[2]);
  if (output_file.is_open())
  {
    output_file << result_str;
    output_file.close();
  }

  return 0;
}
