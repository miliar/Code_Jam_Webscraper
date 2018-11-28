#include <iostream>
#include <algorithm>

int main(int argc, char **argv) {
	size_t T;
	std::cin >> T;
	for(size_t count(0); count < T; ++count) {
		std::string inputString, inputStringCopy;
		std::cin >> inputString;
		inputStringCopy = inputString;

		std::cout << "Case #" << count+1 << ": ";
		size_t flipCount(0);

		// Now we have the input sequence
		auto ii = inputString.begin();
		while(true) {
			while((ii+1 <= inputString.end()-1) && *ii == *(ii+1)) {
				// Greedy advance
				++ii;
			}

			if(ii == (inputString.end()-1)) {
				if(*ii == '+') {
					// We reached the end of input string
					std::cout << flipCount << std::endl;
					break;
				} else if(*ii == '-') {
					++flipCount;
					std::cout << flipCount << std::endl;
					break;
				} else {
					std::cerr << "Something bad..." << std::endl;
				}
				break;
			}

			++flipCount;
			// flip from start to ii
			for(auto it = inputString.begin(); it != ii; ++it) {
				*it = (*it == '-') ? '+' : '-';
			}
			++ii;
		}
	}

}
