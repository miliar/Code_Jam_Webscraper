#include <iostream>
#include <fstream>

using namespace std;

int solve(istream& in) {
	int s_max;
	int shyness[1001];

	in >> s_max; // s_max
	in.ignore(); // space

	for (int i = 0; i <= s_max; i++) {
		char temp;
		in >> temp;
		shyness[i] = temp - '0';
	}

	// for (int i = 0; i <= s_max; i++) {
	// 	cout << shyness[i] << " ";
	// }
	// cout << endl;

	int padding_counter = 0;
	int shyness_counter = 0;
	for (int i = 0; i <= s_max; i++) {
		if (shyness_counter < i) {
			padding_counter++;
			shyness_counter++;
		}
		shyness_counter += shyness[i];
	}

	return padding_counter;
}

int main() {

	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int T;

	fin >> T;

	for (int i = 1; i <= T; i++) {
		fout << "Case #" << i << ": " << solve(fin) << endl;
	}

	fin.close();
	fout.close();

	return 0;
}
