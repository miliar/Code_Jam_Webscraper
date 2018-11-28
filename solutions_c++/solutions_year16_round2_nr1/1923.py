// cat input.in | ./a.out > output
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>


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



std::string names[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
std::string magic[] = {"Z", "O", "W", "R", "U", "F", "X", "S", "G", "I"};

void find_and_remove(std::vector<int> &digits, std::string &s, int d) {
	while(s.find(magic[d]) != std::string::npos) {
		//std::cerr << "found " << d << std::endl;
		digits.push_back(d);
		for(char c: names[d]) {
			int i = s.find(c);
			//std::cerr << s << i << std::endl;
			if(i == std::string::npos) std::cerr << "ERROR!"<<std::endl;
			s.erase(i,1);
		}
	}
}

// has to print everything except "Case #n: " and eol \n
// read from std::cin
void handle_case() {
	std::string s;
	std::cin >> s;
	
	std::vector<int> digits;
	
	find_and_remove(digits, s, 0);
	find_and_remove(digits, s, 2);
	find_and_remove(digits, s, 4);
	find_and_remove(digits, s, 6);
	find_and_remove(digits, s, 8);
	
	find_and_remove(digits, s, 1);
	find_and_remove(digits, s, 3);
	find_and_remove(digits, s, 5);
	find_and_remove(digits, s, 7);
	
	find_and_remove(digits, s, 9);
	
	std::sort(digits.begin(), digits.end());
	
	for(int i:digits) std::cout << i;
}


int main() {
	int num_cases;
	std::cin >> num_cases;
	for(int tcase = 1; tcase <= num_cases; tcase++) {
		std::cout << "Case #" << tcase << ": ";
		handle_case();
		std::cout << std::endl;
	}
}
