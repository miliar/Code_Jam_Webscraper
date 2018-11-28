#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <sstream>
#include <string>

using namespace std;

int min_happy(const string& s) {
	int res = 0;
	int i = 0;
	
	while (i < s.size()) {
		if (i < s.size() - 1 && s[i] != s[i+1]) {
			res += 1;
		}
		else if (i == s.size() - 1) {
			res += ((s[i] == '-') ? (1) : (0));
		}
		i++;
	}

	return res;
}

int main() {
	int n_tests;

	cin >> n_tests;
	cin.ignore();

	for (int test = 0; test < n_tests; test++) {
		// input
		string s;
		cin >> s;
		cin.ignore();


		cout << "Case #" << test+1 << ": "; 

		// output
		cout << min_happy(s);

		cout << endl;
	}

	return 0;
}