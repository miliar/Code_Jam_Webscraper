#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>

using namespace std;

int main() {
	int T;
	cin >> T;
	string line;
	getline(cin, line);
	for (int t = 1; t <= T; t++) {
		getline(cin, line);
		int groups = 1;
		char lastChar = line[0];
		for (int i = 1; i < line.size(); i++) {
			if (lastChar != line[i]) {
				lastChar = line[i];
				groups++;
			}
		}
		if (lastChar == '+') {
			groups--;
		}
		printf("Case #%d: %d\n", t, groups);
	}
}