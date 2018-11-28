#include <iostream>
#include <math.h>
#include <bitset>
#include <vector>
#include <string>
#include <sstream>

// using namespace std;

bool prime_digit(long long x)
{
  if (x < 2) return false;
  for(long long i=2; i<= sqrt(x); i++) {
    if ((x%i) == 0) return false;
  }
  return true;
}

bool prime_array(std::vector<long long> vec) {
	for (long long i = 0; i < 10; i++) {
		if (prime_digit(vec[i]) == true) {
			return false;
		}
	}

	return true;
}

std::string binary_(long long num, int size_) {
 	std::string temp = "";
 	long long rem = 0;

 	while (num > 0) {
 		rem = num % 2;
 		temp = std::to_string(rem) + temp;
 		num = num / 2;
 	}

 	int diff = size_ - temp.length();

 	for (int i = 0; i < diff; i++) {
 		temp = "0" + temp;
 	}

 	return ("1" + temp + "1");
}

std::vector<long long> toBin_(long long number_) {
	std::vector <long long> temp;

	if (number_ == 2) {
		temp.push_back(11);
		return temp;
	} else {
		long long max_ = pow(2,number_ - 2);

		for (long long i = 0; i < max_; i++) {
			std::string binary = binary_(i, number_ - 2);
			std::stringstream ss2(binary); 
			long long result; ss2 >> result;

			temp.push_back(result);
		}

		return temp;
	}
}

std::vector<long long> genBase(long long number) {
	std::vector<long long> temp_vec;

	for (int i = 2; i <= 10; i++) {
		std::string temp = std::to_string(number);
		long long result = 0;

		for (int j = temp.size() - 1; j >= 0; j--) {
			if (temp[j] == '1') {
				result = result + pow(i, temp.size() - 1 - j);
			}
		}

		temp_vec.push_back(result);
	}

	return temp_vec;
}

std::vector <long long> genDivisors(long long number) {
	std::vector <long long> temp = genBase(number);
	std::vector <long long> div_list;

	for (int j = 0; j < temp.size(); j++) {
		for (int i = 2; i < number - 1; i++) {
			if (temp[j] % i == 0) {
				div_list.push_back(i);
				break;
			}
		}
	}

	return div_list;
}

int main() {
	int number_of_test_cases; std::cin >> number_of_test_cases;
	std::cout << ("Case #" + std::to_string(number_of_test_cases) + ":") << std::endl;

	// std::cout << "HERE" << std::endl;

	int n; std::cin >> n;
	int j; std::cin >> j;

	std::vector <long long> old_list = toBin_(n);

	std::vector <long long> new_list;

	// std::cout << "HERE" << std::endl;

	for (int i = 0; i < old_list.size() / 100; i++) {
		std::vector <long long> temp = genBase(old_list[i]);
		if (prime_array(temp) == true) {
			new_list.push_back(old_list[i]);
		}

		// std::cout << "RUNNING" << std::endl;
	}

	// std::cout << "HERE" << std::endl;

	// std::cout << std::endl;

	for (int i = 0; i < j; i++) {
		std::cout << new_list[i] << " ";
		std::vector <long long> temp;

		temp = genDivisors(new_list[i]);

		for (int i = 0; i < temp.size(); i++) {
			std::cout << temp[i] << " ";
		}

		std::cout << std::endl;
	}	
    return 0;

    std::cout << "HERE" << std::endl;
}
