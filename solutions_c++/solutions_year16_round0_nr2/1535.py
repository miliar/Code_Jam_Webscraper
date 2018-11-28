#include <iostream>
#include <string>



using namespace std;

void solve(string s) {
	int count = 1;
	char c = s.at(0);
	int len = s.length();
	for (int i = 0; i < len;i++) {
		if (c != s.at(i)) {
			c = s.at(i);
			count ++;
		}
	}
	if (c == '+') {
		count --;
	}
	cout << count << endl;
}




int main() {
	int T;

	cin >> T;

	for (int i = 0; i < T; i++) {
		string s;
		cin >> s;
		cout << "Case #" << i + 1 << ": ";
		solve(s);
	}
	return 0;
}