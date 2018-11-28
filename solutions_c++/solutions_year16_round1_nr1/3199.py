#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int T;
string s1, s2;

int main() {
	ifstream in("in.txt");
	ofstream out("out.txt");

	in >> T;

	for(int t = 1; t <= T; t++) {
		out << "Case #" << t << ": ";

		in >> s1;
		s2 = s1.substr(0, 1);

		for(int i = 1; i < s1.length(); i++) {
			if(s1.at(i) >= s2.at(0)) {
				s2 = s1.at(i) + s2;
			} else {
				s2 += s1.at(i);
			}
		}

        out << s2 << endl;
	}

	return 0;
}
