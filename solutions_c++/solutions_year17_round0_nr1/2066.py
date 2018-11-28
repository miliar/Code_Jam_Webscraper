#include <iostream>
#include <fstream>

using namespace std;

int main(int argv, const char **args) {
	ifstream cin(args[1]);
	ofstream cout(args[2]);
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		string s;
		int fliperSize;
		cin >> s >> fliperSize;
		int flipTime = 0;
		bool possible = true;

		for (int j = 0; j <= s.length() - fliperSize; j++) {
			if (s[j] == '-') {
				flipTime++;
				for (int k = 0; k < fliperSize; k++) {
					s[j+k] = (s[j+k] == '-')?'+':'-';
				}
			}

		}

		for (int j = s.length() - fliperSize + 1; j < s.length(); j++) {
			if (s[j] == '-') {
				possible = false;
				break;
			}
		}

		cout << "Case #" << i << ": ";
		if (possible) {
			cout << flipTime;
		}else {
			cout << "IMPOSSIBLE";
		}
		cout << endl;

	}
	return 0;
}