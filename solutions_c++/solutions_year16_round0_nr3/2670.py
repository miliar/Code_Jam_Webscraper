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
    int64_t numdigits = data[0];
    int64_t numjamcoins = data[1];

    std::vector<int> digits;
    for (int i = 0; i < numdigits; i++) {
      if (i == 0 || i == numdigits - 1) {
        digits.push_back(1);
      } else {
        digits.push_back(0);
      }
    }

    std::stringstream case_result;
    case_result << std::endl;
    std::vector<int64_t> divisors;
    int found_jamcoins = 0;
    while (found_jamcoins < numjamcoins && increase_digits(digits)) {
      // Interpret as binary
      bool is_prime;
      divisors.clear();
      for (int i = 2; i < 11; i++) {
        // Interpret in base i
        int64_t value = interpret_digits(digits, i);
        // Find divisor
        int64_t divisor;
        is_prime = find_divisor(value, divisor);
        divisors.push_back(divisor);
        if (is_prime)
          break;
      }
      if (!is_prime)
      {
        // Good jamcoin
        std::string jamcoin_result = print_digits(digits) + print_divisors(divisors);
        case_result << jamcoin_result << std::endl;
        found_jamcoins++;
        printf("%s\n", jamcoin_result.c_str());
      }
    }
    std::string case_result_str = case_result.str();
    case_result_str.pop_back();
    result.push_back(case_result_str);
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
