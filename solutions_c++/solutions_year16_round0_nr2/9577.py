#include <bits/stdc++.h>

using namespace std;

int main () {
	ifstream fin ("b.in");
	ofstream fout ("b.out");
	int T;
	fin >> T;
	for (int tt = 0; tt < T; tt++) {
		fout << "Case #" << tt + 1 << ": ";
		string s;
		fin >> s;
		int cnt = 0;
		int up = 1;
		for (int i = s.size() - 1; i >= 0; i--) {
			cerr << tt+1 << " " << i << " " << cnt << endl;
			if (up == 1) {
				if (s[i] == '-') {
					cerr << i << "  " << cnt << endl;
					while (i >= 0 && s[i] == '-') i--;
					i++;
					cnt++;
					up *= -1;
					cerr << i << "  " << cnt << endl;					
				}
			}
			else {
				if (s[i] == '+') {
					cerr<<"Ddd\n";
					while (i >= 0 && s[i] == '+') i--;
					i++;
					cnt++;
					up *= -1;
					cerr << i << "  " << cnt << endl;					
				}
			}
		}
		fout << cnt << endl;
	}
	return 0;
}
