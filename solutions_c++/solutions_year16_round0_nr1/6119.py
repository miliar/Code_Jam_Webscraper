#include <math.h>
#include <iostream>
#include <string>

using namespace std;

int main() {
	int numberOfCases, i = 0;
	int N;
	int resp = 0;

	cin >> numberOfCases;
	while (cin >> N) {
		if (N == 0) {
			cout << "Case #" << ++i << ": INSOMNIA" << endl;
			continue;
		}
		int counter = 1;
		bool seen[10] = {0};
		while (true) {
			bool cont = false;
			for (int i = 0; i < 10; i++) {
				if (!seen[i]) {
					cont = true;
					break;
				}
			}
			if (!cont) {
				break;
			}

			resp = counter * N;
			// cerr << "\t NUMBER = " << resp << endl;
			string n_s = to_string(resp);

			for (int i = 0; i < n_s.length(); i++) {
				// cout << "\t testing " << (n_s[i] - '0') << endl;
				seen[n_s[i] - '0'] = true;
			}
			// cerr << "TESTE" << endl;
			counter++;
		}

		cout << "Case #" << ++i << ": " << resp << endl;
	}
}
