#include <iostream>
#include <string>
using namespace std;

int flip(string str) {
	bool flag = str[0] == '+' ? true : false;
	int ret = 0;
	for (int i = 1; i < str.size(); i++) {
		if (str[i] == str[i - 1]) continue;
		else {
			ret++;
			flag = !flag;
		}
	}
	if (!flag) ret++;
	return ret;
}

int main() {
	int cas;
	string str;
	cin >> cas;
	for (int i = 1; i <= cas; i++) {
		cin >> str;
		int ret = flip(str);
		cout << "Case #" << i << ": " << ret << endl;
	}
	return 0;
}

