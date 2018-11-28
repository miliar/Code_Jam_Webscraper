#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <bitset>
#include <utility>
#include <vector>

std::pair<bool, std::vector<int>> get_jamcoin(long number);

int main() {
  std::ifstream input_cases;
  input_cases.open("input.in");
  std::ofstream output_cases;
  output_cases.open("output.txt");
  output_cases << "Case #1:" << std::endl;
  std::string input;
  std::getline(input_cases, input);
  std::getline(input_cases, input);
  std::stringstream input_stream(input);
  std::string throw_away;
  long length_of_jamcoin;
  long number_of_coins_to_generate;
  input_stream >> length_of_jamcoin;
  input_stream >> number_of_coins_to_generate;
  long current_number = 1 << (length_of_jamcoin - 1);
  ++current_number;
  while (number_of_coins_to_generate) {
    auto jamcoin = get_jamcoin(current_number);
    if (jamcoin.first) {
      std::string bitstring = std::bitset<64>(current_number).to_string();
      bitstring.erase(0, bitstring.find_first_not_of('0'));
      output_cases <<  bitstring << " ";
      for (auto i = jamcoin.second.begin(); i != jamcoin.second.end(); ++i) {
	      output_cases << *i << " ";
      }
      output_cases << std::endl;
      --number_of_coins_to_generate;
    }
    current_number += 2;
  }
}

// interprets number as base specified in the base param,
// then converts that number to base 10
long interpret_and_convert_base(long base, std::string number) {
  long interpreted_number = 0;
  for (long i = number.size() - 1, current_multiplier = 1; i >= 0; --i, current_multiplier *= base) {
    if (number[i] == '1') {
      interpreted_number += current_multiplier;
    }
  }
  return interpreted_number;
}

// adapted prime number checker
long get_first_divisor(long number) {
  if (number % 2 == 0) {
    return 2;
  }
  for (long i = 3; i * i < number; i += 2) {
    if (number % i == 0) {
      return i;
    }
  }
  return -1;
}

// checks if a number is a jamcoin and returns its divisors if it is
std::pair<bool, std::vector<int>> get_jamcoin(long number) {
  std::string bitstring = std::bitset<64>(number).to_string();
  bitstring.erase(0, bitstring.find_first_not_of('0'));
  std::vector<int> divisors;
  // check the number is composite from base 2 to base 10
  for (long i = 2; i < 11; ++i) {
    long number_to_check = interpret_and_convert_base(i, bitstring);
    long divisor = get_first_divisor(number_to_check);
    if (divisor < 0) {
      return std::make_pair(false, std::vector<int>());
    } else {
      divisors.push_back(divisor);
    }
  }
  return std::make_pair(true, divisors);
}
