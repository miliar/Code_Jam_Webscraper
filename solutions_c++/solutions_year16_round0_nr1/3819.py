#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main() {
	fstream fin;
	fin.open("input.txt");
	int cases = 0;
	fin >> cases;
	for (int rnd = 0; rnd < cases; ++rnd) {
		// Do each case here
		std::vector<bool> nums(10, false);
		long num_seen = 0;
		long val;
		fin >> val;
		long update = 1;
		long its = 1;
		// cout << "*****************\n";
		while (true) {
			update = val * its;
			its++;
			long num = update;
			// cout << "Num is " << num << endl;
			while (num) {
				long ones = num %10;
				num /= 10;
				if (!nums[ones]) {
					// cout << "Found " << ones << endl;
					nums[ones] = true;
					num_seen++;
				}
			}
			if (num_seen == 10) {
				break;
			}
			if (its == 20000) {
				break;
			}
		}
		if (num_seen == 10) {
			cout << "Case #" << rnd+1 << ": " << update << endl;
		} else {
			cout << "Case #" << rnd+1 << ": " << "INSOMNIA" << endl;
		}
		// Output case info
	}
	fin.close();
	return 0;
}