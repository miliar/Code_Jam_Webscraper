#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int main() {
//	srand(time(NULL));
	ifstream input;
	input.open("in.txt", ios::in);

	int testCases = 0;
	input >> testCases;
//	cout << "Test Cases : " << testCases << endl;

	for (int i = 0; i < testCases; i++) {
		int n;
		input >> n;
//		cout << n;
		int digits[10] = { 0 };
		int found = 0;
		if (n == 0) {
			cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
			continue;
		}
		int bo;
		int digit;
		int tn;
		for (int iteration = 1;; iteration++) {
			bo = 0;
			tn = n * iteration;
			while (tn) {
				digit = tn % 10;
				tn = tn / 10;
				if (digits[digit] == 0) {
					digits[digit] = 1;
					found++;
					if (found == 10) {
						cout << "Case #" << i + 1 << ": " << n * iteration
								<< endl;
						bo = 1;
						break;
					}
				}
			}
			if (bo)
				break;
		}
	}
}
