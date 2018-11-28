#include <iostream>
#include <iomanip>

int main(int argc, char* argv[]) {
	unsigned int T;
	double C, F, X;
	double acc, mn, v;

	std::cin >> T;

	for( unsigned int t = 1; t <= T; t++ ) {
		std::cin >> C >> F >> X;
		acc = 0; mn = 0;

		mn = X / 2;
		for( unsigned int i = 0; i <= X/C; i++ ) {
			acc += C / ((i*F) + 2);
			v = acc + (X / (((i+1)*F) + 2));
			if ( v < mn ) { mn = v; }
		}

		std::cout << "Case #" << t << ": " << std::fixed << std::setprecision(7) << mn << std::endl;
	}

	return 0;
}