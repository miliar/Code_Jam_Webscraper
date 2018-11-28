#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

int main() {
	string token;

	cin >> token;
	int T = atoi(token.c_str());

	for (int t = 1; t <= T; t++) {
		cin >> token;
		int S = atoi(token.c_str());

		cin >> token;
		int total = 0;
		int needed = 0;
		for (int s = 0; s <= S; s++) {
			int missing = max(0, s - total);
			needed += missing;
			total += missing + token[s] - '0';
		}
		printf("Case #%d: %d\n", t, needed);
	}
}

