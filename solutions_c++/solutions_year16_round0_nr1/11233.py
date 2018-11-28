#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <stdlib.h>
using namespace std;

bool notSeen(char dig, string digits) {
	for (unsigned int i=0;i<digits.size();i++) {
		if (dig == digits[i]) return false;
	}

	return true;
}

int main(int argc, char* argv[]) {

	ifstream finp(argv[1]);

	if (!finp.is_open()) {
		cerr << "Unable to open input file " << argv[0] << endl;
	}

	ofstream fout("output.txt");

	string cases,num;
	ostringstream convert;
	long long t,n;
	int count,orig;
	getline(finp,cases);

	t = atoi(cases.c_str());

	count = 1;

	while(count <= t) {

		getline(finp,num);

		if (num == "0" || num == "") {
			fout << "Case #" << count << ": INSOMNIA" << endl;
			count++;
			continue;
		}

		string digits = "";
		orig = atoi(num.c_str());

		while(digits.size() < 10) {

			for (unsigned int i=0;i<num.size();i++) {

				if (notSeen(num[i],digits)) digits += num[i];

			}

			n = atoi(num.c_str());

			n += orig;
			ostringstream convert;
			convert << n;
			num = convert.str();

		}

		fout << "Case #" << count << ": " << n-orig << endl;
		count++;


	}

}