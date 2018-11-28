
#include <iostream>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		int s;
		char shy[2000];
		cin >> s >> shy;
		int f = 0;
		int stand = 0;
		int level = 0;
		while (level <= s) {
			if (f + stand < level) {
				f = level - stand;
			}
			stand += shy[level] - '0';
			level++;
		}
		cout << f << endl;
	}
	return 0;
}

