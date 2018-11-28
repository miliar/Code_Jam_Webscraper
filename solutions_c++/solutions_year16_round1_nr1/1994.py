#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main() {
	int t;
	cin >> t;

	ofstream ofs("thelastword.txt");
	string str, ans;
	int c = 1;
	while (t--) {
		cin >> str;
		int len = str.length();

		ans = str[0];
		for (int i = 1; i < len; ++i) {
			if (str[i] >= ans[0]) {
				ans = str[i]+ans;
			}
			else {
				ans += str[i];
			}
		}

		ofs << "Case #" << c++ << ": " << ans << endl;
	}
}