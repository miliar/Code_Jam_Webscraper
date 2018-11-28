#include <fstream>

using namespace std;

unsigned long long solve(unsigned int N) {
	if (N == 0)
		return -1;
	int mask = 0;
	unsigned int i = 1;
	unsigned long long spoken = N;
	do {
		unsigned int temp_i = i;
		unsigned int shift_size = 0;
		while (temp_i % 2 == 0) {
			shift_size++;
			temp_i = temp_i/2;
		} 
		spoken = (N  << shift_size) * temp_i;
		unsigned long long temp = spoken;
		while (temp != 0) {
			mask |= 1 << temp % 10;
			temp /= 10;
		}
		i++;
	} while (mask != 1023);

	return spoken;
}

int main(int argc, char *argv[]) {
	// read file
	std::ifstream infile(argv[1]);
	std::ofstream outfile("output.txt");
	unsigned int no_tests;
	unsigned int N;
	infile >> no_tests;
	for (int i = 0; i < no_tests; i++) {
		infile >> N;
		if (N == 0) {
			outfile << "Case #" << i + 1 << ": INSOMNIA\n";
		}
		else {
			int result = solve(N);
			outfile << "Case #" << i+1 << ": " << result << "\n";
		}
	}
	infile.close();
	outfile.close();
	return 0;
}