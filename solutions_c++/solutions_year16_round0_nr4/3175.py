// D.cpp

#include <iostream>
using namespace std;

// for passing small-test

int main(int argc, char const *argv[]) {
	int T;
	cin >> T;

	for (int t = 0; t < T; ++t) {
		int K, C, S;
		cin >> K >> C >> S;

		cout << "Case #" << t+1 << ": ";
		for (int i = 0; i < K-1; ++i) {
			cout << i+1 << " ";
		}
		cout << K << endl;
	}

	return 0;
}