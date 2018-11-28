#include <iostream>
#include <cmath>

int main(int argc, char* argv[]) {
	unsigned int T, result;
	unsigned long long r, t, val;

	std::cin >> T;

	for(unsigned int i = 0; i < T; i++) {
		std::cin >> r >> t;
		result = 0;
		for(;;) {
			val = (r+1)*(r+1)-r*r;
			if( val > t ) break;
			t -= val; r += 2; result++;
		}
		std::cout << "Case #" << (i+1) << ": " << result << std::endl;
	}

	return 0;
}