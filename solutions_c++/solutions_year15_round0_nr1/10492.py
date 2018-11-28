#include <iostream>
using namespace std;

int main() {
	
	int tc;
	cin >> tc;

	int ct = 0;

	while (ct < tc) {

		int max;
		cin >> max;

		string s;
		cin >> s;

		int appl = 0;
		int friends = 0;
		for (int i = 0; i <= max; i++) {
			if (appl+friends < i) {
				friends += i - (appl+friends);
			}
			appl += s[i] - '0';
		}

		cout << "Case #" << (++ct) << ": " << friends << endl;
	}



}