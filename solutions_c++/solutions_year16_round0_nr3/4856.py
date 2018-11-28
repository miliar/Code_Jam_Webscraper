#include <iostream>
#include <cstdio>
#include <streambuf>
#include <array>
#include <cstdio>
#include <string>
#include <bitset>
#include <vector>
#include <fstream>
#include <utility>

template<class T>
class Primes {
	std::vector<T> primes;
	T last_number_tested;
public:
	Primes() {
		primes.push_back(2);
		primes.push_back(3);
		last_number_tested = 3;
	}
	bool is_prime(T number) {
		produce_until(number);
		return std::binary_search(primes.begin(), primes.end(), number);
	}
	bool quick_is_prime(T number) {
		if (last_number_tested >= number) {
			return is_prime(number);
		}

		produce_until_sqrt(number);
		for (const auto& p : primes) {
			if (number % p == 0) {
				return false;
			}
			if (p > number/p) {
				break;
			}
		}
		return true;
	}
	void produce_until_sqrt(T v) {
		while (v/last_number_tested > last_number_tested) {
			push_last_number_tested();
		}
	}
	void produce_until(T v) {
		if (v & 1 == 0) {//if even, just test the previous odd number 
			v--;
		}
		while (v > last_number_tested) {
			push_last_number_tested();
		}
	}
	void print_primes() {
		for (const auto& i : primes) {
			std::cout << i << " ";
		}
		std::cout << std::endl;
	}
	void push_back_primes() {
		while (push_last_number_tested() == false);
	}
	bool push_last_number_tested() {
		last_number_tested += 2;
		for (const auto& i : primes) {
			if (last_number_tested % i == 0) {
				return false;//not prime
			}
			if (i> last_number_tested/i) { // all possible divisors are <= sqrt(v), so, if i^2 > v, it is a prime
				break;//prime
			}
		}

		primes.push_back(last_number_tested);
		return true;//prime
	}
	void save(const char * path) {	
		size_t s = primes.size();
		std::ofstream file(path, std::ios::binary);
		file.write((char*)&s, sizeof(s));
		file.write((char*)primes.data(), sizeof(T) * s);
	}
	void load(const char * path) {
		size_t s;
		std::ifstream file(path, std::ios::binary);
		file.read((char*)&s, sizeof(s));
		primes.resize(s);
		file.read((char*)primes.data(), sizeof(T)*s);
	}
	T non_trivial_divisor(T number) {
		if (last_number_tested >= number) {
			if (is_prime(number)) {
				return 0;
			}
		}

		produce_until_sqrt(number);

		for (const auto& p : primes) {
			if (number % p == 0) {
				return p;
			}
			if (p > number / p) {
				return 0;
			}
		}
		return 0;
	}
};


Primes<long long unsigned> primes;

void problemC(int J = 0, int N = 0) {
	int num_tests;
	if (!N || !J) {
		std::cin >> num_tests;
		std::cin >> J >> N;
	}
	num_tests = 1;

	std::string possible_jamcoin = '1' + std::string(J - 2,'0') + '1';


	auto next_jamcoin = [](std::string& s){
		int i = s.size() - 2;
		while(i < s.size()) {
			if (s[i] == '1') {
				s[i] = '0';
				i--;
			}
			else {
				s[i] = '1';
				break;
			}
		}

		return s.front() == '1';
	};

	int jamcoins_found = 0;

	std::vector<long long unsigned> divisors;
	divisors.reserve(9);

	for (int i = 1; i <= num_tests; i++) {
		std::cout << "Case #" << i << "\n";

		
		while (jamcoins_found < N) {

			std::cerr << "Possible " << possible_jamcoin << "\n";


			divisors.clear();
			bool is_jamcoins = true;
			for (int b = 2; b <= 10; b++) {
				long long unsigned n = std::stoull(possible_jamcoin, NULL, b);
				
				long long unsigned div = primes.non_trivial_divisor(n);
				if (div != 0) {
					divisors.push_back(div);
				}
				else {
					is_jamcoins = false;
					break;
				}
				std::cerr << b << " ";
			}
			std::cerr << "\n";

			if (is_jamcoins) {
				std::cout << possible_jamcoin << " ";
				for (const auto & d : divisors) {
					std::cout << d << " ";
				}
				std::cout << std::endl;

				jamcoins_found++;
			}

			if (!next_jamcoin(possible_jamcoin)) {
				break;
			}
		}
	}
}

int main() {
	std::string name = "Csmall";
	std::string name_input = name + ".in";
	std::string name_output = name + ".out";
	//primes.produce_until_sqrt(10000000000000000 - 1);
	//primes.save("a.primes");
	//std::cout << "!";
	primes.load("a.primes");

	//freopen(name_input.c_str(),"r",stdin);
	freopen(name_output.c_str(),"w",stdout);
	//problemC();

	//problemC(6, 3);
	problemC(16,50);
	getchar();
}