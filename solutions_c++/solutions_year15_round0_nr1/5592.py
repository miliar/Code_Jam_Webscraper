#include <iostream>
#include <string>
using namespace std;

int main() {
	int ncases;
	cin >> ncases;

	for (int c = 1; c <= ncases; c++) {
		int n;
		cin >> n;

		string s;
		cin >> s;
		int ppl = 0;

		int sum = 0;

		for (int i = 0; i <= n; i++) {
			int q = s[i] - '0';

			if (q > 0) {
				if (sum + ppl < i) {
					ppl += (i - (sum + ppl));
				}
				sum += q;
			}
		}
		
		cout << "Case #" << c << ": " << ppl << endl;
	}

	return 0;
}