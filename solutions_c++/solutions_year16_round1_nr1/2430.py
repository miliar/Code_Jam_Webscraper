#include <fstream>
#include <string>
#include <list>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("out.txt");

int main() {
	int tests;
	fin >> tests;

	for(int test = 0; test < tests; ++test) {
		string s;
		list<char> res;
		fin >> s;
		res.insert(res.begin(), s[0]);
		for (int i = 1; i < s.length(); ++i) {
			if (s[i] >= *res.begin()) {
				res.insert(res.begin(), s[i]);
			} else {
				res.insert(res.end(), s[i]);
			}
		}

		fout << "Case #" << test + 1 << ": ";
		for (list<char>::iterator i = res.begin(); i != res.end(); ++i) {
			fout << *i;
		}
		fout << endl;
	}

	return 0;
}
