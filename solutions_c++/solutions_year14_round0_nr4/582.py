
#include <iostream>
#include <algorithm>

int main() {
	unsigned T;
	std::cin >> T;
	for (unsigned c = 1; c <= T; ++c) {
		unsigned N;
		std::cin >> N;
		double naomi[N], ken[N];
		for (unsigned i = 0; i < N; ++i)
			std::cin >> naomi[i];
		for (unsigned i = 0; i < N; ++i)
			std::cin >> ken[i];
		std::sort(naomi, naomi + N);
		std::sort(ken, ken + N);
		double * naomiPtr = naomi, * kenPtr = ken;
		unsigned naomiDeceitfulScore = 0;
		while (naomiPtr - naomi < N) {
			if (*naomiPtr > *kenPtr) {
				++kenPtr;
				++naomiDeceitfulScore;
			}
			++naomiPtr;
		}
		naomiPtr = naomi + N - 1;
		kenPtr = ken + N - 1;
		unsigned naomiWarScore = 0;
		while (naomiPtr - naomi >= 0) {
			if (*naomiPtr < *kenPtr)
				--kenPtr;
			else
				++naomiWarScore;
			--naomiPtr;
		}
		std::cout << "Case #" << c << ": " << naomiDeceitfulScore << " " << naomiWarScore << std::endl;
	}
	return 0;
}
