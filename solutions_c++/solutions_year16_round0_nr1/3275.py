#include <iostream>
#include <fstream>

int main() {
	std::ifstream fin;
	fin.open("input.txt");
	int T;
	fin >> T;
	int N;
	//std::cout << T << std::endl;

	std::ofstream fout;
	fout.open("output.txt");

	for (int i = 1; i <= T; ++i) {
		std::cout << i << "/" << T << std::endl;
		fin >> N;
		bool done = false;
		uint64_t sum = N;
		uint16_t digits = 0;
		while (!done) {
			uint64_t sum_tmp = sum;
			while (sum_tmp > 0) {
				int8_t digit = sum_tmp % 10;
				digits = digits | (1 << digit);
				sum_tmp /= 10;
			}
			//std::cout << "\t" << std::hex << digits << std::dec << std::endl;
			if (digits == 0x3FF) {
				//std::cout << sum << std::endl;
				fout << "Case #" << i << ": " << sum << std::endl;
				done = true;
			}
			sum += N;
			if (sum == N) {
				//std::cout << "INSOMNIA" << std::endl;
				fout << "Case #" << i << ": INSOMNIA" << std::endl;
				done = true;
			}
		}
	}

	fin.close();
	fout.close();
	return 0;
}