#include <iostream>

using namespace std;

int main(int argc, char const *argv[]) {
	
	int nTestCases;
	cin >> nTestCases;

	for (int i = 0; i < nTestCases; ++i) {
		int K, C, S;
		cin >> K >> C >> S;

		cout << "Case #" << i+1 << ": ";
		for (int j = 0; j < K; ++j) {
			cout << j+1 << " ";
		}
		cout << endl;
	}

	return 0;
}