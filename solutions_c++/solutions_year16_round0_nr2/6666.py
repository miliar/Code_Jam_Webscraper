#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string S;

void flipRange(int i) {
	for (int n = 0; n <= i / 2; ++n) {
		if (n != i - n) {
			swap(S[n], S[i - n]);
			S[n] = (S[n] == '-' ? '+' : '-');
			S[i - n] = (S[i - n] == '-' ? '+' : '-');
		} else {
			S[n] = (S[n] == '-' ? '+' : '-');
		}
	}
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cin >> S;
		int flips = 0;
		//cout << S << "\n";
		for (int i = S.size() - 1; i >= 0; --i) {
			if (S[i] == '-') {
				if (S[0] == '-') {
					flipRange(i);
					//cout << S << "\n";
					++flips;
				} else {
					int x = 0;
					while (x < i && S[x] == '+') {
						++x;
					}
					flipRange(x - 1);
					//cout << S << ")\n";
					flipRange(i);
					//cout << S << "\n";
					flips += 2;
				}
			}
		}
		cout << "Case #" << t << ": " << flips << "\n";
	}
	return 0;
}