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

  std::vector<std::string> result;
  for (int i = 0; i < num_cases; i++) {
    std::string number_str;
    std::getline(input_file, number_str);
    int number = std::stoi(number_str);
    int original_number = number;

    if (number == 0) {
      result.push_back("INSOMNIA");
    }
    else {
      int digits[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
      while (true)
      {
        int tmp_number = number;
        while (true) {
          digits[tmp_number % 10] += 1;
          tmp_number /= 10;
          if (tmp_number == 0) break;
        }
        bool all_digits = true;
        for (int i = 0; i < 10; i++) {
          if (digits[i] == 0) {
            all_digits = false;
          }
        }
        if (all_digits) break;
        number += original_number;
      }
      result.push_back(std::to_string(number));
    }

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
