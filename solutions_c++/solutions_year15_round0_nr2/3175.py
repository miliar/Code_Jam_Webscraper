#include <iostream>
#include <queue>

const int MAXPI = 1005;

unsigned int pancake[MAXPI], D;

unsigned int ceil(unsigned int a, unsigned int b) {
	unsigned int c = a/b;
	return c + (a > b*c);
}

unsigned int numStop(unsigned int maxWait) {
	unsigned int operation = 0;
	for (int i = 0; i < D; i++)
		if (pancake[i] > maxWait)
			operation += ceil(pancake[i], maxWait) - 1;
	return operation;
}

void solve() {
	unsigned int maxP = 0;
	
	std::cin >> D;
	for (unsigned int i = 0; i < D; i++) {
		std::cin >> pancake[i];
		if (pancake[i] > maxP)
			maxP = pancake[i];
	}
	
	unsigned int best = maxP;
	for (unsigned int max_wait = 1; max_wait <= maxP; max_wait++) {
		unsigned int operation = numStop(max_wait);
		if (max_wait + operation < best)
			best = max_wait + operation;
	}
	
	std::cout << best << std::endl;
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