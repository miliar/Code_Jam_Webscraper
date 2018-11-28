#include <iostream>
#include <string>

using namespace std;

int main() {
	int n;
	cin >> n;

	string input;
	getline(cin, input);

	for (int i = 1; i <= n; i++) {
		getline(cin, input);

		string res = "";
		string::iterator it = input.begin();
		res = res + *it;
		it++;

		while (it != input.end()) {
			if (*it < res[0]) res = res + *it;
			else res = *it + res;
			it++;
		}

		cout << "Case #" << i << ": ";
		cout << res << endl;
	}

	return 0;
}