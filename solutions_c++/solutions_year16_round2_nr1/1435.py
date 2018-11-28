#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

int main() {
	int T;
	cin >> T;
	vector<string> P = {
		"ZERO",
		"ONE",
		"TWO",
		"THREE",
		"FOUR",
		"FIVE",
		"SIX",
		"SEVEN",
		"EIGHT",
		"NINE"
	};
	vector<int> O = {0, 2, 6, 8, 7, 4, 5, 3, 9, 1};
	vector<char> C = {'Z', 'W', 'X', 'G', 'S', 'U', 'V', 'H', 'I', 'O'};
	for (int t = 1; t <= T; ++t) {
		string S;
		cin >> S;
		vector<int> N(9, 0);
		vector<int> A(26, 0);
		for (int i = 0; i < S.size(); ++i) {
			++A[S[i] - 'A'];
		}
		for (int i = 0; i < 10; ++i) {
			N[O[i]] = A[C[i] - 'A'];
			for (int j = 0; j < P[O[i]].size(); ++j) {
				A[P[O[i]][j] - 'A'] -= N[O[i]];
			}
		}
		// N[0] = A['Z' - 'A'];
		// N[2] = A['W' - 'A'];
		// N[6] = A['X' - 'A'];
		// N[8] = A['G' - 'A'];
		// N[7] = A['S' - 'A'];
		// N[4] = A['U' - 'A'];
		// N[5] = A['V' - 'A'];
		// N[3] = A['H' - 'A'];
		// N[9] = A['I' - 'A'];
		// N[1] = A['O' - 'A'];
		cout << "Case #" << t << ": ";
		for (int i = 0; i < 10; ++i) {
			//cout << N[i] << " ";
			while(N[i]--) {
				cout << i;
			}
		}
		cout << "\n";
	}
	return 0;
}
