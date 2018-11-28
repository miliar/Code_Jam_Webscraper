#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int ans = 0;
bool testEnd(string str) {
	int len = str.length();
	for (int i = 0; i < len; ++i) {
		if (str[i] != '+')
			return false;
	}
	return true;
}

int main(int argc, char* argv[]) {
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		string s;
		cin >> s;
		ans = 0;
		int len = s.length();
		if (s[len-1] == '-') {
			ans++;
		}
		for (int j = len-2; j >= 0; j--) {
			if (s[j] != s[j+1]) {
				ans++;
			}
		}
		cout << "Case #" << i << ": "<< ans << endl;
	}
}