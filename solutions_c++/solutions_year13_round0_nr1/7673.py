#include <iostream>
using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T = 0; cin >> T;
	for(int i = 1; i <= T; ++i) {
		cout << "Case #" << i << ": ";

		char s[20];
		cin >> s;
		cin >> s + 4;
		cin >> s + 8;
		cin >> s + 12;

		int p = 0;
		int o = 0, x = 0;
		int o1 = 0, x1 = 0;
		for(int j = 0; j < 4; ++j) {
			o1 = 0; x1 = 0;
			for(int k = 0; k < 4; ++k) {
				if(s[j * 4 + k] == 'X')
					++x1;
				else if(s[j * 4 + k] == 'O')
					++o1;
				else if(s[j * 4 + k] == 'T') {
					++o1; ++x1;
				} else
					++p;
			}
			if(o1 > o) o = o1;
			if(x1 > x) x = x1;
		}

		for(int j = 0; j < 4; ++j) {
			o1 = 0; x1 = 0;
			for(int k = 0; k < 4; ++k) {
				if(s[j + k * 4] == 'X')
					++x1;
				else if(s[j + k * 4] == 'O')
					++o1;
				else if(s[j + k * 4] == 'T') {
					++o1; ++x1;
				} else
					break;
			}
			if(o1 > o) o = o1;
			if(x1 > x) x = x1;
		}

		o1 = 0; x1 = 0;
		for(int j = 0; j < 4; ++j) {
			if(s[j + j * 4] == 'X')
				++x1;
			else if(s[j + j * 4] == 'O')
				++o1;
			else if(s[j + j * 4] == 'T') {
				++o1; ++x1;
			} else
				break;
		}
		if(o1 > o) o = o1;
		if(x1 > x) x = x1;

		o1 = 0; x1 = 0;
		for(int j = 0; j < 4; ++j) {
			if(s[(3 - j) + j * 4] == 'X')
				++x1;
			else if(s[(3 - j) + j * 4] == 'O')
				++o1;
			else if(s[(3 - j) + j * 4] == 'T') {
				++o1; ++x1;
			} else
				break;
		}
		if(o1 > o) o = o1;
		if(x1 > x) x = x1;

		if(o == 4 && x == 4)
			cout << "Draw";
		else if(o == 4)
			cout << "O won";
		else if(x == 4)
			cout << "X won";
		else if(p == 0)
			cout << "Draw";
		else
			cout << "Game has not completed";
		cout << endl;
	}

	return 0;
}
