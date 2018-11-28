#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream fin("BIn.txt");
ofstream fout("BOut.txt");

#define cin fin
#define cout fout

int main() {
	int T;
	cin >> T;
	string s;
	getline(cin, s);
	for (int TC = 1; TC <= T; TC++) {
		int ans = 0;
		getline(cin, s);
		for (int i = s.length() - 1; i >= 0;) {
			if ((s[i] == '+' && ans % 2 == 1) || (s[i] == '-' && ans % 2 == 0)) {
				ans++;
			}
			i--;
			while (i > 0 && s[i] == s[i + 1]) {
				i--;
			}
		}
		cout << "Case #" << TC << ": " << ans << endl;
	}
}