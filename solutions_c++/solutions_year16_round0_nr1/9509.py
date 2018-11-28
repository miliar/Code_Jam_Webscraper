#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<algorithm>
#include<fstream>
#include<sstream>
#include <cmath>

using namespace std;

string process_testcase_two(string s);

string process_testcase_one(string s)
{
	long long ip;
	long long multiplier = 1;
	istringstream iss(s);

	iss >> ip;

	if (ip == 0) {
		return "INSOMNIA";
	}

	set<int> unfound;
        for (int i = 0; i < 10; ++i) {
		unfound.insert(i);
	}

       unsigned long long prod;
	while (unfound.size() > 0) {
		prod = ip * multiplier;
		//cout << "Prod : " << prod << endl;
		while (prod) {
			int cur_digit = (prod%10);
		//	cout << "erasing " << cur_digit << endl;
			unfound.erase(cur_digit);
			prod /= 10;
		}

		if (unfound.size() == 0)
			break;

		++multiplier;
	}

	ostringstream oss;
	oss<< ip * multiplier;

	return oss.str();
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
		cout << process_testcase_one(s) << endl;
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

