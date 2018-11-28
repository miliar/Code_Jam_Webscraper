#include <bits/stdc++.h>

using namespace std;

int main() {

    ifstream fin("D:\\Google Drive\\Descargas\\B-large.in");
    ofstream fout("D:\\Google Drive\\Descargas\\B-large.out");

	int T, y, pos;
	string s;

	fin >> T;

	for (int c=1; c<=T; c++) {
		fin >> s;
		y = 0;
		while (s.find('-') != string::npos) {
			if (s[0] == '+') {
				pos = s.find_first_of('-');
				s.replace(s.begin(), s.begin() + pos, string(pos, '-'));
				y++;
			} else {
				pos = s.find_first_of('+');
				if (pos == string::npos)
					pos = s.length();
				s.replace(s.begin(), s.begin() + pos, string(pos, '+'));
				y++;
			}
		}
		fout << "Case #" << c << ": " << y << endl;
	}

    return 0;
}