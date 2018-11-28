#include <iostream>
#include <string>

using namespace std;

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; ++t) {
		int S;
		string aud;
		int claps = 0;
		int adds = 0;

		cin >> S >> aud;

		for (int s = 0; s <= S; ++s) {
			int ppl = aud[s] - '0';

			if (ppl > 0 && claps < s) {
				adds += s - claps;
				claps = s;
			}

			claps += ppl;
		}

		cout << "Case #" << t << ": " << adds << endl;
	}
}
