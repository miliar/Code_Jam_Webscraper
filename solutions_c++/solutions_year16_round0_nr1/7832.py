#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

bool check(bool* arr) {

	for (int i = 0; i < 10; i++)
		if (!arr[i]) return false;

	return true;
}

long solve(int n) {

	bool* arr = new bool[10];

	for (int i = 0; i < 10; i++)
		arr[i] = false;

	int iter = 0;
	while (!check(arr)) {
		long temp = n * iter;
		while (temp > 0) {
			arr[temp % 10] = true;
			temp /= 10;
		}
		iter++;
	}
	iter--;

	return n * iter;
}

int main() {

	int t, n;
	fstream infile;
	infile.open("A-large.in", ios_base::in | ios_base::app);
		
	infile >> t;

	fstream outfile;
	outfile.open("out.out", ios_base::out | ios_base::app);

	for (int i = 1; i <= t; i++) {
		infile >> n;

		if (n == 0) {
			outfile << "Case #" << i << ": INSOMNIA" << endl;
			continue;
		}

		outfile << "Case #" << i << ": " << solve(n) << endl;
	}

	return 0;
}