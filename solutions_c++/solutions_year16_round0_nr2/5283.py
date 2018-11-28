#include <bits/stdc++.h>

using namespace std;

void contract(string &str) {
	int end = str.length() - 1;
	while(end >= 0 && str[end] == '+') end--;
	str = str.substr(0, end + 1);
}

int change_start(string &str) {
	int len = str.length(), flag = 0;
	for(int i = 0; i < len && str[i] == '+'; i++) {
		str[i] = '-'; flag = 1;
	}
	return flag;
}

int rev(string &str) {
	int len = str.length();
	for(int i = 0; i < len; i++) {
		if(str[i] == '+') str[i] = '-';
		else if(str[i] == '-') str[i] = '+';
	}
	reverse(str.begin(), str.end());
	return (len != 0);
}

int main() {
	int t; cin >> t;
	string str;
	for(int testcase = 1; testcase <= t; testcase++) {
		cin >> str;
		int cnt = 0;
		while(str.length()) {
			contract(str);
			cnt += change_start(str);
			cnt += rev(str);
		}
		cout << "Case #" << testcase << ": ";
		cout << cnt << endl;
	}
	return 0;
}
