#include<stdlib.h>
#include<iostream>
#include<fstream>

using namespace std;

int main() {

	int T, N;

	ifstream input;
	input.open("A-large.in");

	ofstream output;
	output.open("output.txt");


	input >> T;

	for (int i = 1; i <= T; i++) {

		int count = 1, result = 0, fresult = 0;
		int nums[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
		bool all = false;

		input >> N;

		if (N == 0) {

			all = true;

		}

		while (all == false) {

			result = count * N;

			fresult = result;

			do {

				int digit = result % 10;

				for (int k = 0; k < 10; k++) {

					if (digit == k) {

						nums[k] = digit + 1;

					}

				}

			} while (result /= 10);

			int sum = 0;
			for (int k = 0; k < 10; k++) {

				sum += nums[k];

			}

			if (sum == 55) {

				all = true;

			}

			count++;

		}

		if (fresult == 0) {

			output << "Case #" << i << ": INSOMNIA" << endl;

		}
		else {

			output << "Case #" << i << ": " << fresult << endl;
		
		}

	}

	input.close();
	output.close();

	return 0;

}