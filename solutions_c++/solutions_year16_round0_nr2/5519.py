#include <fstream>
#include <vector>
#include <string>
using namespace std;

void main() {
	ifstream in("B-large.in");
	ofstream out("out.txt");
	int t;
	in >> t;
	for (int i = 0; i < t; ++i) {
		string s;
		in >> s;
		out << "Case #" << i + 1 << ": ";
		int blocks = 0;
		for (int j = 1; j < s.size(); ++j) {
			if (s[j] != s[j - 1])
				blocks++;
		}
		if (s.back() == '-')
			blocks++;
		out << blocks << endl;
	}
	in.close();
	out.close();
}