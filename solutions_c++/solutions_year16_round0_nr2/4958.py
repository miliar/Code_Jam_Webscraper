#include <iostream>
#include <string>

using namespace std;

int getReverseTime(const string &str) {
	int ret = 0;
	for (int i = 1; i < str.length(); i ++) {
		if (str[i] != str[i - 1]) ret++;
	}
	if (str.back() == '-') ret++;
	return ret;
}

int main() {
	int t, T;
	string str;

	cin >> T;
	t = 0;
	while (T-- > 0) {
		cout << "Case #" << ++t << ": ";
		cin >> str;
		cout << getReverseTime(str) << endl;
	}
	return 0;
}
