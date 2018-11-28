#include <iostream>
#include <string>
#include <fstream>
#include <sstream>

using namespace std;

template<typename T>
T from_str(const std::string& s)
{
	std::istringstream is(s);
	T t;
	is >> t;
	return t;
}

int get_invited_num(int smax, string& digits)
{
	int invited_num = 0;
	int stand_num = 0;
	int i = 0;
	for (; i <= smax; ++i) {
		if (stand_num >= smax) break;
		if (digits[i] == '0') continue;
		if (i <= stand_num) {
			stand_num += digits[i] - '0';
		}
		else {
			invited_num += i - stand_num;
			stand_num += invited_num + digits[i] - '0';
		}
	}
	return invited_num;
}

int main()
{
	int test_num, smax;
	string digits;

	ifstream infile;
	infile.open("A-small-attempt2.in");
	ofstream outfile;
	outfile.open("out.txt");

	string tmp;
	getline(infile, tmp);
	test_num = from_str<int>(tmp);

	int i = 0;
	while (infile.good() && !infile.eof() && EOF != infile.peek()) {
		getline(infile, tmp);
		smax = from_str<int>(tmp.substr(0, 1));
		digits = tmp.substr(2);
		outfile << "Case #" << ++i << ": " << get_invited_num(smax, digits) << endl;
	}
	return 0;
}