#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>


using namespace std;

void testcases() {
	int N; cin >> N;
	if (N == 0) {
		cout << "INSOMNIA" << endl;
		return;
	}

	vector<int>	digits(10,0);
	int counter = 0;
	int number = 0;

	while (counter < 10) {
		number += N;
		stringstream ss; ss << number;
		string s = ss.str();
		// check digits for new appearance
		for (size_t i = 0; i < s.length(); ++i) {
			stringstream sk; sk << s.at(i);
			int k; sk >> k;
			if (digits[k] == 0) {
				counter++;
				digits[k]++;
			}
		}
	}

	cout << number << endl;
	
}

int main() {
	ios_base::sync_with_stdio(false);
	int T; cin >> T;
	for (int i = 1; i <= T; ++i) {
		cout << "Case #" << i << ": ";
		testcases();
	}

	return EXIT_SUCCESS;
}
