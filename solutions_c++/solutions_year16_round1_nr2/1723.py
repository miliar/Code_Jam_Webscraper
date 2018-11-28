#include <iostream>
#include <cstdio>
#include <vector>


int main(int argc, char **argv) {

	unsigned T;
	std::cin >> T;

	for (unsigned i=0; i<T; ++i) {

		unsigned N;
		std::cin >> N;

		int heights[2501];
		for (unsigned j=1; j<=2500; ++j) {
			heights[j] = 0;
		}

		for (unsigned j=0; j<N*(2*N-1); ++j) {
			unsigned h;
			std::cin >> h;
			++heights[h];
		}

		unsigned check = 0;
		printf("Case #%d:",i+1);
		for (unsigned j=1; j<=2500; ++j) {
			if (heights[j]%2) {
				printf(" %u",j);
				++check;
			}
		}
		printf("\n");
		if (check != N) {
			printf("ERROR\n");
		}
	}

	return 0;
}
