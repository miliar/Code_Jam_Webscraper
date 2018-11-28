#include <cmath>
#include <iostream>
#include <unordered_set>

#define RETURN_TYPE std::string
#define DEBUG_MODE 0

void analyze(std::unordered_set<int>& seenDigits, unsigned N) {
	std::string str = std::to_string(N);
	for (char c : str) {
		seenDigits.insert(c - '0');
	}
	/*int before;
	#if DEBUG_MODE
	std::cout << N;
	#endif
	while (N >= 10) {
		before = seenDigits.size();
		seenDigits.insert(N % 10);
		#if DEBUG_MODE
		if (seenDigits.size() > before) {
			std::cout << '\t' << '(' << N % 10 << ") | " << seenDigits.size() << std::endl;
		}
		#endif
		N /= 10;
	}
	before = seenDigits.size();
	seenDigits.insert(N % 10);
	#if DEBUG_MODE
	if (seenDigits.size() > before) {
		std::cout << '\t' << '(' << N % 10 << ") | " << seenDigits.size() << std::endl;
	} else if (N < 10) {
		std::cout << std::endl;
	}
	#endif*/
}

RETURN_TYPE parse(unsigned N){
	std::unordered_set<int> seenDigits;
	for (unsigned i = 1; i <= 1e5; i++) {
		analyze(seenDigits, i * N);
		if (seenDigits.size() == 10) {
			#if DEBUG_MODE
			return std::to_string(N) + std::string(": ") + std::to_string(i * N);
			#else
			//return std::to_string(N) + std::string(": ") + std::to_string(i * N);
			return std::to_string(i * N);
			#endif
		}
	}
	//return std::string("INSOMNIA (") + std::to_string(seenDigits.size()) + std::string(")");
	return "INSOMNIA";
}

int main(){
	int numberOfCases, i = 0;
	unsigned N;
	
	std::cin >> numberOfCases;
	for (int i = 0; i < numberOfCases; i++) {
		std::cin >> N;
		RETURN_TYPE r = parse(N);
		std::cout << "Case #" << (i+1) << ": " << r;
		#if DEBUG_MODE
		std::cout << std::endl << "----------------------------";
		#endif
		if (i != numberOfCases - 1) {
			std::cout << std::endl;
		}
	}
}