#include <iostream>

using namespace std;

int getMinS(string s) {
	for(int i = s.size() - 1; i >= 0 ; i--) {
		if(s.at(i) == '-') {
			return i;
		}
	}
	return -1;
}

int solve(string s) {
	int m = getMinS(s);
	if(m == -1) return 0;
	char t = s.at(0);
	int res = 0;
	for(int i = 1; i <= m; i++) {
		if(t != s.at(i)) {
			res++;
			t = s.at(i);
		}
	}
	return res + 1;
}

int main() {
	int tc;
	cin >> tc;
	for(int ctc = 1; ctc <= tc; ctc++) {
		string s;
		cin >> s;
		cout << "Case #" << ctc << ": " << solve(s) << endl;
	}
	return 0;
}
