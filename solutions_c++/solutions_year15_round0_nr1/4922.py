#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;

int main() {
	ifstream test_file ("A-large.in", ios::in);
	ofstream output;
	output.open("A-large.out");
	int t;
	int s_max, friends;
	test_file >> t;
	char c;
	int *shyness;
	for (int testNum = 0; testNum < t; testNum++) {
		friends = 0;
		test_file >> s_max;
		shyness = new int[s_max];
		int standing = 0;
		for (int k = 0; k <= s_max; k++) {
			test_file >> c;
			int k_num = c - '0';
			shyness[k] = k_num;
			if (standing < k && k_num > 0) {
				friends += (k - standing);
				standing += (k - standing);
			}
			standing += k_num;
		}
		output << "Case #" << (testNum + 1) << ": " << friends << endl;
	}

	return 0;
}