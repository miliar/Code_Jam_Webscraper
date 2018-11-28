#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream fin("CIn.txt");
ofstream fout("COut.txt");

#define cin fin
#define cout fout

int main() {
	int T;
	cin >> T;
	string s;
	getline(cin, s);
	for (int TC = 1; TC <= T; TC++) {
		int k, c, s;
		cin >> k >> c >> s;

		cout << "Case #" << TC << ":";
		for (int i = 1; i <= s; i++) {
			cout << " " << i;
		}
		cout << endl;
	}
}