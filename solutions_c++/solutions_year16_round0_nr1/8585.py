#include <iostream>
#include <fstream>
using namespace std;

int main(void) {
	ifstream fin("input_b.txt");
	ofstream fout("output_b.txt");

	int test_case;
	fin >> test_case;
	for (int test_idx = 1; test_idx <= test_case; test_idx++) {
		int n;
		fin >> n;
		cout << n;
		
		if (n == 0) {
			fout << "Case #" << test_idx << ": " << "INSOMNIA" << endl;
			continue;
		}

		bool digit[10] = { 0 };
		int nn = 0;
		while (true) {
			nn += n;
			int temp = nn;
			while (temp) {
				digit[temp % 10] |= 1;
				temp /= 10;
			}

			bool all_used = true;
			for (int i = 0; i <= 9; i++) {
				if (!digit[i]) {
					all_used = false;
					break;
				}
			}

			if (all_used) {
				cout << "Case #" << test_idx << ": " << nn << endl;
				fout << "Case #" << test_idx << ": " << nn << endl;
				break;
			}
		}
	}
	return 0;
}