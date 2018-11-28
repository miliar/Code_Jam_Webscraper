#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ofstream myfile("example.txt");
	ifstream target("A-small-attempt0.in");
	int T;
	target >> T;
	cout << T << endl;
	for (int i = 0; i < T; i++) {
		int initial;
		target >> initial;
		if (initial == 0) {
			myfile << "Case #" << i + 1 << ": INSOMNIA" << endl;
			continue;
		}
		bool find = false;
		int num = 0;
		int time[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
		int result = initial;
		while (!find) {
			int n = result;
			find = true;
			do {
				int digit = n % 10;
				time[digit]++;
				n /= 10;
			} while (n > 0);
			for (int j = 0; j < 10; j++) {
				if (time[j] == 0) {
					find = false;
					break;
				}
			}
			result += initial;
		}
		myfile << "Case #" << i + 1 << ": " << result - initial << endl;
	}
	return 0;
}
