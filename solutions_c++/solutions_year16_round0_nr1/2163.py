#include <iostream>
#include <set>

using namespace std;

int main() {
	int numCases;
	cin >> numCases;
	for (int caseNum = 1; caseNum <= numCases; ++caseNum) {
		long long n, original_n;
		int numIters = 1;
		set<int> digits;
		cin >> n;
		original_n = n;

		if (n == 0) {
			cout << "Case #" << caseNum << ": INSOMNIA" << endl;
			continue;
		}

		while (digits.size() < 10) {
			numIters++;
			long long n_digits = n;
			while (n_digits > 0) {
				digits.insert(n_digits % 10);
				n_digits /= 10;
			}
			n = numIters * original_n;
		}

		cout << "Case #" << caseNum << ": " << (numIters - 1) * original_n << endl;
		
	}	
	
	return 0;
}
