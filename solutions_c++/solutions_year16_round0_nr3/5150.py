#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <cmath>
#include <iterator>

bool is_prime(long long x) {
	for (long long i = 2; i <= sqrt(x); ++i) {
		if (x % i == 0) {
			return false;
		}
	}
	return true;
}

long long find_divisor(long long x) {
	for (long long i = 2; i <= x; ++i) {
		if (x % i == 0) {
			return i;
		}
	}
}

//
std::vector<std::string> get_binary(unsigned int n)
{
    std::vector<std::string> result;

    if (n <= 1)
    {
        result.push_back("0");
        result.push_back("1");
    }
    else
    {   // recurse, then add extra bit chars
        std::vector<std::string> sub = get_binary(n-1);
        for (std::vector<std::string>::const_iterator it = sub.cbegin(); it != sub.cend(); ++it) {
            result.push_back(*it+'0');
            result.push_back(*it+'1');
        }
    }
    return result;
}

int main() {
	std::string line;
	int c = 0;
	// get the line
	while (std::getline(std::cin, line)) {
		if (c == 0) {
			++c;
			continue;
		}
		// put the line in a stringstream
		std::stringstream stream(line);
		// parse
		int n;
		std::vector<int> v;
		while (stream >> n) {
			v.push_back(n);
		}

		std::cout << "Case #1:" << std::endl;

		int N = v[0];
		int J = v[1];

		std::vector<long long> all_j;

		std::vector<std::string> binary_v = get_binary(N);

		for (int i = 0; i < binary_v.size(); ++i) {
			std::string temp = binary_v[i];
			if (temp[0] != '1') {
				continue;
			}
			else if (temp[temp.size()-1] != '1') {
				continue;
			}
			else {
				all_j.push_back(std::stoll(temp));
			}
		}

		int num_cases_printed = 0;
		for (int i = 0; i < all_j.size(); ++i) {
			//
			std::vector<long long> temp_v;
			bool at_least_one_prime = false;
			
			for (int j = 2; j <= 10; ++j) {
				long long temp = all_j[i];
				long long number = 0;
				int counter = 0;
				while (temp > 0) {
					int digit = temp % 10;
					number += digit * pow(j, counter);
					++counter;
					temp /= 10;
				}
				temp_v.push_back(number);
			}
			for (int j = 0; j < temp_v.size(); ++j) {
				// if one of the base representation is a prime
				if (is_prime(temp_v[j])) {
					at_least_one_prime = true;
					break;
				}
			}
			if (at_least_one_prime) {
				continue;
			}
			
			std::vector<long long> divisors;
			for (int j = 0; j < temp_v.size(); ++j) {
				divisors.push_back(find_divisor(temp_v[j]));
			}

			std::cout << all_j[i] << " ";

			for (int j = 0; j < divisors.size(); ++j) {
				std::cout << divisors[j];
				if (j != divisors.size() - 1) {
					std::cout << " ";
				}
			}
			std::cout << std::endl;

			++num_cases_printed;
			if (num_cases_printed == J) {
				break;
			}
		}

	}
    return 0;
}


