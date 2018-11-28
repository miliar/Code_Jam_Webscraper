#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

int main() {
	ifstream in("B-large.in");
	cin.rdbuf(in.rdbuf());
	ofstream out("B-large.out");
	cout.rdbuf(out.rdbuf());
	// read
	string s;
	int kase = 1, n, slen;
	cin >> n;
	while (n--) {
		int count = 0;
		cin >> s;
		slen = s.length();
		for (int i = 1 ; i < slen; ++i) {
			if (s[i] != s[i-1]) ++count;
		}
		if (s[slen - 1] == '-') ++count;
		cout << "Case #" << kase++ << ": ";
		cout << count << endl;
	}
}