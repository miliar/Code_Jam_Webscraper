#include <iostream>
#include <string>

using namespace std;

int getShortestPath(string s) {
	// count number of alternations, if last alternation is a + subtract 1
	int alternations = 1;
	for (unsigned i = 1; i < s.size(); ++i) {
		if (s[i] != s[i-1]) {
			++alternations;
		}
	}
	if (s[s.size()-1] == '+') {
		return alternations - 1;
	}
	return alternations;
}

int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		string s;
		cin >> s;
		getShortestPath(s);
		cout << "Case #" << i+1 << ": " << getShortestPath(s) << "\n";
	}
	return 0;
}