#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<algorithm>
#include<fstream>
#include<sstream>
#include <cmath>

using namespace std;

string process_testcase_two(string s);

string process_testcase(string s)
{
	return s;
}

int main(int argc, const char *argv[])
{
	int tc = 0;
	ifstream is;
	if (argc == 1)
		is.open("input.txt");
	else
		is.open(argv[1]);

	string s;
	getline(is, s);
	istringstream iss(s);
	int numchars, dic;
	iss >> tc;

	for (int i = 1; i <= tc; i++)
	{
		printf("Case #%d: ", i);
		getline(is, s);
		cout << process_testcase_two(s) << endl;
	}
	is.close();
	return 0;
}

string process_testcase_two(string s)
{
	int result = 0;
	for (int i = s.size()-1; i>=0; --i) {
		if ((result%2) == 0) {
			// orientation unchanged.
			if (s[i] == '-') {
				++result;
			}
		} else {
			// orientation flipped
			if (s[i] == '+') {
				++result;
			}
		}
	}
	ostringstream r_ss;
	r_ss << result;
	return r_ss.str();
}

