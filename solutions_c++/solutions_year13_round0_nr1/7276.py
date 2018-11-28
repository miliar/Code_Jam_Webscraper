#include <iostream>
#include <map>
using namespace std;

int T;
char b[5][5];
map<char, int> m;
bool ans, complete;
bool check() {
	if(!ans) {
		if(m['X'] == 4 || m['X'] == 3 && m['T'] == 1) {
			cout << "X won" << endl;
			ans = true;
		} else if(m['O'] == 4 || m['O'] == 3 && m['T'] == 1) {
			cout << "O won" << endl;
			ans = true;
		}
	}
	m.clear();
}
int main() {
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		complete = true;
		ans = false;
		cout << "Case #" << t << ": ";
		for(int i = 0; i < 4; ++i) {
			for(int j = 0; j < 4; ++j) {
				cin >> b[i][j];
				if(b[i][j] == '.') { complete = false; }
			}
		}
		for(int i = 0; i < 4; ++i) {
			for(int j = 0; j < 4; ++j) {
				m[b[i][j]]++;
			}
			check();
		}
		for(int i = 0; i < 4; ++i) {
			for(int j = 0; j < 4; ++j) {
				m[b[j][i]]++;
			}
			check();
		}
		for(int j = 0; j < 4; ++j) {
			m[b[j][j]]++;
		}
		check();
		for(int j = 0; j < 4; ++j) {
			m[b[j][4-j-1]]++;
		}
		check();
		if(!ans) {
			if(complete) {
				cout << "Draw" << endl;
			} else {
				cout << "Game has not completed" << endl;
			}
		}
	}
	return 0;
}