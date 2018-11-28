#include <iostream>
using namespace std;

int main(void) {
	int T, K, C, S;

	cin >> T;
	for (int testCase = 1; testCase <= T; testCase++) {
		cin >> K >> C >> S;
		cout << "Case #" << testCase << ":";
		for (int i = 1; i <= S; i++) {
			cout << " " << i;
		}
		cout << endl;
	}
}