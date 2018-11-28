#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

int main () {
	int t;
	cin >> t;
	int count = 0;
	string str, ans = "";
	char s;
	for (int q = 0; q < t; q++) {
		count += 1;
		cin >> str;
		s = str[0];
		ans = ans + s;
		for (int i = 1; i < str.length(); i++) {
			
			if (str[i] < s) {
				ans = ans + str[i];
			}
			else {
				ans = str[i] + ans;
			}
			s = ans[0];
		}
		cout << "Case #" << count << ": " << ans << endl;
		ans = "";
		str = "";
	}
	return 0;
}