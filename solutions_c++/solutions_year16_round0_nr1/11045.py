#include <iostream>
#include <fstream> 

using namespace std;

int main() {
	ofstream fout("A-small.out");
	ifstream fin("A-large.in");
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		// cout << t << endl;
		int N;
		fin >> N;
		fout << "Case #" << t << ": ";
		if (N == 0) {
			fout << "INSOMNIA" << endl;
		}
		else {
			bool digits[10];
			for (int d = 0; d < sizeof(digits); d++) {
				digits[d] = false;
			}
			int count = 0;
			int multiple;
			for (int i = 1; count < 10; i++) {
				// cout << i << endl;
				multiple = i*N;
				// cout << "multiple: " << multiple << endl;
				int num = multiple;
				do {
					int rem = num%10;
					// cout << "rem:" << rem << endl;
					if (!digits[rem]) {
						digits[rem] = true;
						count++;
					}
					num /= 10;
				} while (num > 0);
			}
			fout << multiple << endl;
		}
	}
}