#include <iostream>
#include <string>

using namespace std;

long long solve(string name, int n) {
	int len = name.length();
	int *list = new int[len];

	for (int i = 0; i < len; i++) {
		char c = name[i];

		if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
			list[i] = 0;
		} else {
			list[i] = 1;
		}
	}

	long long value = 0;

	for (int i = 0; i <= len - n; i++) {
		int chain_len = 0;

		for (int j = i; j < len; j++) {
			if (list[j]) {
				if (++chain_len == n) {
					value += len - j;
					break;
				}
			} else {
				chain_len = 0;
			}
		}
	}

	delete [] list;
	return value;
}

int main() {
	int case_cnt;

	cin >> case_cnt;

	for (int i = 1; i <= case_cnt; i++) {
		string name;
		int n;

		cin >> name >> n;
		cout << "Case #" << i << ": " << solve(name, n) << endl;
	}

	return 0;
}
