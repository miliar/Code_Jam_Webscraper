#include <iostream>
#include <vector>
#include <string>

using namespace std;

void entry() {
	string S;
	cin >> S;
	string r = "";
	for (int i = 0; i < S.size(); ++i) {
		if (S[i] + r < r + S[i]) {
			r = r + S[i];
		}
		else {
			r = S[i] + r;
		}
	}
	cout << r;
}

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		cout << "Case #" << (i + 1) << ": ";
		entry();
		cout << "\n";
	}
	return 0;
}
