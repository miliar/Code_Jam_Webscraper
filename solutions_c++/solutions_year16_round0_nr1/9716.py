#include <iostream>
#include <algorithm>
#include <string>
#include <numeric>
#include <sstream>

using namespace std;

int main() {
	int t, n;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> n;
		string str = to_string(n);
		bool num[10] = {false};
		int count = 0;
		bool ins = false;
		int idx, a = n;
		while (true) {
			count += 1;
			for (int j = 0; j < str.length(); j++) {
				idx = str[j] - '0';
				if (num[idx] == false) {
					num[idx] = true;
				}
			}
			if (accumulate(num, num + 10, 0) == 10) {
				break;
			}
			if (count > 1000) {
				ins = true;
				break;
			}
			n += a;
			str = to_string(n);
		}
		if (ins) {
			cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
		}
		else {
			cout << "Case #" << i + 1 << ": " << str << endl;
		}
	}
	return 0;
}