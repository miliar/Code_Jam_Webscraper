#include <fstream>
#include <string>

// Ominous Omino

int main() {

	std::ifstream file("input.in");
	std::ofstream out("output.txt");

	int t;
	file >> t;

	int count = 1;

	while (t-- > 0) {
		bool richard = false;
		int x, r, c;
		file >> x;
		file >> r;
		file >> c;
		int n = r * c;
		if (x < 7) {
			if (x > 1) {
				if (n % x != 0) {
					richard = true;
				} else if (r == 1 || c == 1) { // divisible
					if (x == 2) {
						if (n % x != 0) {
							richard = true;
						}
					} else {
						// x > 2
						richard = true;
					}
				} else if (x < n && x > n / 2) { // at least 2x2
					richard = true;
				} else if (r < x && c < x) { // less than or equal to half
					//can break with straight line
					richard = true;
				} else if (x % 2 == 0) {
					if (r < x/2 || c < x/2) {
						//can break with L
						richard = true;
					} else if (r == x/2 || c == x/2) {
						//can break with s
						richard = true;
					}
				} else if (r <= x/2 || c <= x/2){
					// can break with L
					richard = true;
				} else if ((r == 1+ x/2 || c == 1+x/2) && (r%2 == c%2) && (abs (r-c) <= 2)) {
					//can break with w
					richard = true;
				}
			}
		} else {
			richard = true;
		}
		out << "Case #" << count++ << ": " << (richard ? "RICHARD" : "GABRIEL") << std::endl;
	}

	return 0;
}