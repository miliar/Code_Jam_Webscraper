#include <iostream>
using namespace std;

int main(int argc, char ** argv) {
	int TestCases;
	
	cin >> TestCases;

	for (int tcase = 1; tcase <= TestCases; tcase++) {
		int Smax;
		char buffer[2048];

		cin >> Smax >> buffer;
		int friends_needed = 0;
		int curr_count = buffer[0] - '0';
		for (int i = 1; i <= Smax; i++) {
			if (curr_count < i) {
				friends_needed += (i - curr_count);
				curr_count = i;
			}
			curr_count += buffer[i] - '0';
		}
		cout << "Case #" << tcase << ": " << friends_needed << endl;
	}

	return 0;
}