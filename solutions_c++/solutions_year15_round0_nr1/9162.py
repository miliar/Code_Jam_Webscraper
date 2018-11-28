#include <bits/stdc++.h>
using namespace std;

int main() {
	int test;
	int Smax;
	string S;
	cin >> test;

	int kase = 1;

	while (test--) {

		cin >> Smax >> S;

		int current = 0;
		int added = 0;

		for (int i = 0 ; i<S.length() ; i++) {
			if (i > current) {
				added += (i-current);
				current += (i-current);
			}
			current += (S[i]-'0');
		}

		cout << "Case #" << kase++ << ": " << added << endl;
	}

	return 0;
}