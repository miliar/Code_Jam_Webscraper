#include <iostream>
#include <sstream>
#include <cstdio>

int main(int argc, char **argv) {

	unsigned T;
	std::cin >> T;

	std::ostringstream oss;
	for (unsigned i=2; i<11; ++i) {
		oss << ' ' << (i+1);
	}
	std::string divisors(oss.str());

	for (unsigned i=0; i<T; ++i) {
		printf("Case #%d:",i+1);
		unsigned K, C, S;
		std::cin >> K;
		std::cin >> C;
		std::cin >> S;
		unsigned toClean = K;
		if (K>1 && C>1) {
			--toClean;
		}
		if (S < toClean) {
			printf(" IMPOSSIBLE\n");
			continue;
		}
		for (unsigned j=0;j<toClean;++j) {
			if (toClean == K) {
				printf(" %u",j+1);
			} else {
				printf(" %u",j+2);
			}
		}
		printf("\n");//
	}

	return 0;
}

