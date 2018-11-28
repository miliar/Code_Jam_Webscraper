#include <iostream>
#include <vector>
#include <string>
#include <algorithm>


using namespace std;

int main() {
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		int mx = 0;  string S; cin >> mx >> S;
		int curNum = 0;
		int need = 0;
		for (int i = 0; i < S.size(); i++) {
			if (S[i] > '0') {
				need += (max(0, i - curNum));
				curNum = curNum + need + (S[i] - '0');
			}
		}
		cout << "Case #" << (t) << ": " << need << endl;
	}

	return 0;
}