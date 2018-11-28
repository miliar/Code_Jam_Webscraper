#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<algorithm>
#include<fstream>
#include<sstream>
#include <cmath>
#define DEBUG 0
#define dcout if(DEBUG) cout

using namespace std;

string process_testcase_two(string s);

string process_testcase_one(string s)
{
	string result;
	result += s[0];
	for (int i = 1; i < s.size(); ++i) {
		string tempS;
		tempS += s[i];
		if (s[i] < result[0]) {
			result = result + tempS;
		} else {
			result = tempS + result;
		}
	}

	return result;
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

