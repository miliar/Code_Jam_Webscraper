#include <iostream>

int solve(std::string S) {
	const size_t length = S.length();

	unsigned flip = 0;

	for(int checker=length-1; checker>=0; --checker) {
		if (S[checker] != '+'){
			++flip;
			for(size_t flipper=0; flipper<=checker; ++flipper) {
				if (S[flipper] == '+'){
					S[flipper] = '-';
				}
				else {
					S[flipper] = '+';
				}
			}
		}
	}
	return flip;
}


int main() {
	unsigned cases;

	std::cin >> cases;

	for(unsigned i=0; i<cases; ++i) {
		std::string S;
		std::cin >> S;

		int solution = solve(S);

		std::cout << "Case #" << i+1 << ": "<< solution << std::endl;
	}

}