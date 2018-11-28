#include<iostream>
#include<vector>
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

string process_testcase(string s)
{
	istringstream iss(s);
	ld C, F, X;
	ld cur_rate = 2.0;
	ld time_req = 0.0;

	iss >> C >> F >> X;
	
	while (1) {
		ld without_fact = X / cur_rate;
		ld with_new_fact = (ld)(X /(ld) (F + cur_rate)) +(ld) ((ld)C /(ld) cur_rate);

		if (with_new_fact < without_fact) {
			time_req += (ld)(C / cur_rate);
			cur_rate += F;
		}
		else {
			time_req += (ld)((ld)X /(ld) cur_rate);
			break;
		}
	}
	ostringstream oss;
	oss << std::fixed << setprecision(7) << time_req;
	// cout << "op : " << setprecision(10) << time_req << endl;
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
	int numchars, dic;
	iss >> tc;

	for (int i = 1; i <= tc; i++)
	{
		os << "Case #" << i << ": ";
		getline(is, s);
		os << process_testcase(s) << endl;
	}
	is.close();
	//getchar();
	return 0;
}