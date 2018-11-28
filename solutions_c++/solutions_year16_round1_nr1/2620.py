#include <iostream>
#include <string>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		string S;
		cin >> S;
		string O = "";
		O += S[0];
		for (int i = 1; i < S.size(); ++i) {
			if (S[i] >= O[0]) {
				O = S[i] + O;
			} else {
				O += S[i];
			}
		}
		cout << "Case #" << t <<": " << O << "\n";
	}
	return 0;
}