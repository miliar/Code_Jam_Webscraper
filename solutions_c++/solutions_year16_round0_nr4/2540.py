#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <unordered_map>
#include <numeric>
#include <deque>
#include <cmath>


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

bool increase_digits(std::vector<int>& digits)
{
  // Exclude first and last digit
  std::vector<int> working_digits(digits.begin() + 1, digits.end() - 1);
  // Find last zero and change it one and all the following ones to zeros
  auto lastzero = std::find(working_digits.rbegin(), working_digits.rend(), 0);
  if (lastzero == working_digits.rend()) {
    // Maximum value reached return false
    return false;
  }
  *lastzero = 1;
  std::fill(lastzero.base(), working_digits.end(), 0);
  std::copy(working_digits.begin(), working_digits.end(), digits.begin() + 1);
  return true;
}

int64_t interpret_digits(const std::vector<int>& digits, int base)
{
  int64_t return_value = 0;
  int exponent = digits.size() - 1;
  for (auto d : digits) {
    return_value += d * pow(base, exponent);
    exponent--;
  }
  return return_value;
}

bool find_divisor(int64_t value, int64_t& divisor)
{
  for (int64_t i = 2; i < sqrt(value); i++) {
    if (value % i == 0) {
      // Divisor was found
      divisor = i;
      return false;
    }
  }
  // Divisor was not found
  return true;
}

std::string print_digits(const std::vector<int>& digits)
{
  std::string return_value;
  for (auto d : digits) {
    if (d == 0) {
      return_value.push_back('0');
    }else{
      return_value.push_back('1');
    }
  }
  return return_value;
}

std::string print_divisors(const std::vector<int64_t>& divisors)
{
  std::stringstream output;
  for (auto d : divisors) {
    output << " " << d; 
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
    std::string data_str;
    std::getline(input_file, data_str);
    std::vector<int64_t> data = space_split_string<int64_t>(data_str);
    int64_t K = data[0];
    int64_t C = data[1];
    int64_t S = data[2];

    if (S != K) {
      printf("S is not equal to K!\n");
      return -1;
    }
    std::stringstream tiles_to_uncover;
    for (int i = 0; i < K; i++) {
      tiles_to_uncover << i + 1 << " ";
    }
    std::string tiles_to_uncover_str = tiles_to_uncover.str();
    tiles_to_uncover_str.pop_back();

    result.push_back(tiles_to_uncover_str);
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
