#include <iostream>
#include <fstream>
#include <stdio.h>

using std::cout; using std::endl;
int main() {
	std::ifstream input;
	input.open("./data/B-small-attempt0.in");
	std::ofstream out;
	out.open("./data/B-small-attempt0.out");
	long cases;
	input >> cases;

	std::cout << cases << std::endl;
	for (long c = 0; c < cases; ++c) {
		long a, b, k;
		input >> a;
		input >> b;
		input >> k;
		long n_won = 0;
		for (long a_it = 0; a_it < a; ++a_it) {
			for (long b_it = 0; b_it < b; ++b_it) {
				long c = a_it & b_it;
				if (c < k) n_won ++; 
			}
		}
		cout << "Case #" << c+1 << ": " << n_won << endl;
		out <<  "Case #" << c+1 << ": " << n_won << endl;
	}
}