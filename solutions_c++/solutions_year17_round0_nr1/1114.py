#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
	ifstream in;
	ofstream out;

	in.open("C:\\works\\in.txt");
	out.open("C:\\works\\out.txt");

	int n;

	in >> n;

	for (int i = 0; i < n; i++) {
		string s;
		int k;
		in >> s;
		in >> k;
		int count = 0;
		bool possible = true;
		int pos = 0;
		while (pos < s.size()) {
			if (s[pos] == '-') {
				if (pos + k > s.size()) {
					possible = false;
					break;
				}
				else {
					count++;
					for (int j = 0; j < k; j++) {
						s[pos + j] = s[pos + j] == '-' ? '+' : '-';
					}
				}
			}
			pos++;
		}
		out << "Case #" << i + 1 << ": ";
		if (possible) {
			out << count;
		}
		else {
			out << "IMPOSSIBLE";
		}
		out << endl;
	}
}