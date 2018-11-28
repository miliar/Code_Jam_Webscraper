#include <iostream>
#include <string>

const int SMAX = 1005;

// number of Poeple with Shyness Level Less Than
unsigned int numPSLLT[SMAX];

void printNumPSLLT(unsigned int N) {
	std::cout << "numPSLLT[0.." << N << "]:" << std::endl;
	for (unsigned int i = 0; i <= N; i++)
		std::cout << numPSLLT[i] << " ";
	std::cout << std::endl;
}

void solve() {
	unsigned int Smax;
	std::string shyness;
	
	std::cin >> Smax >> shyness;
	
	unsigned int addition = 0;
	
	numPSLLT[0] = 0;
	for (unsigned int i = 1; i <= Smax; i++) {
		numPSLLT[i] = numPSLLT[i-1] + (unsigned int)(shyness[i-1]-'0');
		if (numPSLLT[i] + addition < i)
			addition += i - numPSLLT[i] - addition;
	}
	
	std::cout << addition << std::endl;
}

int main() {
	unsigned int T;
	
	std::cin >> T;
	for (unsigned int i = 0; i < T; i++) {
		std::cout << "Case #" << i+1 << ": ";
		solve();
	}
	
	return 0;
}