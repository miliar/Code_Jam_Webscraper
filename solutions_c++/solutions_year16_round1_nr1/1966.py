#include <iostream>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <numeric>

using namespace std;

int main(int argc, char** argv)
{
	if (argc != 3)
		return -1;

	ifstream in(argv[1]);
	ofstream out(argv[2]);

	int t;
	string s;

	in >> t;

	for (int caseN = 1; caseN <= t; ++caseN) {
		in >> s;
		out << "Case #" << caseN << ": ";

		string r;
		r += s.at(0);

		for (unsigned int i = 1; i < s.length(); ++i) {
			char c = s.at(i);
			unsigned int j = 0;
			while (j < r.length() && r.at(j) == c) {
				++j;
			}
			if (j >= r.length() || r.at(j) >= c) {
				// append at end
				r += c;
			}
			else {
				// append at start
				r = c + r;
			}
		}
		out << r << endl;
	}


	in.close();
	out.close();

    return 0;
}



