#include <iostream>
#include <fstream>
#include "BigInteger.cpp"

int main() {
	int T;
	BigInt a, b, sqrt_a, sqrt_b, i, i_sqr;
	std::ifstream fin;
	std::ofstream fout;
	fin.open("C-small-attempt0.in");
	fout.open("output.txt");
	fin >> T;
	for (int test_case = 0; test_case < T; test_case++) {
		fin >> a >> b;
		sqrt_a = sqrt(a);
		if (sqrt_a * sqrt_a < a) {
			sqrt_a = sqrt_a + 1;
		}
		sqrt_b = sqrt(b);
		int counter = 0;
		for (i = sqrt_a, i_sqr = sqrt_a * sqrt_a; i < sqrt_b + 1; i_sqr = i_sqr + 2 * i + 1, i = i + 1) {
			if (i.isPalindrome() && i_sqr.isPalindrome()) {
				counter++;
			} else {
			}
		}
		fout << "Case #"<< test_case + 1 << ": " << counter << std::endl;
	}
	return 0;
}