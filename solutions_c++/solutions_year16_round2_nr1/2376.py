#include <iostream>
#include <string>
using namespace std;

string seq[10] = {"ZERO", "TWO", "SIX", "FOUR", "EIGHT", 
				"THREE", "SEVEN", "FIVE", "ONE", "NINE"};
int k_v[10] = {0, 2, 6, 4, 8, 3, 7, 5, 1, 9};
char k_w[10] = {'Z', 'W', 'X', 'U', 'G',
				'T', 'S', 'V', 'O', 'I'};

int main() {
	int T;
	int t;
	int key;
	string S;
	int input[256];
	int ans[10];

	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	cin >> T;
	for (t = 1; t <= T; ++t) {
		cin >> S;
		memset(input, 0, sizeof(input));
		memset(ans, 0, sizeof(ans));

		for (int i = 0; i < S.size(); ++i) {
			input[S[i] - 'A']++;
		}

		cout << "Case #" << t << ": ";
		for (key = 0; key < 10; ++key) {
			while(input[k_w[key] - 'A'] > 0) {
				ans[k_v[key]]++;
				for (int i = 0; i < seq[key].size(); ++i) {
					input[seq[key][i] - 'A']--;
				}
			}
		}
		for (int i = 0; i < 10; ++i) {
			while(ans[i]) {
				ans[i]--;
				cout << i;
			}
		}
		cout << endl;
	}
	return 0;
}