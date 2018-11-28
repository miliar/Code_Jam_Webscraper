// cat input.in | ./a.out > output
#include <iostream>
#include <vector>
#include <cmath>
#include <bitset>
#include <iomanip>


typedef long long myint;

template <typename T>
std::vector<T> read_vector(int length, std::istream& in = std::cin) {
	std::vector<T> vector;
	for(; length>0; length--) {
		T item;
		in >> item;
		vector.push_back(item);
	}
	return vector;
}

// jamcoins are saved as myint in base 2

// return divisor or 0 if prime
myint find_divisor(myint n) {
	if(n%2 == 0) return 2;
	myint max = sqrt(n)+1;
	for(myint divisor=3; divisor < max; divisor+=2) {
		if(n % divisor == 0) return divisor;
	}
	return 0;
}

myint to_base(myint jamcoin, int base) {
	myint num = 0;
	myint mult = 1;
	while(jamcoin > 0) {
		num += mult * (jamcoin%2);
		if(num < 0)
			std::cerr << "Overflow!" << std::endl;
		jamcoin /= 2;
		mult *= base;
	}
	return num;
}

void print_binary(myint jamcoin, const int length) {
	myint mask = 1;
	mask <<= (length-1);
	while(mask>0) {
		std::cout << ((jamcoin&mask) != 0 ? 1:0);
		mask >>= 1;
	}
	//std::cout << "=" << jamcoin;
}


// has to print everything except "Case #n: "
// read from std::cin
void handle_case() {
	int n, j; // jamcoin length, num of jamcoins to produce
	std::cin >> n >> j;
	
	myint jamcoin_candidate = 1;
	jamcoin_candidate <<= (n-1);
	jamcoin_candidate += 1;
	
	myint max_jamcoin = 1;
	max_jamcoin <<= n;
	
	for(; j>0; jamcoin_candidate+=2) {
		if(jamcoin_candidate >= max_jamcoin) {
			std::cerr << "Not enough valid jamcoins" << std::endl;
			break;
		}
		
		bool is_jamcoin = true;
		std::vector<myint> divisors;
		for(int base=2; base<=10; base++) {
			myint div = find_divisor(to_base(jamcoin_candidate, base));
			if(div != 0) {
				divisors.push_back(div);
			} else {
				is_jamcoin = false;
				break;
			}
		}
		
		if(is_jamcoin) {
			j--;
			print_binary(jamcoin_candidate, n);
			for(myint div: divisors)
				std::cout << " " << div;
			std::cout << std::endl;
		}
	}
	
}


int main() {
	int num_cases;
	std::cin >> num_cases;
	for(int tcase = 1; tcase <= num_cases; tcase++) {
		std::cout << "Case #" << tcase << ": " << std::endl;
		handle_case();
	}
}
