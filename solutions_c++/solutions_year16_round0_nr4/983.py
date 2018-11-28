#include <algorithm>
#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	int tests;
	cin >> tests;
	for(int test = 1; test <= tests; ++test) {
		int length, complexity, limit;
		cin >> length >> complexity >> limit;
		cout << "Case #" << test << ':';
		if(complexity * limit < length) {
			cout << " IMPOSSIBLE\n";
			continue;
		}
		int i = 0;
		while(i < length) {
			long long result = 0;
			for(int j = 0; j < complexity; ++j) {
				result = result * length + min(i++, length - 1);
			}
			cout << ' ' << result + 1;
		}
		cout << '\n';
	}
	return 0;
}
