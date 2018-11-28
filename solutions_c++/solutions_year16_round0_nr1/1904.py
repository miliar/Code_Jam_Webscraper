#include <iostream>

using namespace std;

int main() {

	int cases; cin >> cases >> ws;

	for (int c = 0; c < cases; c++) {
		long long N; cin >> N >> ws;
		cout << "Case #" << (c+1) << ": ";
		if (N == 0) {
			cout << "INSOMNIA\n";
			continue;
		}
		bool *digits = new bool[10];
		for (int i = 0; i < 10; i++) digits[i] = false;
		int count = 0;
		long long last;
		int mult = 0;
		bool success = false;
		while (count != 10) {
			mult++;
			long long Ncopy = N * mult;
			long long copy = Ncopy;
			last = Ncopy;
			while (copy > 0) {
				int digit = copy%10;
				copy /= 10;
				if (!digits[digit]) {
					count++;
					digits[digit] = true;
				}		
			}
			if (count >= 10) {
				success = true;
				break;
			}
			if (mult > 10000 || N < 0) break;
		}
		if (success) {
			cout << last << "\n";			
		}
		else {
			cout << "INSOMNIA\n";
		}

		delete digits;
	}

	return 0;
}
