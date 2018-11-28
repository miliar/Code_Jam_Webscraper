#include <bits/stdc++.h>

using namespace std;

int main() {
	int nCase;
	cin >> nCase;

	for (int i = 1; i <= nCase; ++i) {
		cout << "Case #" << i << ": ";
		string a;
		cin >> a;

		bool inMinus = (a[0] == '-');
		bool firstMinus = inMinus;
		int count = 0;
		for (int j = 0; j < a.length(); ++j) {
			if (a[j] == '-') {
				if (!inMinus) {
					count += 2;
					inMinus = true;
				}
			} else {
				inMinus = false;
			}
		}

		if (firstMinus) ++count;
		cout << count << endl;
	}

	return 0;
}
