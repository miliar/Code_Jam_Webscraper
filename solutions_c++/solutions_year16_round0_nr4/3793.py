#include <iostream>

unsigned long long power(unsigned basic, unsigned index) {
	unsigned long long ret = 1;

	for (unsigned i=0; i<index; ++i) {
		ret = ret*basic;
	}

	return ret;
}

unsigned long long Choose(unsigned K, unsigned C, unsigned long long  Si) {
	unsigned long long chosen = 0;
	for (unsigned long long i=1; i < C; ++i) {
		chosen += power(K, i)*Si;
	}

	return chosen;
}

void solve(unsigned K, unsigned C, unsigned S) {
	if (S != K) { 
		std::cout << " IMPOSSIBLE" << std::endl;
		return;
	}

	if (C == 1) {
		for (unsigned long long i = 0; i < S; ++i) {
			std::cout << " " << i+1;
		}

		std::cout << std::endl;
		return;
	}

	for (unsigned long long i = 0; i < S; ++i) {
		if (i == 0) {
			std::cout << " 1";
		}
		else {
			std::cout << " " << Choose(K, C, i)+(i+1);
		}
	}

	std::cout << std::endl;

	return;
}


int main() {
	unsigned cases;

	std::cin >> cases;

	for(unsigned i=0; i<cases; ++i) {
		unsigned K;
		unsigned C;
		unsigned S;
		std::cin >> K;
		std::cin >> C;
		std::cin >> S;

		std::cout << "Case #" << i+1 << ":";
		solve(K, C, S);
	}

}
