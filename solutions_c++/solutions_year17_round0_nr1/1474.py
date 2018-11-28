#include <iostream>
#include <string>
using namespace std;

int process(string& S, int K) {
	int SLen = S.length(), count = 0;
	for (int i = 0, limit = SLen - K; i <= limit; ++i) {
		if (S[i] == '-') {
			++count;
			S[i] = '+';
			for (int j = i + 1, limitj = i + K; j < limitj; ++j) {
				if (S[j] == '+') S[j] = '-';
				else S[j] = '+';
			}
		}
	}
	for (int i = SLen - K + 1; i < SLen; ++i) {
		if (S[i] == '-') return -1;
	}
	return count;
}

int main () { // first try ok small test
	//data
	int T, K;
	string S;
	
	//input
	cin >> T;

	for (int i = 0; i < T; ++i) {
		// input
		cin >> S >> K;

		//process		
		int min = process(S, K);

		//output
		cout << "Case #" << (i + 1) << ": ";
		if (min < 0) cout << "IMPOSSIBLE";
		else cout << min;
		if (i + 1 < T) cout << endl;
	}

	return 0;
}