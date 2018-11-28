// cat input.in | ./a.out > output
#include <iostream>
#include <vector>


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







// has to print everything except "Case #n: " and eol \n
// read from std::cin
void handle_case() {
	myint n;
	std::cin >> n;
	if(n==0) {
		std::cout << "INSOMNIA";
		return;
	}
	int sign = +1;
	if(n<0) {
		n *= -1;
		sign = -1;
	}
	
	myint initn = n;
	
	bool seen[10] = {false};
	while(true) {
		myint tmpn = n;
		while(tmpn > 0) {
			seen[tmpn%10] = true;
			tmpn = tmpn/10;
		}
		
		bool all_seen = true;
		for(bool s: seen) {
			if(!s) all_seen = false;
		}
		
		if(all_seen) {
			break;
		} else {
			n += initn;
			if(n<0)
				std::cerr << "Overflow error!" << std::endl;
		}
	}
	
	std::cout << (n*sign);
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
