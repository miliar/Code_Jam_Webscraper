#include <iostream>

int main() {

	unsigned lawnCount;
	std::cin >> lawnCount;

	for (int i = 1; i <= lawnCount; ++i) {

		unsigned lines, cols;
		std::cin >> lines >> cols;

		uint8_t* lawn = new uint8_t[lines * cols];

		for (unsigned j = 0; j < lines * cols; ++j) {
			unsigned h;
			std::cin >> h;
			lawn[j] = h;
		}

		uint8_t* linemax = new uint8_t[lines];
		uint8_t* colmax = new uint8_t[cols];

		for (unsigned j = 0; j < lines; ++j) {
			linemax[j] = 0;
		}

		for (unsigned k = 0; k < cols; ++k) {
			colmax[k] = 0;
		}

		for (unsigned j = 0; j < lines; ++j) {
			for (unsigned k = 0; k < cols; ++k) {
				uint8_t& h(lawn[j * cols + k]);
				if (h > linemax[j]) {
					linemax[j] = h;
				}
				if (h > colmax[k]) {
					colmax[k] = h;
				}
			}
		}

		bool valid = true;

		for (unsigned j = 0; valid and j < lines; ++j) {
			for (unsigned k = 0; valid and k < cols; ++k) {
				uint8_t& h(lawn[j * cols + k]);
				if (h < linemax[j] and h < colmax[k]) {
					valid = false;
				}
			}
		}

		delete[] linemax;
		delete[] colmax;
		delete[] lawn;

		std::cout << "Case #" << i << ": " << (valid ? "YES" : "NO" ) << std::endl;

	}

}
