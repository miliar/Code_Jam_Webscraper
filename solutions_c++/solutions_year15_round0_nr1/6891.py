#include <iostream>
#include <fstream>

int solve(int n, std::string weights);

int main()
{
	std::ifstream in;
	in.open("A-large.in");
	if (in.fail()) {
		std::cerr << "Error while opening the input file\n";
		return 1;
	}

	int cases;
	in >> cases;

	for (int i = 0; i < cases; i++) {
		int n;
		std::string weights;
		in >> n >> weights;
		std::cout << "Case #" << i + 1 << ": " << solve(n, weights) << "\n";
	}

	return 0;
}

int solve(int n, std::string weights)
{
	int guests = 0;
	for (int i = n; i >= 0; i--) {
		// Sum of all the weights on the left of the current number
		int sum = guests;
		for (int j = i - 1; j >= 0; j--) {
			sum += weights[j] - '0';
		}
		// Needed new guests
		if (sum < i) {
			guests += i - sum;
		}
	}
	return guests;
}