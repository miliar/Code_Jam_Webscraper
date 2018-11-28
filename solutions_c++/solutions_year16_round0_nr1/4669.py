#include <fstream>
#include <iostream>
#include <map>
#include <cmath>

using namespace std;

bool checkDigits(long long n, map<int, bool> &digits);

int main() {
	fstream fin, fout;
	fin.open("A_large.txt", ios::in | ios::out);
	fout.open("A_large_output.txt", ios::in | ios::out);

	int t;
	fin >> t;

	long long temp;
	bool foundAll;
	map<int, bool> digits;
	for (int i = 0; i < t; i++) {
		long n;	
		fin >> n;

		temp = n;
		foundAll = false;
		digits.clear();

		for (int m = 1; temp != 0 && !foundAll; ++m) {
			temp = n * m;
			foundAll = checkDigits(temp, digits);
		}
 
		if (temp == 0) {
			fout << "Case #" << (i+1) << ": INSOMNIA" << endl;
		} else {
			fout << "Case #" << (i+1) << ": " << temp << endl;
		}
	}

	fin.close();
	fout.close();

	return 0;
}

bool checkDigits(long long n, map<int, bool> &digits) {
	while (n != 0) {
		int units = n % 10;
		digits[units] = true;

		if (digits.size() == 10) {
			return true;
		}

		n /= 10;
	}

	return false;
}
