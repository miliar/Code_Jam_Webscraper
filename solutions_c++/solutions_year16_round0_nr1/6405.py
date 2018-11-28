#include <iostream>

using namespace std;

int main() {
	int numTestCases = 0;
	cin >> numTestCases;
	for (int i = 0; i < numTestCases; i++) {
		long long int start = 0;
		cin >> start;
		if (start == 0) {
			cout << "Case #" << i+1 << ": INSOMNIA" << endl;
		} else {
			bool arr[10] = {false};
			int sum = 0;
			int loops = 0;
			while (sum < 10) {
				loops++;
				long long int N = start * loops;
				do {
					int digit = N % 10;
					arr[digit] = true;
					N /= 10;
				} while (N > 0);
				sum = 0;
				for (int i = 0; i < 10; i++) {
					sum +=arr[i];
				}
			};
			cout << "Case #" << i+1 << ": " << loops * start << endl;
		}
	}
	return 0;
}