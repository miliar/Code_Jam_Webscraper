#include <vector>
#include <iostream>
#include <fstream>
#include <cmath>

long long int reverse(long long int x) {
	long long int y = 0;

	while (x > 0) {
		y *= 10;
		y += x % 10;
		x /= 10;
	}

	return y;
}

int main(void) {
	int cases = 0;
	std::fstream inFile;
	long long int a, b, c, x, y;
	int cnt;

	inFile.open("fs.txt");

	inFile >> cases;

	for (int i = 0; i < cases; ++i) {
		inFile >> a >> b;
		c = (long long int)floor(sqrt(a));
		x = c * c;
		cnt = 0;

		while (x <= b) {
			if (c == reverse(c)) {
				y = reverse(x);

				if (x == y && x >= a) {
					cnt++;
				}
			}

			c++;
			x = c * c;
		}

		std::cout << "Case #" << (i + 1) << ": " << cnt << std::endl;
	}

	return 0;
}
