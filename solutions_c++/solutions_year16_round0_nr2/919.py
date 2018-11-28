#include <iostream>
#include <string>
using namespace std;

int main() {
	int cases;
	cin >> cases;
	for (int caseCounter = 1; caseCounter <= cases; caseCounter++) {
		string s;
		cin >> s;
		int changes = 0;
		if (s.length() > 1) {
			for (int i = 0; i <= s.length() - 2; i++) {
				if (s[i] != s[i + 1])
					changes++;
			}
		}
		if (s[s.length() - 1] == '-')
			changes++;
		cout << "Case #" << caseCounter << ": " << changes << endl;
	}
	return 0;
}
