#include <iostream>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int l0 = 0; l0 < t; l0++) {
		int smax;
		string shy;
		cin >> smax >> shy;

		int add = 0, cur = 0;
		for (int l1 = 0; l1 < (int)shy.length(); l1++) {
			if (cur < 0) {
				add++;
				cur++;
			}
			cur += int(shy[l1] - '0');
			cur--;
		}
		cout << "Case #" << l0 + 1 << ": " << add << endl;
	}
	return 0;
}