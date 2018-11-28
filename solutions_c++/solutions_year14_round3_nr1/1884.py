#include<iostream>
#include<vector>
#include<deque>
#include<string>
#include<map>
#include<algorithm>
#include<fstream>
#include<sstream>
#include <cmath>
#include <iomanip>
#include "stdio.h"

using namespace std;
typedef  double ld;

#define DEBUG 1
#define dcout if (DEBUG) cout

vector<long long> pows;
string
process_input(int P, int Q)
{
	if (find(pows.begin(), pows.end(), Q) == pows.end()) {
		return "impossible";
	}
	int count = 1;
	
	if (Q % 2) {
		return "impossible";
	}

	Q /= 2;

	while ((count < 40) && (P < Q)) {
		if (Q % 2) {
			return "impossible";
		}
		++count;
		Q /= 2;
	}
	if (count > 40) {
		return "impossible";
	}

	ostringstream oss;
	oss << count;
	return oss.str();
}

int main(int argc, const char *argv[])
{
	int tc = 0;
	ifstream is;
	if (argc == 1)
		is.open("c:\\shiv\\gcj\\input.txt");
	else
		is.open(argv[1]);
	ofstream os;
	os.open("c:\\shiv\\gcj\\output.txt");

	string s;
	getline(is, s);
	istringstream iss(s);
	iss >> tc;

	pows.push_back(2);
	for (int i = 1; i < 40; ++i) {
		pows.push_back(pows[i - 1] * 2);
	}

	for (int i = 1; i <= tc; i++)
	{
		os << "Case #" << i << ": ";
		int P, Q;
		char temp;
		getline(is, s);
		istringstream iss(s);
		iss >> P >> temp >> Q;

		os << process_input(P, Q) << endl;
	}

	is.close();
	os.close();
//	getchar();
	return 0;
}