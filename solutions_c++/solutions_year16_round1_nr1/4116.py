#include<cstdio>
#include <fstream>
#include <vector>
#include <string>
using namespace std;


int main()
{
	fstream f_in("A-large.in", fstream::in);
	fstream f_out("A-large.out", fstream::out);
	int t;
	f_in >> t;
	for (int i = 0; i < t; ++i) {
		string s;
		f_in >> s;
		string r;
		if (s.length() == 0) {
			f_out << "Case #" << i + 1 << ": \n";
			continue;
		}
		r += s[0];
		for (int j = 1; j < s.length(); ++j) {
			if (s[j] >= r[0]) {
				r = s[j] + r;
			}
			else {
				r = r + s[j];
			}

		}
		f_out << "Case #" << i + 1 << ": " << r << "\n";
	}







	return 0;
}