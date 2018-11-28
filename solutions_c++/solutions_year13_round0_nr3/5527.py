#include<iostream>
#include<fstream>
#include<cstdio>
#include<cmath>

using namespace std;

bool isPalindrome(int x) {
	char buffer[101];
	int n = sprintf(buffer, "%d", x);

	for (int i = 0; i < n/2; ++i)
		if (buffer[i] != buffer[n - 1 - i])
			return false;

	return true;
}

int main() {
	ifstream input_file;
	ofstream output_file;

	int cases = 0, fair_square = 0;

	input_file.open("D:\\Lysander\\input.txt");
	output_file.open("out.txt");

	if (input_file.is_open()) {
		input_file >> cases;
		for (int i = 1; i <= cases; ++i) {
			fair_square = 0;
			int a, b;
			input_file >> a >> b;
			
			for (int j = a; j <= b; ++j) {
				int sqrt_j = (int)sqrt((double)j);
				if (isPalindrome(j) && isPalindrome(sqrt_j) && (sqrt_j * sqrt_j) == j) {
					fair_square++;
					cout << j << " " << (int)sqrt((double)j) << endl;
				}
			}

			output_file << "Case #" << i << ": " << fair_square << endl;
		}
	}

	input_file.close();
	output_file.close();
	return 0;
}