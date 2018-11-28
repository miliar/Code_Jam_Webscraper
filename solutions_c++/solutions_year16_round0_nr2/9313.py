#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>


using namespace std;

void testcases() {
	string s; cin >> s;
	int flips = 0;

	for (size_t i = 0; i < s.length()-1; ++i)
		if (s.at(i) != s.at(i+1))
			flips++;
	if (s.at(s.length()-1) == '-')
		flips++;

	cout << flips << endl;
	
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
